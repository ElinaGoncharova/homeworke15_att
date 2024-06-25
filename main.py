import pandas as pd
import random

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one hot encoded DataFrame
one_hot = pd.DataFrame()

# Заполнение one hot encoded DataFrame
for category in data['whoAmI'].unique():
    one_hot[category] = data['whoAmI'].apply(lambda x: 1 if x == category else 0)

# Вывод результата
print(one_hot.head())
