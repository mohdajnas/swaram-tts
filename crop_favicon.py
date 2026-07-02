import sys
try:
    from PIL import Image
    
    img = Image.open('public/favicon.png')
    width, height = img.size
    print(f"Original size: {width}x{height}")
    
    # Assuming the wave logo is a square on the left side.
    # We crop a square of size height x height from the left.
    # To be safe, maybe there's some padding. We can crop a square from the left edge.
    box = (0, 0, height, height)
    cropped_img = img.crop(box)
    
    cropped_img.save('public/favicon.png')
    print("Cropped successfully to a square.")
except ImportError:
    print("Pillow not installed.")
