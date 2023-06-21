import json
from html import unescape

data = json.load(open("api.json", encoding="UTF-8"))
footnote = open("footnote.md", "w")
summary = open("summary.md", "w")
for entry in data:
    if entry["version"] != "1.16.1":
        continue
    address = int(entry["address"])  # hex
    epd = int(entry["pid"])  # dec
    byte_offset = int(entry["byte"])  # 0~3
    size = int(entry["size"])  # dec
    length = int(entry["length"])  # dec
    scr = unescape(entry["scr"].strip())
    description = unescape(entry["description"].strip())
    name = unescape(entry["name"].strip())
    filename = name.replace(" ", "")
    filename = filename.replace('"', "")
    filename = filename.replace("/", "")
    filename = filename.replace("?", "")
    filename = filename + ".md"

    footnote.write(f"[{address:08X}]: offsets/{filename}\n")
    summary.write(f"    - [{name}](offsets/{filename})\n")
    with open(filename, "w") as f:
        f.write(
            f"""
#  {name}
Address   | {address:X}
----------|-------------
Player ID | {epd} (Byte Offset: {byte_offset})
Size 	  | {size}
Length 	  | {length}
SC:R      | {scr}

{description}
"""
        )
