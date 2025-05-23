def format_star_rating(rating):
    full_stars = int(rating)
    half_star = rating - full_stars >= 0.5
    empty_stars = 5 - full_stars - (1 if half_star else 0)
    
    stars_html = ""
    # Full stars
    for _ in range(full_stars):
        stars_html += '<span style="color: gold; font-size: 24px;">★</span>'
    
    # Half star if needed
    if half_star:
        stars_html += '<span style="color: gold; font-size: 24px;">⯨</span>'
    
    # Empty stars
    for _ in range(empty_stars):
        stars_html += '<span style="color: #ccc; font-size: 24px;">☆</span>'
    
    return f'<div style="text-align: center;">{stars_html} <span style="font-size: 20px; vertical-align: middle; margin-left: 10px;">{rating}/5.0</span></div>'
