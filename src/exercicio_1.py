import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Cria um DataFrame a partir do arquivo csv
dataset = pd.read_csv('../data/census.csv')
# Cria um segundo DataFrame contendo apenas as colunas 'education' e 'income'
dataset2 = dataset[["education","income"]]
# Cria um terceiro DataFrame que conterá os dados de dataset2 agrupados por 'education', por 'income'
# totalizando de acordo com o valor da coluna 'education'.
dataset3 = dataset2.groupby(['education', 'income'])['education'].count().reset_index(name="total")
# Cria um quarto DataFrame que conterá apenas a titulação e o total de registros daquela titulação
# independente da renda anual.
dataset4 = dataset2.groupby(['education'])['education'].count()
# Cria uma nova coluna no dataset3: percentage. Essa coluna corresponde ao percentual que aquela faixa de renda
# corresponde no total daquela titulação. Aqui é usada a técnica de list comprehension. Para cada linha de
# dataset3 são lidas as colunas 'education' e 'total' e é calculado o percentual do total daquela titulação
# (que já estará dividido por renda anual) em relação ao total da titulação independente da renda anual (essa
# informação está presente no DataFrame dataset4).
dataset3['percentage'] = [(total / dataset4[degree] * 100) for (degree, total) in zip(dataset3['education'],dataset3['total'])]
# sns.scatterplot(data=dataset3, x="education", y="percentage", hue="income")
sns.barplot(x="education", y="total", hue="income", data=dataset3)
plt.show()