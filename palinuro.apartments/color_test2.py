import re
import base64
from io import BytesIO
from PIL import Image

with open('/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html', 'r', encoding='utf-8') as f:
    text = f.read()

floyd_card = text[1880:1920]
# just find the card image
match = re.search(r'id="pg-floyd".*?<img.*?src="data:image/[^;]+;base64,([^"]+)"', text, re.DOTALL)
if match:
    pass # this would find the first image in pg-floyd, which is the slider image 1.

# Let's find the card image:
#       <div class="card" onclick="goApt('floyd')">
#         <div class="card-img">
#           <img
#             src="data:image/jpeg;base64,/9j...
card_start = text.find("onclick=\"goApt('floyd')\"")
card_end = text.find('class="card-name">Floyd</div>', card_start)
card_html = text[card_start:card_end]
match = re.search(r'img\s+src="data:image/[^;]+;base64,([^"]+)"', card_html)
if match:
    b64 = match.group(1)
    img_data = base64.b64decode(b64)
    img = Image.open(BytesIO(img_data)).convert('RGB')
    img = img.resize((50, 50))
    pixels = list(img.getdata())
    print(f"Card: R={sum(p[0] for p in pixels) / len(pixels):.1f}, G={sum(p[1] for p in pixels) / len(pixels):.1f}")

