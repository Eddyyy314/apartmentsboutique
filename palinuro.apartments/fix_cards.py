import re

file_path = "/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# I want to find the base64 of length 207636 (which was originally Floyd's card / Green bathroom)
# and set it to Eddy's card.
# I want to find the base64 of length 230960 (which was originally Eddy's card / White bed)
# and set it to Floyd's card.

green_b64 = None
white_b64 = None

imgs = re.findall(r'src="data:image[^>]+;base64,([^"]+)"', text)
for b64 in imgs:
    if len(b64) == 207636 and not green_b64:
        green_b64 = b64
    if len(b64) == 230960 and not white_b64:
        white_b64 = b64

if not green_b64 or not white_b64:
    print("Could not find base64s!")
    exit(1)

eddy_card_start = text.find("onclick=\"goApt('eddy')\"")
eddy_card_end = text.find('class="card-name">Eddy&sofy</div>', eddy_card_start)
eddy_card_html = text[eddy_card_start:eddy_card_end]

floyd_card_start = text.find("onclick=\"goApt('floyd')\"")
floyd_card_end = text.find('class="card-name">Floyd</div>', floyd_card_start)
floyd_card_html = text[floyd_card_start:floyd_card_end]

eddy_match = re.search(r'src="data:image[^>]+;base64,([^"]+)"', eddy_card_html)
floyd_match = re.search(r'src="data:image[^>]+;base64,([^"]+)"', floyd_card_html)

if eddy_match and floyd_match:
    old_eddy = eddy_match.group(1)
    old_floyd = floyd_match.group(1)
    
    new_eddy_card_html = eddy_card_html.replace(old_eddy, green_b64)
    new_floyd_card_html = floyd_card_html.replace(old_floyd, white_b64)
    
    text = text[:eddy_card_start] + new_eddy_card_html + text[eddy_card_end:floyd_card_start] + new_floyd_card_html + text[floyd_card_end:]
    print("Replaced both cards.")
else:
    print("Matches failed.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

