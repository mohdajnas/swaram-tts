from bs4 import BeautifulSoup
import re

# Classes
active_classes = "flex items-center gap-3 px-3 py-2.5 bg-surface-container-lowest text-primary font-semibold border-l-4 border-primary transition-all relative group"
inactive_classes = "flex items-center gap-3 px-3 py-2.5 text-secondary hover:bg-surface-container-low transition-all"

def get_soup(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return BeautifulSoup(f.read(), 'html.parser')

def write_soup(file_path, soup):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# Extract sidebar from index.html
home_soup = get_soup('index.html')
home_sidebar = home_soup.find('aside')

def sync_sidebar(target_file, target_href):
    soup = get_soup(target_file)
    sidebar = soup.find('aside')
    if sidebar and home_sidebar:
        # Clone home sidebar
        new_sidebar = BeautifulSoup(str(home_sidebar), 'html.parser').find('aside')
        
        # Reset all links to inactive
        for a in new_sidebar.find_all('a'):
            a['class'] = inactive_classes
            
        # Set the target link to active
        target_a = new_sidebar.find('a', href=target_href)
        if target_a:
            target_a['class'] = active_classes
            
        sidebar.replace_with(new_sidebar)
        write_soup(target_file, soup)
        print(f"Synced sidebar for {target_file}")
    else:
        print(f"Could not find sidebar in {target_file}")

# index.html active is index.html
# studio.html active is studio.html
# library.html active is library.html

sync_sidebar('studio.html', 'studio.html')
sync_sidebar('library.html', 'library.html')

# Also fix index.html just in case (to ensure it has the correct active classes, although it already does)
sync_sidebar('index.html', 'index.html')

