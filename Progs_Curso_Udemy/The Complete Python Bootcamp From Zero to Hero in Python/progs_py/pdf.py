import PyPDF2

dir = 'c:\\Users\\lucas\\OneDrive - PUCRS - BR\\Arquivos Aula\\CC\\Projetos\\MyPythonStuff\\Progs_Curso_Udemy\\Other Files and Folders\\'

#with open(dir+'Working_Business_Proposal.pdf','rb') as pdf:

pdf = open(dir+'Working_Business_Proposal.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(pdf)

page_one = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfWriter()

pdf_writer.addPage(page_one)
    
    #with open(dir+'Some_New_Document.pdf','wb') as doc:
doc = open(dir+'Some_New_Document.pdf','wb')    
    
pdf_writer.write(doc)

doc.close()

pdf.close()

