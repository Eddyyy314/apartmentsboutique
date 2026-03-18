import re
import sys

file_path = "/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update the modal summary in JS
target_modal = """      document.getElementById('modal-summary').innerHTML =
        '<strong>Appartamento:</strong> ' + (apt === 'eddy' ? 'Eddy&sofy' : 'Floyd') + '<br>' +
        '<strong>Check-in:</strong> ' + fmt(s.ci) + ' ' + s.ci.getFullYear() + '<br>' +
        '<strong>Check-out:</strong> ' + fmt(s.co) + ' ' + s.co.getFullYear() + '<br>' +
        '<strong>Ospiti:</strong> ' + s.guests + '<br>' +
        '<strong>Totale stimato:</strong> €' + total + ' per ' + nights + ' notti';"""

replace_modal = """      document.getElementById('modal-summary').innerHTML =
        '<strong>Appartamento:</strong> ' + (apt === 'eddy' ? 'Eddy&sofy' : 'Floyd') + '<br>' +
        '<strong>Check-in:</strong> ' + fmt(s.ci) + ' ' + s.ci.getFullYear() + '<br>' +
        '<strong>Check-out:</strong> ' + fmt(s.co) + ' ' + s.co.getFullYear() + '<br>' +
        '<strong>Ospiti:</strong> ' + s.guests + '<br>' +
        '<strong>Notti:</strong> ' + nights;"""

if target_modal in text:
    text = text.replace(target_modal, replace_modal)
    print("Modal updated.")
else:
    print("WARNING: Modal text not found!")

# 2. Swap the card images
eddy_card_start = text.find("onclick=\"goApt('eddy')\"")
eddy_card_end = text.find('class="card-name">Eddy&sofy</div>', eddy_card_start)
eddy_card_html = text[eddy_card_start:eddy_card_end]

floyd_card_start = text.find("onclick=\"goApt('floyd')\"")
floyd_card_end = text.find('class="card-name">Floyd</div>', floyd_card_start)
floyd_card_html = text[floyd_card_start:floyd_card_end]

eddy_b64_match = re.search(r'src="data:image[^>]+;base64,([^"]+)"', eddy_card_html)
floyd_b64_match = re.search(r'src="data:image[^>]+;base64,([^"]+)"', floyd_card_html)

if eddy_b64_match and floyd_b64_match:
    eddy_b64 = eddy_b64_match.group(1)
    floyd_b64 = floyd_b64_match.group(1)

    print(f"Eddy b64 len: {len(eddy_b64)}, Floyd b64 len: {len(floyd_b64)}")

    # Since the string replace might be tricky with massive base64s if they appear multiple times,
    # let's just replace them exactly in their respective html blocks.
    new_eddy_card_html = eddy_card_html.replace(eddy_b64, floyd_b64)
    new_floyd_card_html = floyd_card_html.replace(floyd_b64, eddy_b64)

    text = text[:eddy_card_start] + new_eddy_card_html + text[eddy_card_end:floyd_card_start] + new_floyd_card_html + text[floyd_card_end:]
    print("Cards swapped.")
else:
    print("Cards base64 not found!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Done python script")
