import zipfile, xml.etree.ElementTree as ET

for idx, f in enumerate([
    r"D:\SpaceBook\Books\12th\12th Computer Science\Word\001_page_1_and_330_more_part_01_of_03.docx",
    r"D:\SpaceBook\Books\12th\12th Computer Science\Word\001_page_1_and_330_more_part_02_of_03.docx",
    r"D:\SpaceBook\Books\12th\12th Computer Science\Word\001_page_1_and_330_more_part_03_of_03.docx"
]):
    with zipfile.ZipFile(f) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        p_list = []
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            t = ''.join([node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]).strip()
            if t: p_list.append(t)
        print(f"Part {idx+1}: {len(p_list)} paras. Start: '{p_list[0][:50]}', End: '{p_list[-1][:50]}'")
