import pandas as pd
from IPython.display import display
data = {'Branche':['Alpha', 'Beta', 'Gamma', 'Delta'],
        'Number of students':[350, 410, 650, 240],
        'Сlasses of study':['1-4', '5-9', '5-11', '10-11'],
        'Activity rating':[2, 1, 3, 4]
}
df = pd.DataFrame(data)
print('Первые три строки')
display(df.head(3))
print('Последние три строки')
display(df.tail(3))
df.to_csv('output.csv', sep=',', encoding='utf-8')
