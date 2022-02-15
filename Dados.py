import os 
from fpdf import FPDF 
  
pdf = FPDF() 

pdf.add_page() 

pdf.set_font("Arial", size = 15) 

pdf.cell(200, 10, txt = "Para a realização do grafico analizei os dados do site",  
         ln = 1, align = 'A')

pdf.cell(200, 10, txt = "https://www.seade.gov.br/coronavirus/ em seguida fiz ",  
         ln = 2, align = 'A')

pdf.cell(200, 10, txt = "uma planilha com as informações extraidas, separadas por ",  
         ln = 3, align = 'A')

pdf.cell(200, 10, txt = "tres colunas: data, total de casos e casos por dia  ",  
         ln = 4, align = 'A')
         
pdf.cell(200, 10, txt = "desde o dia 28 de Feveireiro de 2020 até o dia 31 de Janeiro de 2022",  
         ln = 2, align = 'A')

pdf.cell(200, 10, txt = "com isso, contrui um grafico em linha de forma organizada,  ",  
         ln = 5, align = 'A')

pdf.cell(200, 10, txt = "para que pudesse ser visto de forma clara as informações. ",  
         ln = 6, align = 'A')

pdf.cell(200, 10, txt = "pode-se concluir que o número de casos por dias teve grandes",  
         ln = 7, align = 'A')

pdf.cell(200, 10, txt = "variações porém o total de casos desde o começo da pandemia é alarmante",  
         ln = 8, align = 'A')

pdf.cell(200, 10, txt = " visto que já tivemos mais de 4 mil casos confirmados de coronavirus",  
         ln = 9, align = 'A')

pdf.output("Dados.pdf")  

os.system("pause")