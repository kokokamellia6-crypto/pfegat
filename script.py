import base64

with open("logo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("utf-8")

logo_uri = f"data:image/png;base64,{logo_b64}"

with open("logo_uri.txt", "w", encoding="utf-8") as f:
    f.write(logo_uri)

print("Done")