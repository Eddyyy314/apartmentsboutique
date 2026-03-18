import re
import base64
from io import BytesIO
import logging
from PIL import Image

def find_green_img():
    with open('/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html', 'r', encoding='utf-8') as f:
        text = f.read()

    start = text.find('id="sl-floyd"')
    floyd_section = text[start:start+1000000]

    imgs = []
    # find exactly all img srcs
    for match in re.finditer(r'<img\s+src="data:image/[^;]+;base64,([^"]+)"', floyd_section):
        imgs.append(match.group(1))

    for i, b64 in enumerate(imgs):
        try:
            img_data = base64.b64decode(b64)
            img = Image.open(BytesIO(img_data)).convert('RGB')
            img = img.resize((50, 50))
            pixels = list(img.getdata())
            r = sum(p[0] for p in pixels) / len(pixels)
            g = sum(p[1] for p in pixels) / len(pixels)
            b = sum(p[2] for p in pixels) / len(pixels)
            print(f"Image {i+1}: R={r:.1f}, G={g:.1f}, B={b:.1f}")
            # If green is significantly dominant, output it
        except Exception as e:
            print(f"Error {i+1}: {e}")

find_green_img()
