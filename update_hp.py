import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Replace title
content = content.replace('<title>Konga ASUS Shop In Shop</title>', '<title>Konga HP Shop In Shop</title>')

# 2. Replace Navbar
navbar_old = """    <header class="navbar">
      <nav class="navbar-container">
        <div class="navbar-logo">
          <img src="https://upload.wikimedia.org/wikipedia/commons/2/2e/ASUS_Logo.svg" alt="ASUS Logo" />
        </div>
        <div class="nav-wrapper">
          <ul class="nav-items">
            <li><a href="https://www.konga.com/search?q=ASUSLaptop">Laptops</a></li>
            <li><a href="https://www.konga.com/search?q=ASUSGamingg1">ROG Gaming</a></li>
            <li><a href="https://www.konga.com/search?q=ASUSComponents">Components</a></li>
            <li><a href="https://www.konga.com/search?q=ASUSMonitor">Monitors</a></li>
            <li><a href="https://www.konga.com/search?q=ASUS">Accessories</a></li>
          </ul>
        </div>
      </nav>
    </header>"""

navbar_new = """    <header class="navbar">
      <nav class="navbar-container">
        <div class="navbar-logo">
          <img src="https://upload.wikimedia.org/wikipedia/commons/a/ad/HP_logo_2012.svg" alt="HP Logo" style="height: 40px;"/>
        </div>
        <div class="nav-wrapper">
          <ul class="nav-items">
            <li><a href="https://www.konga.com/search?q=HPLaptop">Laptops</a></li>
            <li><a href="https://www.konga.com/search?q=HPGaming">Omen Gaming</a></li>
            <li><a href="https://www.konga.com/search?q=HPComponents">Components</a></li>
            <li><a href="https://www.konga.com/search?q=HPMonitor">Monitors</a></li>
            <li><a href="https://www.konga.com/search?q=HP">Accessories</a></li>
          </ul>
        </div>
      </nav>
    </header>"""
content = content.replace(navbar_old, navbar_new)

# 3. Shop by Category Replacement
shop_cat_old = """    <!-- Shop By Category Section -->
    <section class="shop-by-category-section section-reset" style="margin-top: 2rem !important;">
      <div class="shop-by-category-header" style="background-color: #111111; border-radius: 12px 12px 0 0;">Shop By Category</div>
      <div class="shop-category-container">
        <div class="shop-category-grid">
          <!-- Card 1 -->
          <a href="https://www.konga.com/search?q=ASUSLaptop" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Z/U/118566_1775817835.png" alt="Laptops" />
            </div>
            <div class="shop-category-label">Laptops</div>
          </a>
          <!-- Card 2 -->
          <a href="https://www.konga.com/search?q=ASUSGamingg1" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/D/U/57289_1778592626.jpg" alt="Gaming" />
            </div>
            <div class="shop-category-label">Gaming</div>
          </a>
          <!-- Card 3 -->
          <a href="https://www.konga.com/search?q=ASUSComponents" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/O/209656_1781270619.jpg" alt="Components" />
            </div>
            <div class="shop-category-label">Components</div>
          </a>
          <!-- Card 4 -->
          <a href="https://www.konga.com/search?q=ASUSMonitor" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/Y/163031_1778853996.jpg" alt="Monitors" />
            </div>
            <div class="shop-category-label">Monitors</div>
          </a>
        </div>
      </div>
    </section>"""

shop_cat_new = """    <!-- Shop By Category Section -->
    <section class="shop-by-category-section section-reset" style="margin-top: 2rem !important;">
      <div class="shop-by-category-header" style="background-color: #111111; border-radius: 12px 12px 0 0;">Shop By Category</div>
      <div class="shop-category-container">
        <div class="shop-category-grid">
          <!-- Card 1 -->
          <a href="https://www.konga.com/search?q=HP+Gaming+Laptops" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/D/U/57289_1778592626.jpg" alt="Gaming Laptops" />
            </div>
            <div class="shop-category-label">Gaming Laptops</div>
          </a>
          <!-- Card 2 -->
          <a href="https://www.konga.com/search?q=HP+Students+Laptops" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Z/U/118566_1775817835.png" alt="Students Laptops" />
            </div>
            <div class="shop-category-label">Students Laptops</div>
          </a>
          <!-- Card 3 -->
          <a href="https://www.konga.com/search?q=HP+All+in+Ones" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/Y/163031_1778853996.jpg" alt="All in Ones" />
            </div>
            <div class="shop-category-label">All in Ones</div>
          </a>
          <!-- Card 4 -->
          <a href="https://www.konga.com/search?q=HP+Ink+Toners" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/O/209656_1781270619.jpg" alt="Ink & Toners" />
            </div>
            <div class="shop-category-label">Ink & Toners</div>
          </a>
          <!-- Card 5 -->
          <a href="https://www.konga.com/search?q=HP+Printers" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/O/209656_1781270619.jpg" alt="Printers" />
            </div>
            <div class="shop-category-label">Printers</div>
          </a>
          <!-- Card 6 -->
          <a href="https://www.konga.com/search?q=HP+Components" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/O/209656_1781270619.jpg" alt="HP Components" />
            </div>
            <div class="shop-category-label">HP Components</div>
          </a>
          <!-- Card 7 -->
          <a href="https://www.konga.com/search?q=HP+Desktops" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Z/U/118566_1775817835.png" alt="Desktops" />
            </div>
            <div class="shop-category-label">Desktops</div>
          </a>
          <!-- Card 8 -->
          <a href="https://www.konga.com/search?q=HP+Monitors" class="shop-category-item">
            <div class="shop-category-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/Y/163031_1778853996.jpg" alt="Monitors" />
            </div>
            <div class="shop-category-label">Monitors</div>
          </a>
        </div>
      </div>
    </section>"""
content = content.replace(shop_cat_old, shop_cat_new)

# 4. Must Haves Replacement (was Best Sellers)
must_haves_old = """     <!-- Best Sellers Section -->
    <section class="shop-by-category-section section-reset" style="margin-top: 2rem !important;">
      <div class="shop-by-category-header" style="background-color: #111111; border-radius: 12px 12px 0 0;">
        <div style="display: flex; justify-content: space-between; width: 100%; align-items: center;">
          <span>Best Sellers</span>
          <a href="https://www.konga.com/brand/asus" class="flash-more">
            See more
            <span class="icon-circle" style="background-color: #ffffff;">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 18L15 12L9 6" stroke="#000000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </a>
        </div>
      </div>
      
    </section>


    <div class="shop-category-container">
        <div style="background-color: #ffffff; border-radius: 0 0 24px 24px; padding: 2rem; width: 100%;">
          <div class="product-grid" style="grid-template-columns: repeat(4, 1fr); gap: 2rem; width: 100%;">
            <!-- Best Seller 1 -->
            <article class="product-card">
              <h3>ROG Strix</h3>
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/U/I/118566_1776263615.jpg" alt="ROG Strix G16" />
              <a href="https://www.konga.com/search?q=ASUSROGStrix1" class="product-btn">Buy Now</a>
            </article>
            <!-- Best Seller 2 -->
            <article class="product-card">
              <h3>TUF Gaming</h3>
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/E/S/118566_1776261783.jpg" alt="TUF Gaming A16" />
              <a href="https://www.konga.com/search?q=ASUSTUFGaming1" class="product-btn">Buy Now</a>
            </article>
            <!-- Best Seller 3 -->
            <article class="product-card">
              <h3>Zenbook</h3>
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_1920,c_limit/media/catalog/product/T/H/181128_1781017103.jpg" alt="Zenbook Duo" />
              <a href="https://www.konga.com/search?q=asusZenbook1" class="product-btn">Buy Now</a>
            </article>
            <!-- Best Seller 4 -->
            <article class="product-card">
              <h3>Vivobook</h3>
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_1920,c_limit/media/catalog/product/H/U/118566_1775817869.png" alt="Vivobook 14" />
              <a href="https://www.konga.com/search?q=ASUSVivobook1" class="product-btn">Buy Now</a>
            </article>
          </div>
        </div>
      </div>"""

must_haves_new = """    <!-- Shop These Must Haves Section -->
    <section class="shop-by-category-section section-reset" style="margin-top: 2rem !important;">
      <div class="shop-by-category-header" style="background-color: #111111; border-radius: 12px 12px 0 0;">
        <div style="display: flex; justify-content: space-between; width: 100%; align-items: center;">
          <span>Shop These Must Haves</span>
          <a href="https://www.konga.com/brand/hp" class="flash-more">
            See more
            <span class="icon-circle" style="background-color: #ffffff;">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 18L15 12L9 6" stroke="#000000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </a>
        </div>
      </div>
    </section>

    <div class="shop-category-container">
        <div style="background-color: #ffffff; border-radius: 0 0 24px 24px; padding: 2rem; width: 100%;">
          <div class="product-grid" style="grid-template-columns: repeat(4, 1fr); gap: 2rem; width: 100%;">
            <!-- Must Have 1 -->
            <article class="product-card">
              <h3>HP Workstation</h3>
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_1920,c_limit/media/catalog/product/H/U/118566_1775817869.png" alt="HP Workstation" />
              <a href="https://www.konga.com/search?q=HP+Workstation" class="product-btn">Buy Now</a>
            </article>
            <!-- Must Have 2 -->
            <article class="product-card">
              <h3>Omen Laptops</h3>
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/U/I/118566_1776263615.jpg" alt="Omen Laptops" />
              <a href="https://www.konga.com/search?q=HP+Omen+Laptops" class="product-btn">Buy Now</a>
            </article>
            <!-- Must Have 3 -->
            <article class="product-card">
              <h3>Omen Desk PCs</h3>
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/E/S/118566_1776261783.jpg" alt="Omen Desk PCs" />
              <a href="https://www.konga.com/search?q=HP+Omen+Desktop" class="product-btn">Buy Now</a>
            </article>
            <!-- Must Have 4 -->
            <article class="product-card">
              <h3>Students Laptops</h3>
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_1920,c_limit/media/catalog/product/T/H/181128_1781017103.jpg" alt="Students Laptops" />
              <a href="https://www.konga.com/search?q=HP+Students+Laptops" class="product-btn">Buy Now</a>
            </article>
          </div>
        </div>
      </div>"""
content = content.replace(must_haves_old, must_haves_new)

# 5. Fix remaining "ASUS" mentions in text
# Banner section
content = content.replace('alt="ASUS AI Laptops"', 'alt="HP AI Laptops"')
content = content.replace('alt="ASUS TUF Gaming FA506"', 'alt="HP Victus Gaming"')
content = content.replace('alt="ASUS Vivobook TP3407"', 'alt="HP Pavilion"')
content = content.replace('alt="ASUS Zenbook UX8407"', 'alt="HP Spectre x360"')
content = content.replace('alt="ASUS ROG Ally"', 'alt="HP Omen Transcend"')
content = content.replace('alt="ASUS Zenbook Duo"', 'alt="HP Envy x360"')
content = content.replace('href="https://www.konga.com/search?search=ASUS"', 'href="https://www.konga.com/search?search=HP"')

# SEO Section
content = content.replace('Your Trusted Destination for ASUS Laptops and Electronics in Nigeria', 'Your Trusted Destination for HP Laptops and Electronics in Nigeria')
content = content.replace('ASUS products in Nigeria', 'HP products in Nigeria')
content = content.replace('authentic ASUS computing devices', 'authentic HP computing devices')
content = content.replace('collection of ASUS devices', 'collection of HP devices')
content = content.replace('ASUS Zenbook OLED', 'HP Spectre x360')
content = content.replace('TUF Gaming laptops', 'Victus Gaming laptops')
content = content.replace('ASUS brings reliable hardware', 'HP brings reliable hardware')
content = content.replace("ASUS's latest gaming devices", "HP's latest gaming devices")
content = content.replace('ROG Ally', 'Omen Transcend')
content = content.replace('ROG series offers', 'Omen series offers')
content = content.replace('genuine ASUS products', 'genuine HP products')
content = content.replace('all your ASUS computing needs', 'all your HP computing needs')
content = content.replace('trust ASUS for innovation', 'trust HP for innovation')

with open('index.html', 'w') as f:
    f.write(content)
print("Done")
