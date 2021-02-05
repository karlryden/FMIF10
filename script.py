import pandas as pd 

months = ['April', 'Maj', 'Juni', 'Juli', 'Augusti', 'September']
regions = ['Norrbotten', 'Västra Götaland', 'Dalarna']

for region in regions:
    for month in months:
        target = './data/xlsx/' + region + '/' + month + '.xlsx'
        path = './data/csv/' + region + '/' + 'test' + '.csv'
        excel = pd.read_excel(target, 'Data', dtype=str).fillna(0)
        print(excel.iloc[3])
        # s = excel.iloc[3] + excel.iloc[4]
        # print(s)
        break
        # data.to_csv(path, encoding='utf-8', index=False)
        
    break
