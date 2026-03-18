import re

file_path = "/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

imgs = re.findall(r'src="data:image[^>]+;base64,([^"]+)"', text)
for i, b64 in enumerate(imgs):
    print(f"Image location index {i}, len: {len(b64)}, prefix: {b64[:30]}")

