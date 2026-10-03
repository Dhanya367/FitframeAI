"""Body measurement + classification using MediaPipe Pose and OpenCV."""
import math
import cv2
import numpy as np
import mediapipe as mp

mp_pose = mp.solutions.pose
L_SH, R_SH, L_HIP, R_HIP = 11, 12, 23, 24


class AnalysisError(Exception):
    pass


def _load(data):
    img = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise AnalysisError("Could not read the image. Use a JPG or PNG.")
    scale = 640 / max(img.shape[:2])
    return cv2.resize(img, None, fx=scale, fy=scale) if scale < 1 else img


def _detect(img):
    with mp_pose.Pose(static_image_mode=True, model_complexity=1,
                      enable_segmentation=True) as pose:
        r = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if not r.pose_landmarks or r.segmentation_mask is None:
        raise AnalysisError("No body detected. Use a full-body photo.")
    h, w = img.shape[:2]
    pts = [(l.x * w, l.y * h, l.visibility) for l in r.pose_landmarks.landmark]
    if any(pts[i][2] < 0.5 for i in (L_SH, R_SH, L_HIP, R_HIP)):
        raise AnalysisError("Shoulders/hips not clearly visible. Stand in full view.")
    return pts, r.segmentation_mask > 0.5


def _run(mask, y, cx):
    """Width of the body silhouette on row y, for the run containing cx."""
    y = min(max(int(y), 0), mask.shape[0] - 1)
    row = mask[y]
    idx = np.flatnonzero(row)
    if idx.size == 0:
        return 0
    x = int(idx[np.argmin(abs(idx - cx))])
    l = r = x
    while l > 0 and row[l - 1]:
        l -= 1
    while r < len(row) - 1 and row[r + 1]:
        r += 1
    return r - l + 1


def _widths(img_bytes):
    """Shoulder, waist, hip widths and total body height, all in pixels."""
    pts, mask = _detect(_load(img_bytes))
    sy = (pts[L_SH][1] + pts[R_SH][1]) / 2
    hy = (pts[L_HIP][1] + pts[R_HIP][1]) / 2
    cx = (pts[L_HIP][0] + pts[R_HIP][0]) / 2
    torso = hy - sy
    if torso < 30:
        raise AnalysisError("Torso too small in the photo. Step back, full body.")
    band = lambda a, b: [_run(mask, sy + torso * t, cx) for t in np.linspace(a, b, 8)]
    sh = max(band(0.0, 0.15))
    wa = min(w for w in band(0.45, 0.80) if w > 0)
    hi = max(band(1.0, 1.35))
    rows = np.flatnonzero(mask.any(axis=1))
    return sh, wa, hi, int(rows[-1] - rows[0])


def classify(sh, wa, hi, side_ratio=None):
    big, avg = max(sh, hi), (sh + hi) / 2
    # THRESHOLDS: tune these after testing with real photos
    if wa / big >= 0.92 or (side_ratio and side_ratio >= 0.95 and wa / big >= 0.85):
        return "Apple"
    if hi / sh > 1.05:
        return "Pear"
    if sh / hi > 1.05:
        return "Inverted Triangle"
    return "Hourglass" if wa / avg <= 0.78 else "Rectangle"


def _girth(width, depth):
    """Body cross-section as an ellipse -> circumference (Ramanujan)."""
    a, b = width / 2, depth / 2
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))


DEPTH_RATIO = 0.70  # average front-to-back depth / width, used without a side photo


def analyze(front_bytes, side_bytes, height_cm):
    sh, wa, hi, bh = _widths(front_bytes)
    if bh < 300:
        raise AnalysisError("Full body not detected. Step back so head to feet are in frame.")
    k = height_cm / bh                      # centimetres per pixel
    w_wa, w_hi = wa * k, hi * k
    d_wa, d_hi = w_wa * DEPTH_RATIO, w_hi * DEPTH_RATIO
    side_ratio, used_side = None, False
    if side_bytes:
        try:
            _, s_wa, s_hi, s_bh = _widths(side_bytes)
            ks = height_cm / s_bh
            d_wa = min(max(s_wa * ks, 0.5 * w_wa), 0.95 * w_wa)
            d_hi = min(max(s_hi * ks, 0.5 * w_hi), 0.95 * w_hi)
            side_ratio, used_side = s_wa / s_hi, True
        except AnalysisError:
            pass
    cm = {"shoulder": sh * k, "waist": _girth(w_wa, d_wa), "hip": _girth(w_hi, d_hi)}
    res = {"body_type": classify(sh, wa, hi, side_ratio), "used_side": used_side}
    for key, v in cm.items():
        res[key + "_cm"] = round(v)
        res[key + "_in"] = round(v / 2.54 * 2) / 2
    return res
