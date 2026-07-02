import re
import sys

def replace_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace href="#" with href="index.html" for Home
    content = re.sub(r'href="#"([\s\S]*?>home<)', r'href="index.html"\1', content)
    content = re.sub(r'href="#"([\s\S]*?>mic<)', r'href="studio.html"\1', content)
    content = re.sub(r'href="#"([\s\S]*?>library_music<)', r'href="library.html"\1', content)
    
    # Also in case there are links by text content:
    # We can match href="#" followed by something and then >Home<
    content = re.sub(r'href="#"([\s\S]*?>Home<)', r'href="index.html"\1', content)
    content = re.sub(r'href="#"([\s\S]*?>Studio<)', r'href="studio.html"\1', content)
    content = re.sub(r'href="#"([\s\S]*?>Library<)', r'href="library.html"\1', content)
    content = re.sub(r'href="#"([\s\S]*?>Voices Library<)', r'href="library.html"\1', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file in ['index.html', 'studio.html', 'library.html']:
    replace_links(file)

