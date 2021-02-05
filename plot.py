import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = ['April', 'Maj', 'Juni', 'Juli', 'Augusti', 'September']
regions = ['Norrbotten', 'Västra Götaland', 'Dalarna']

data = pd.read_csv('./data/csv/Norrbotten.csv', index_col=0)

# print(data)

T = [t for t in range(22*6)]
D = []

for i in range(22):
    D.append(data.iloc[i].to_numpy())

D = np.concatenate(D)
print(D)

plt.plot(T, D)
plt.show()

# for i in range(22):
#     plt.plot(data.iloc[i])
#     plt.pause(0.1)
# plt.show()