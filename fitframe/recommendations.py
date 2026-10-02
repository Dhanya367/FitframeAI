RECS = {
    "Rectangle": {
        "summary": "Shoulders, waist and hips are similar in width. Goal: create curves.",
        "outfits": ["Peplum tops and ruffled blouses", "Belted dresses and wrap dresses", "High-waisted flared trousers", "Layered looks with textures"],
        "colors": ["Pastels on top, bold on bottom", "Color-blocking", "Rich jewel tones"],
        "tips": ["Define the waist with belts", "Add volume with ruffles or pleats", "Avoid boxy, straight cuts"]},
    "Pear": {
        "summary": "Hips are wider than shoulders. Goal: balance the upper body.",
        "outfits": ["Boat-neck and off-shoulder tops", "A-line skirts and dresses", "Structured blazers with shoulder detail", "Dark straight or bootcut jeans"],
        "colors": ["Bright or light colors on top", "Dark colors on bottom", "Bold prints on top"],
        "tips": ["Draw attention upward with necklines", "Avoid clingy fabrics on hips", "Choose wide-leg over skinny"]},
    "Apple": {
        "summary": "Fuller midsection with slimmer legs. Goal: elongate the torso and show off legs.",
        "outfits": ["Empire-waist tops and dresses", "V-neck tops", "Straight-leg trousers", "Open jackets and long cardigans"],
        "colors": ["Solid darker tones on the torso", "Bright colors on legs or accessories", "Monochrome outfits"],
        "tips": ["Avoid tight belts at the waist", "Choose flowy, non-clingy fabrics", "Show off legs with knee-length hems"]},
    "Hourglass": {
        "summary": "Shoulders and hips balanced with a defined waist. Goal: highlight the waist.",
        "outfits": ["Wrap dresses", "Fitted tailored blazers", "High-waisted pencil skirts", "Belted coats"],
        "colors": ["Almost any color works", "Monochrome for a long line", "Medium-scale prints"],
        "tips": ["Emphasize the waist", "Avoid shapeless, oversized cuts", "Choose stretchy, fitted fabrics"]},
    "Inverted Triangle": {
        "summary": "Shoulders are wider than hips. Goal: add volume below, soften the top.",
        "outfits": ["A-line and full skirts", "Wide-leg pants", "Scoop or V-neck tops", "Printed or bright bottoms"],
        "colors": ["Darker, simple colors on top", "Bright or patterned bottoms", "Soft neutrals above"],
        "tips": ["Avoid shoulder pads and puff sleeves", "Add detail at the hips", "Choose soft, drapey fabrics on top"]},
}

STYLE_PRESETS = {
    "Feminine": {
        "general": {
            "outfits": ["Soft drape silhouettes", "Fitted waist definition", "Lightweight layering pieces"],
            "colors": ["Blush, ivory, soft rose, warm neutrals", "Soft jewel tones", "Muted pastels"],
            "tips": ["Use cinched waists and gentle structure", "Choose flattering necklines and balanced layers", "Keep proportions polished rather than oversized"]
        },
        "Pear": {
            "outfits": ["Off-shoulder tops and fitted knitwear", "A-line midi skirts and wrap styles", "Tailored blazers with a clean shoulder line", "Dark straight or bootcut jeans"],
            "colors": ["Soft ivory and blush on top", "Deep indigo or charcoal on bottom", "Soft jewel tones"],
            "tips": ["Create balance with structured shoulders", "Choose lighter tops to brighten your upper half", "Stay away from overly clingy bottoms"]
        },
        "Apple": {
            "outfits": ["Empire-waist dresses and draped tops", "V-neckline knits", "Straight-leg trousers with ankle length", "Open longline cardigans"],
            "colors": ["Soft charcoal and warm neutrals", "Muted rose and dusty blue", "Cream and gold accents"],
            "tips": ["Add vertical clean lines to lengthen the torso", "Avoid bulky waist belts", "Let the legs stay the focal point"]
        },
        "Hourglass": {
            "outfits": ["Wrap midi dresses", "Fitted tailored blazers", "High-waisted pencil skirts", "Belted coats"],
            "colors": ["Soft contrast and tonal layering", "Warm neutrals and jewel tones", "Medium-scale prints"],
            "tips": ["Highlight the waist without excess volume", "Keep silhouettes clean and fitted", "Add shape with defined shoulders or structured belts"]
        },
        "Rectangle": {
            "outfits": ["Peplum tops and softly draped shirts", "Belted dresses and wrap midi cuts", "High-waisted relaxed trousers", "Textured layering pieces"],
            "colors": ["Pastels with contrast accents", "Soft jewel tones", "Cream and taupe"],
            "tips": ["Create soft curves with ruching and waist emphasis", "Try gentle volume at the shoulder", "A structured belt will sharpen the silhouette"]
        },
        "Inverted Triangle": {
            "outfits": ["A-line skirts with soft volume", "Wide-leg pants in fluid fabric", "Scoop-neck tops and draped layers", "Printed bottoms with simple tops"],
            "colors": ["Soft neutrals on top", "Warm patterned bottoms", "Muted jewel tones"],
            "tips": ["Soften the shoulder line with drape", "Balance width with fuller skirts and fluid pants", "Keep the top layer light and clean"]
        }
    },
    "Masculine": {
        "general": {
            "outfits": ["Structured shirting", "Clean line jackets", "Minimal layering", "Tailored trousers"],
            "colors": ["Charcoal, navy, stone, olive", "Muted browns and greys", "Subtle contrast tones"],
            "tips": ["Build shape with a strong shoulder line", "Keep fits clean and intentional", "Use crisp lines instead of excess volume"]
        },
        "Pear": {
            "outfits": ["Structured polos and fine-gauge knits", "Relaxed-fit jackets with a sharp shoulder", "Dark denim and tapering trousers", "Layered lightweight knits"],
            "colors": ["Mid-toned blues and charcoal", "Clean whites and navy", "Muted earth tones"],
            "tips": ["Keep shoulders balanced with tailored tops", "Let the trousers stay clean and structured", "Avoid oversized silhouettes that widen the hips"]
        },
        "Apple": {
            "outfits": ["Structured knit polos", "Longline open shirts", "Straight-leg trousers with a clean hem", "Boxy lightweight jackets"],
            "colors": ["Charcoal and navy", "Stone and olive", "Deep navy accents"],
            "tips": ["Keep the torso long and unbroken", "Use vertical lines and soft structure", "Stay away from oversized or bulky waist layers"]
        },
        "Hourglass": {
            "outfits": ["Tailored blazers", "Structured knitwear", "High-waisted trousers", "Relaxed overcoats"],
            "colors": ["Dark neutrals and deep blue", "Stone and charcoal", "Muted contrast tones"],
            "tips": ["Define the waist while keeping the line clean", "Use sharper shoulders and subtle structure", "Avoid boxy cuts that hide the waist"]
        },
        "Rectangle": {
            "outfits": ["Structured shirts with texture", "Belted outerwear", "Straight-leg trousers", "Layered soft knits"],
            "colors": ["Stone, charcoal, navy", "Cool grey and olive", "Muted contrast layers"],
            "tips": ["Add shape with texture and defined waist lines", "Avoid oversized silhouettes that hide your frame", "Keep proportions sleek and clean"]
        },
        "Inverted Triangle": {
            "outfits": ["Lightweight crew shirts", "Relaxed trousers and chinos", "Straight-cut jackets", "Printed bottoms with lighter tops"],
            "colors": ["Stone and camel on top", "Dark denim and olive bottoms", "Muted layered neutrals"],
            "tips": ["Soften the upper body with clean drape", "Add visual weight below the waist", "Avoid heavy shoulder structure and puffed sleeves"]
        }
    },
    "Unisex": {
        "general": {
            "outfits": ["Balanced silhouettes", "Relaxed layering", "Modern utility pieces", "Neutral statement basics"],
            "colors": ["Olive, charcoal, stone, cobalt", "Earthy neutrals", "Crisp black and off-white"],
            "tips": ["Aim for proportion and comfort", "Use layers that suit your shape without overpowering it", "Keep your palette flexible and adaptable"]
        },
        "Pear": {
            "outfits": ["Boat-neck tops and relaxed jackets", "A-line skirts, tailored trousers, or relaxed denim", "Structured layers with soft shoulders", "Simple modern separates"],
            "colors": ["Charcoal, deep navy, muted olive", "Earthy beige and soft slate", "Crisp accent colors on top"],
            "tips": ["Balance the upper body with clean necklines", "Stay consistent with proportion and structure", "Choose easy drape over extra volume on the hips"]
        },
        "Apple": {
            "outfits": ["Relaxed shirting and draped layers", "Straight-leg trousers", "Longline outerwear", "Soft structure at the shoulder"],
            "colors": ["Neutral layers with subtle contrast", "Slate, taupe, olive, deep navy", "Soft accent pops"],
            "tips": ["Keep lines long and clean", "Avoid tight waist-bands and bulky layers", "Let the lower half stay easy and relaxed"]
        },
        "Hourglass": {
            "outfits": ["Wrap silhouettes", "Soft tailored blazers", "High-waisted trousers", "Balanced layered knits"],
            "colors": ["Muted contrast and bold neutrals", "Soft earth tones and mid-tone blues", "Clean monochrome combinations"],
            "tips": ["Keep the waist defined without overdoing volume", "Mix structure with softness", "Choose fabrics with a little movement"]
        },
        "Rectangle": {
            "outfits": ["Belted shirts and soft structure", "Relaxed flares and wide-leg cuts", "Layered light knits", "Polished simple dresses or separates"],
            "colors": ["Soft contrast neutrals", "Muted jewel tones", "Earthy and stone shades"],
            "tips": ["Add shape with waist emphasis and soft volume", "Keep silhouettes modern and easy", "Use texture instead of excess bulk"]
        },
        "Inverted Triangle": {
            "outfits": ["Fluid tops with simple lines", "A-line or gently flared bottoms", "Relaxed modern layering", "Printed lower pieces"],
            "colors": ["Dark simple tops with light bottoms", "Neutral earth tones", "Subtle statement colors"],
            "tips": ["Soften the shoulder line", "Add volume below the waist", "Use clean finishes and a balanced palette"]
        }
    }
}


def normalize_style(value):
    style = (value or "").strip().lower()
    mapping = {
        "feminine": "Feminine",
        "female": "Feminine",
        "womanly": "Feminine",
        "masculine": "Masculine",
        "male": "Masculine",
        "manly": "Masculine",
        "unisex": "Unisex",
        "neutral": "Unisex",
        "gender-neutral": "Unisex",
    }
    return mapping.get(style, "Unisex")


def _height_adjustments(height_cm):
    try:
        height = float(height_cm or 0)
    except (TypeError, ValueError):
        return {}
    if height <= 160:
        return {
            "outfits": ["Choose knee-length or slightly cropped layers to keep your proportions balanced", "Opt for streamlined hems that don't overwhelm your frame"],
            "tips": ["Keep vertical lines clean and avoid long bulky layers", "Use waist emphasis to lengthen the leg line"]
        }
    if height >= 180:
        return {
            "outfits": ["Choose longer jackets, ankle-length trousers, and extended outer layers", "Let the line continue through the body for a balanced silhouette"],
            "tips": ["Keep proportions long and even", "Avoid cuts that stop too early and shorten the look"]
        }
    return {}


def get_recommendations(body_type, style=None, height_cm=None):
    base = RECS.get(body_type, RECS["Hourglass"]).copy()
    rec = {key: list(value) if isinstance(value, list) else value for key, value in base.items()}
    style = normalize_style(style)
    style_set = STYLE_PRESETS.get(style, STYLE_PRESETS["Unisex"])
    if body_type in style_set:
        rec.update(style_set[body_type])
    elif "general" in style_set:
        rec.update(style_set["general"])

    height_adjust = _height_adjustments(height_cm)
    for key, values in height_adjust.items():
        if key in rec and isinstance(values, list):
            rec[key] = values + rec[key]

    return rec

