import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel('Dados_covid_19_estado.xlsx')
casos = planilha['Casos por dia']

plt.title("Casos por covid")

plt.ylabel("Datas")
plt.xlabel("Casos por dia")

plt.plot(planilha['Total de casos'])

plt.grid()

plt.show()