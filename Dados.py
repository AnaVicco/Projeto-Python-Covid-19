import os 
from fpdf import FPDF 
  
pdf = FPDF() 

pdf.add_page() 

pdf.set_font("Arial", size = 15) 

pdf.cell(200, 10, txt = "Foi analizado uma tabela com os numeros de casos por dia ",  
         ln = 1, align = 'A')

pdf.cell(200, 10, txt = "e o total de casos por coronavirus desde o dia 28 de Feveireiro de 2020 ",  
         ln = 2, align = 'A')

pdf.cell(200, 10, txt = "até o dia 31 de Janeiro de 2022, pode-se concluir que o número",  
         ln = 3, align = 'A')

pdf.cell(200, 10, txt = " de casos por dias teve grandes variações porém o  ",  
         ln = 4, align = 'A')

pdf.cell(200, 10, txt = "total de casos desde o começo da pandemia é alarmante",  
         ln = 5, align = 'A')

pdf.cell(200, 10, txt = "visto que já tivemos mais de 4 mil casos confirmados de coronavirus",  
         ln = 5, align = 'A')
pdf.output("Dados.pdf")  

os.system("pause")