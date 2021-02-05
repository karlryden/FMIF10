import pandas as pd
import matplotlib.pyplot as plt

months = ['April', 'Maj', 'Juni', 'Juli', 'Augusti', 'September']
regions = ['Norrbotten', 'Västra Götaland', 'Dalarna']

data = pd.read_csv('./data/csv/Norrbotten/Juli.csv')

T = data['År▼'].to_numpy()
B = data['Areal\nProduktiv skogsmark (m²)'] + data['  \nAnnan trädbevuxen mark (m²)'].to_numpy()

print(data.head())
print(data.columns)

plt.plot(T, B)
plt.show()