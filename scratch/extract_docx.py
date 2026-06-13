import zipfile
import xml.etree.ElementTree as ET

def read_docx(file_path):
    with zipfile.ZipFile(file_path) as docx:
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        text = []
        for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            p_text = []
            for run in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                if run.text is not None:
                    p_text.append(run.text)
            text.append("".join(p_text))
        return "\n".join(text)

content = read_docx('/Users/mamoru/techmoney/SMCI_投資判断レポート.docx')
with open('/Users/mamoru/techmoney/scratch/smci_extracted_text.txt', 'w', encoding='utf-8') as f:
    f.write(content)
print("Extracted length:", len(content))
