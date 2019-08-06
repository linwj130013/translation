from googletrans import Translator # pip install googletrans
import docx # pip install python-docx 

fin = docx.Document('src.docx')
translator = Translator()
input_str=input('Translate to English (y/n):')
dest_lang=input('Input language code (e.g. zh-TW):') if input_str in ('N','n') else 'en'

for paragraph in fin.paragraphs:
    line=paragraph.text
    if line in ('\n',' ',''):
        continue
    translation = translator.translate(line, dest=dest_lang)
    paragraph.text=paragraph.text+'\n'+translation.text
#     print(translation.origin, ' -> ', translation.text)
    
fin.save('dest.docx')