# python3 manage.py shell < dumpdata.py
from map.models import News
import numpy as np
import pandas as pd

# print(News.objects.all())
categories = pd.read_csv('categories.csv')
crawler_output = pd.read_csv(
    './classifier/data/crawler-output.csv', sep='|')
predictions = pd.read_csv(
    './classifier/predicted_results_1572945538/predictions_all.csv', sep='|')
predictions.rename(
    columns = {'NEW_PREDICTED': 'category'}, inplace = True)

df = pd.merge(predictions, categories, on='category', how='left')
df = pd.merge(df, crawler_output, on='Descript')
print(df)

for ind in df.index:
    _, created = News.objects.get_or_create(
        title=df['Descript'][ind],
        category=df['category'][ind],
        severity=df['severity'][ind],
        state=df['State'][ind],
        statecode=df['StateCode'][ind],
        city=df['City'][ind]
    )
    print(created)
