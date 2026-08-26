import re

with open("index.html", "r") as f:
    html = f.read()

# Replace Featured Banners
featured_banners_old = """    <!-- Featured Banners Section -->
    <section class="shop-by-category-section section-reset" style="margin-top: 2rem !important;">
      <div class="shop-category-container">
        <div style="background-color: #ffffff; border-radius: 0 0 24px 24px; padding: 2rem; width: 100%;">
          <div class="banner-grid" style="grid-template-columns: 1fr 1fr; gap: 1.5rem; width: 100%;">
            <!-- Banner 1 -->
            <a href="https://www.konga.com/search?q=ASUSROGStrix1" class="banner-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/v1782830154/landingPages/2026%20Marketing/AsusSIS/copilot-left.webp" alt="HP Omen Transcend" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
            </a>
            <!-- Banner 2 -->
            <a href="https://www.konga.com/search?q=asusZenbook1" class="banner-card">
              <img src="https://www-konga-com-res.cloudinary.com/image/upload/v1782830154/landingPages/2026%20Marketing/AsusSIS/copilot-right.webp" alt="HP Envy x360" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
            </a>
          </div>
        </div>
      </div>
    </section>"""

featured_banners_new = """    <!-- Featured Banners Section -->
    <section class="shop-by-category-section section-reset" style="margin-top: 2rem !important;">
      <div class="shop-category-container">
        <div style="background-color: #ffffff; border-radius: 0 0 24px 24px; padding: 2rem; width: 100%;">
          <div class="banner-grid" style="grid-template-columns: 1fr 1fr; gap: 1.5rem; width: 100%;">
            <!-- Banner 1 -->
            <a href="#" class="banner-card">
              <img src="https://placehold.co/700x350/024AD8/FFF?text=700+x+350" alt="Placeholder 700x350" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
            </a>
            <!-- Banner 2 -->
            <a href="#" class="banner-card">
              <img src="https://placehold.co/700x350/024AD8/FFF?text=700+x+350" alt="Placeholder 700x350" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
            </a>
          </div>
        </div>
      </div>
    </section>"""

html = html.replace(featured_banners_old, featured_banners_new)

# Fonts
# Update Content Pages font size to 16px (1rem) for headings and 14px (0.875rem) for content.
# Headings: .shop-by-category-header, .product-card h3, .nav-items a, .seo-container > h2, .shop-category-label
# Content: p, spans, .seo-content p, .product-btn, .cta-button
# Instead of doing it blindly, I will manually add global rules or update the specific classes
# Let's add a global typography reset at the top, or update the existing css font-sizes

css_updates = {
    'font-size: 1.5rem;': 'font-size: 1rem;',
    'font-size: 2rem;': 'font-size: 1rem;',
    'font-size: 1.2rem;': 'font-size: 1rem;',
    'font-size: 1.325rem;': 'font-size: 1rem;',
    'font-size: 1.15rem;': 'font-size: 1rem;',
    'font-size: 1.8rem;': 'font-size: 1rem;',
    'font-size: 1.4rem;': 'font-size: 1rem;',
    'font-size: 0.95rem;': 'font-size: 0.875rem;',
    'font-size: 0.9rem;': 'font-size: 0.875rem;',
    'font-size: 0.85rem;': 'font-size: 0.875rem;'
}

for k, v in css_updates.items():
    html = html.replace(k, v)

with open("index.html", "w") as f:
    f.write(html)
