import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace inline header backgrounds
content = content.replace('background-color: #111111;', 'background-color: #024AD8;')

# Replace product button colors
content = content.replace('background-color: #000;\n        color: white;\n        border: none;\n        padding: 0.75rem 2.5rem;\n        border-radius: 50px;', 'background-color: #024AD8;\n        color: white;\n        border: none;\n        padding: 0.75rem 2.5rem;\n        border-radius: 50px;')
content = content.replace('.product-btn:hover {\n        background-color: #1a1a1a;', '.product-btn:hover {\n        background-color: #013399;')

# Replace CTA button
content = content.replace('background-color: #000;\n        color: #fff;', 'background-color: #024AD8;\n        color: #fff;')
content = content.replace('.cta-button:hover {\n        background-color: #333;', '.cta-button:hover {\n        background-color: #013399;')

# Replace pagination dot
content = content.replace('#slide6:checked ~ .pagination label[for="slide6"] {\n        background-color: #000;\n      }', '#slide6:checked ~ .pagination label[for="slide6"] {\n        background-color: #024AD8;\n      }')

# Replace the previous blue #00539b with #024AD8
content = content.replace('#00539b', '#024AD8')

with open('index.html', 'w') as f:
    f.write(content)

print("Colors updated")
