import pandas as pd

df = pd.read_csv('data.csv')

print(f'Средняя зарплата сотрудников: {df.salary.mean()}')
print()
print('Сотрудники старше 30 лет:')
print(df[df.age > 30])