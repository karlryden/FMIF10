import pandas as pd 
import numpy as np

years = [year for year in range(1998, 2020)]
months = ['April', 'Maj', 'Juni', 'Juli', 'Augusti', 'September']
regions = ['Norrbotten', 'Västra Götaland', 'Dalarna']

for region in regions:
    series = [pd.Series(years)]
    for month in months:
        target = './data/xlsx/' + region + '/' + month + '.xlsx'
        path = './data/csv/' + region + '.csv'
        excel = pd.read_excel(target, 'Data', usecols=[0, 3, 4], dtype=float).fillna(0)
        print(excel)
        series.append((excel.iloc[:,1] + excel.iloc[:,2]).astype(int))
        print(series)
    data = pd.concat(series, axis=1)
    labels = ['År']
    for m in months:
        labels.append(m)

    data.columns = labels
    print(data.head())
    data.set_index('År', inplace=True)
    print(data.head())
    data.to_csv(path)
