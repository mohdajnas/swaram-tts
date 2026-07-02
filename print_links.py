from bs4 import BeautifulSoup
import sys

for file in ['index.html', 'studio.html', 'library.html']:
    print(f"--- {file} ---")
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        links = soup.find_all('a')
        for a in links:
            text = a.get_text(strip=True).replace('keyboard_arrow_down', '').strip()
            # Only print links that seem to be navigation (short text)
            if len(text) > 0 and len(text) < 30:
                print(f"{text}: {a.get('href')}")
