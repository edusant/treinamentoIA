import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

dadoscredit = pd.read_csv('credit_data.csv')

#sns.countplot(x = dadoscredit['default'])

#plt.show()

#plt.hist(x = dadoscredit['age']);
#plt.show()

#plt.hist(x = dadoscredit['income']);

#plt.show()

#plt.hist(x = dadoscredit['loan']);

#plt.show()

grafico = px.scatter_matrix(dadoscredit, dimensions=['age', 'income', 'loan'], color = 'default')
grafico.show()
#plt.show()