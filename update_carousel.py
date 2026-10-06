import re

with open("index.html", "r") as f:
    html = f.read()

# Replace inputs
old_inputs = """            <!-- Radio inputs for state management -->
            <input type="radio" id="banner1" name="banner-carousel" checked />
            <input type="radio" id="banner2" name="banner-carousel" />
            <input type="radio" id="banner3" name="banner-carousel" />
            <input type="radio" id="banner4" name="banner-carousel" />"""
new_inputs = """            <!-- Radio inputs for state management -->
            <input type="radio" id="banner1" name="banner-carousel" checked />
            <input type="radio" id="banner2" name="banner-carousel" />
            <input type="radio" id="banner3" name="banner-carousel" />"""
html = html.replace(old_inputs, new_inputs)

# Replace pagination
old_pagination = """            <!-- Pagination dots -->
            <div class="banner-pagination">
              <label for="banner1"></label>
              <label for="banner2"></label>
              <label for="banner3"></label>
              <label for="banner4"></label>
            </div>"""
new_pagination = """            <!-- Pagination dots -->
            <div class="banner-pagination">
              <label for="banner1"></label>
              <label for="banner2"></label>
              <label for="banner3"></label>
            </div>"""
html = html.replace(old_pagination, new_pagination)

# Replace banner slides
# Using regex to grab the whole div since it has commented out code inside
slides_regex = re.compile(r'<!-- Banners container -->.*?</div>\s*<!-- Pagination dots -->', re.DOTALL)
new_slides = """<!-- Banners container -->
            <div class="banner-slides-container">
              <a href="https://www.konga.com/search?q=HPLaptop" class="banner-slide">
                <img src="https://www-konga-com-res.cloudinary.com/image/upload/v1791293857/landingPages/2026%20Marketing/HPSIS/carousel1.png" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
              </a>
              <a href="https://www.konga.com/search?q=HPGaming" class="banner-slide">
                <img src="https://www-konga-com-res.cloudinary.com/image/upload/v1791293859/landingPages/2026%20Marketing/HPSIS/carousel2.gif" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
              </a>
              <a href="https://www.konga.com/search?q=HPLaptop" class="banner-slide">
                <img src="https://www-konga-com-res.cloudinary.com/image/upload/v1791293858/landingPages/2026%20Marketing/HPSIS/carousel3.png" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
              </a>
            </div>

            <!-- Pagination dots -->"""
html = slides_regex.sub(new_slides, html)


# Replace JS variable
html = html.replace('const bannerTotal = 4;', 'const bannerTotal = 3;')


with open("index.html", "w") as f:
    f.write(html)
