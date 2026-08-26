import re

with open("index.html", "r") as f:
    html = f.read()

# Replace the 700x350 placehold.co images with HTML divs
html = html.replace('<img src="https://placehold.co/700x350/024AD8/FFF?text=700+x+350" alt="Placeholder 700x350" style="width: 100%; height: 100%; object-fit: cover; display: block;" />',
                    '<div style="width: 100%; height: 100%; background-color: #024AD8; display: flex; align-items: center; justify-content: center; color: white; font-size: 1rem; font-weight: 500; text-decoration: none;">700 x 350</div>')


# Replace the large carousel banners with HTML divs (1400 x 400)
# We need to replace the entire <picture>...</picture> blocks inside the .banner-slide <a> tags
# Let's just find each picture block and replace it.

picture_regex = re.compile(r'<picture style="width: 100%; height: 100%; display: block;">.*?</picture>', re.DOTALL)

replacement_div = '<div style="width: 100%; height: 100%; background-color: #024AD8; display: flex; align-items: center; justify-content: center; color: white; font-size: 1rem; font-weight: 500; text-decoration: none;">1400 x 400</div>'

html = picture_regex.sub(replacement_div, html)

with open("index.html", "w") as f:
    f.write(html)
