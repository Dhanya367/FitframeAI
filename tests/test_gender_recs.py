from fitframe.recommendations import get_recommendations


def test_style_preferences_are_tailored_by_body_type_and_height():
    feminine = get_recommendations("Pear", "Feminine", 165)
    masculine = get_recommendations("Pear", "Masculine", 180)
    short = get_recommendations("Hourglass", "Feminine", 155)
    tall = get_recommendations("Hourglass", "Feminine", 190)

    assert feminine["outfits"] != masculine["outfits"]
    assert any("skirt" in item.lower() or "dress" in item.lower() for item in feminine["outfits"])
    assert any("trouser" in item.lower() or "polo" in item.lower() for item in masculine["outfits"])
    assert any("cropped" in item.lower() for item in short["tips"]) or any("cropped" in item.lower() for item in short["outfits"])
    assert any("long" in item.lower() or "ankle" in item.lower() for item in tall["tips"]) or any("long" in item.lower() or "ankle" in item.lower() for item in tall["outfits"])
