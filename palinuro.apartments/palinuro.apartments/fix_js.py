import sys

file_path = "/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = "const hs = { eddy: { i: 0, n: 8 }, floyd: { i: 0, n: 8 } };"
replacement = "const hs = { eddy: { i: 0, n: 8 }, floyd: { i: 0, n: 6 } };"
    
new_content = content.replace(target, replacement)
with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Replaced JS limit")
