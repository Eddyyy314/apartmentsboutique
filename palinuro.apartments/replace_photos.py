import re
import base64

with open('/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html', 'r', encoding='utf-8') as f:
    text = f.read()

floyd_start = text.find('id="sl-floyd"')
if floyd_start == -1:
    print("Floyd slider not found")
    exit()

# find end of the slider div
floyd_end = text.find('</div', floyd_start + 1000)
while '</div' in text[floyd_end:floyd_end+20]:
    floyd_end = text.find('</div', floyd_end+10)

floyd_section = text[floyd_start:floyd_end]

# Extract all img tags
img_tags = re.findall(r'<img[^>]+src="data:image/[^;]+;base64,([^"]+)"', floyd_section)

print(f"Found {len(img_tags)} images in original floyd slider.")

if len(img_tags) >= 4:
    target_b64 = img_tags[3] # Orange bathroom
    green2_b64 = img_tags[1]
    green3_b64 = img_tags[2]

    # Remove the green bathrooms from the slider
    for match in re.finditer(r'(<img[^>]+src="data:image/[^;]+;base64,[^"]+"[^>]*>)', floyd_section):
        tag = match.group(1)
        if green2_b64 in tag or green3_b64 in tag:
            floyd_section = floyd_section.replace(tag, '') 

    # Reconstruct text
    new_text = text[:floyd_start] + floyd_section + text[floyd_end:]

    # Now replace the card image
    card_start = new_text.find("onclick=\"goApt('floyd')\"")
    if card_start != -1:
        card_end = new_text.find('class="card-name">Floyd</div>', card_start)
        card_html = new_text[card_start:card_end]
        match = re.search(r'src="data:image/[^;]+;base64,([^"]+)"', card_html)
        if match:
            old_card_b64 = match.group(1)
            # Use string replace for the whole doc just in case it's used elsewhere, but safe
            # Actually, just replace in card_html then replace in new_text
            new_card_html = card_html.replace(old_card_b64, target_b64)
            new_text = new_text[:card_start] + new_card_html + new_text[card_end:]
            print("Card image replaced.")
        else:
            print("Card image base64 not found.")

    with open('/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html', 'w', encoding='utf-8') as f:
        f.write(new_text)

    print("Replacement completed.")
else:
    print("Not enough images found in floyd slider.")

