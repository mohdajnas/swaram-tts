import re
import base64
from bs4 import BeautifulSoup

def extract_base64_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'data:image/png;base64,([A-Za-z0-9+/=]+)', content)
    if match:
        return match.group(1)
    return None

b64_data = extract_base64_from_html('index.html')
if b64_data:
    with open('public/favicon.png', 'wb') as f:
        f.write(base64.b64decode(b64_data))
    print("Saved to public/favicon.png")
else:
    # If no public directory, save to root
    print("Could not extract base64 data")

def add_favicon_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    head = soup.find('head')
    if head:
        # Check if favicon already exists
        if not head.find('link', rel='icon'):
            link = soup.new_tag('link', rel='icon', type='image/png', href='/favicon.png')
            head.append(link)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Added favicon to {file_path}")

add_favicon_to_html('index.html')
add_favicon_to_html('studio.html')
add_favicon_to_html('library.html')
