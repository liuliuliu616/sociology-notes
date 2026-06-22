import zipfile
import re
import sys
import os

# Read docx
docx_path = r"C:\Users\张庆智\Desktop\助手整理\社会学概论第2版 [1-200].docx"
with zipfile.ZipFile(docx_path) as z:
    with z.open("word/document.xml") as f:
        xml = f.read().decode("utf-8")

# Extract text
text = re.sub(r'<[^>]+>', ' ', xml)
text = re.sub(r'\s+', ' ', text).strip()

# Find Chapter 1 - first occurrence is TOC, second is body
idx1_first = text.find('第一章社会的基础与条件')
idx1_second = text.find('第一章社会的基础与条件', idx1_first + 1)
idx2 = text.find('第二章个人与社', idx1_second)

ch1 = text[idx1_second:idx2] if idx2 > 0 else text[idx1_second:]

print(f"Chapter 1 body starts at: {idx1_second}, ends at: {idx2}")
print(f"Length: {len(ch1)} chars")

# Save Chapter 1 to file
output_path = r"C:\Users\张庆智\Documents\First-CC\ch1_full.txt"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(ch1)
print(f"Saved to: {output_path}")

# Print section positions
for kw in ['第一节人口', '第二节环境', '第三节物质资料的生产方式', '第四节文化', '第二章']:
    p = ch1.find(kw)
    if p >= 0:
        print(f"  {kw} at position: {p}")
    else:
        print(f"  {kw}: NOT FOUND")
