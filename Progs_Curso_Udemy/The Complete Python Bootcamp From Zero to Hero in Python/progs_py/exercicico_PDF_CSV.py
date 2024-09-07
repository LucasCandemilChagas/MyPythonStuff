import csv

import PyPDF2

import re

dir = 'c:\\Users\\lucas\\OneDrive - PUCRS - BR\\Arquivos Aula\\CC\\Projetos\\MyPythonStuff\\Progs_Curso_Udemy\\'

csv_data = open(dir+'find_the_link.csv')

csv_reader = csv.reader(csv_data)

link = ''

for i,line in enumerate(list(csv_reader)):
    link+=line[i]
print(link)

with open(dir+'Find_the_Phone_Number.pdf','rb') as pdf:

    pdf_reader = PyPDF2.PdfFileReader(pdf)
    
    for numPage in range(pdf_reader.numPages):
        page = pdf_reader.getPage(numPage)
        text = page.extract_text()
        phone_number = re.search(r'\d{3}.\d{3}.\d{4}',text)
        if phone_number:
            print(phone_number.group())
            break
    