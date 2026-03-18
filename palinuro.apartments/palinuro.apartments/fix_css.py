import sys

file_path = "/Users/edoardolaneve/Desktop/cartella senza nome/palinuro-affitti 4.html"
with open(file_path, "r") as f:
    content = f.read()

target = """    .apt-hero-slides img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;"""
    
replacement = """    .apt-hero-slides img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: contain;"""
    
new_content = content.replace(target, replacement)
with open(file_path, "w") as f:
    f.write(new_content)
print("Replaced CSS")
