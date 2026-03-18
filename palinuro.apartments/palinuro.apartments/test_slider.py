import re

file_path = "/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

eddy_slider = text[text.find('id="sl-eddy"'):text.find('id="sl-floyd"')]
floyd_slider = text[text.find('id="sl-floyd"'):]

eddy_imgs = re.findall(r'src="data:image[^>]+;base64,([^"]+)"', eddy_slider)
floyd_imgs = re.findall(r'src="data:image[^>]+;base64,([^"]+)"', floyd_slider)

for i, b64 in enumerate(eddy_imgs):
    print(f"Eddy slider {i}: len {len(b64)}")

for i, b64 in enumerate(floyd_imgs):
    print(f"Floyd slider {i}: len {len(b64)}")

