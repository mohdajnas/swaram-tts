from bs4 import BeautifulSoup
import re

files = ['index.html', 'studio.html', 'library.html']

script_js = """
<script>
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('mobile-overlay');

    function toggleMenu() {
        sidebar.classList.toggle('-translate-x-full');
        if(overlay.classList.contains('hidden')) {
            overlay.classList.remove('hidden');
            // Small delay to allow CSS transition on opacity
            setTimeout(() => overlay.classList.remove('opacity-0'), 10);
        } else {
            overlay.classList.add('opacity-0');
            setTimeout(() => overlay.classList.add('hidden'), 300);
        }
    }

    mobileMenuBtn?.addEventListener('click', toggleMenu);
    overlay?.addEventListener('click', toggleMenu);
</script>
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # 1. Update aside
    aside = soup.find('aside')
    if aside:
        aside['id'] = 'sidebar'
        # ensure classes are added
        classes = aside.get('class', [])
        # We need to add: transition-transform duration-300 -translate-x-full md:translate-x-0
        new_classes = ['transition-transform', 'duration-300', '-translate-x-full', 'md:translate-x-0']
        for nc in new_classes:
            if nc not in classes:
                classes.append(nc)
        aside['class'] = classes
        
    # 2. Update main
    main = soup.find('main')
    if main:
        classes = main.get('class', [])
        if 'ml-[260px]' in classes:
            classes.remove('ml-[260px]')
            classes.insert(0, 'md:ml-[260px]')
        main['class'] = classes
        
    # 3. Insert overlay right after <body>
    body = soup.find('body')
    if body and not soup.find(id='mobile-overlay'):
        overlay = soup.new_tag('div', id='mobile-overlay')
        overlay['class'] = ['fixed', 'inset-0', 'bg-black/50', 'z-40', 'hidden', 'md:hidden', 'transition-opacity', 'opacity-0', 'duration-300']
        body.insert(0, overlay)
        
    # 4. Header update
    header = soup.find('header')
    if header:
        classes = header.get('class', [])
        if 'justify-end' in classes:
            classes.remove('justify-end')
            classes.append('justify-between')
        header['class'] = classes
        
        # Add hamburger button inside header as first child if it doesn't exist
        if not soup.find(id='mobile-menu-btn'):
            btn = BeautifulSoup('<button id="mobile-menu-btn" class="md:hidden p-2 -ml-2 text-secondary hover:bg-surface-container-low rounded-full z-50 flex items-center justify-center"><span class="material-symbols-outlined">menu</span></button>', 'html.parser')
            header.insert(0, btn)
            
    # 5. Inject script at the end of body
    if not soup.find(text=re.compile('toggleMenu')):
        script_tag = BeautifulSoup(script_js, 'html.parser')
        body.append(script_tag)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Updated {file}")

