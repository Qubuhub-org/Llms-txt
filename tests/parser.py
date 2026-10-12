from pathlib import Path
from parser import parse_llms_txt

text = Path("llms-ctx-full.md").read_text()
data = parse_llms_txt(text)

print(data["title"])
print(data["summary"])
print(data["sections"].keys())
