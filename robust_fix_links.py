from bs4 import BeautifulSoup
import os

files = {
    'index.html': '/tmp/swaram_dashboard.html',
    'studio.html': '/tmp/swaram_studio.html',
    'library.html': '/tmp/swaram_library.html'
}

for dest, src in files.items():
    with open(src, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Find all <a> tags and check their inner text
    for a in soup.find_all('a'):
        text = a.get_text(strip=True).lower()
        if 'home' in text:
            a['href'] = 'index.html'
        elif 'voices library' in text:
            a['href'] = 'library.html'
        # Let's map "Studio Beta" or "Text to Speech" to studio.html
        # If there is no specific "Studio" link, maybe "Text to Speech" is the studio?
        # The design has a "Studio Beta" screen. Let's see if there is a link for it.
        # From earlier grep, the "Home Dashboard" had "Text to Speech".
        elif 'text to speech' in text:
            a['href'] = 'studio.html'
            
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(str(soup))
