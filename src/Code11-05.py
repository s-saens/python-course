import pandas as pd

# 프로젝트 폴더에 있는 CSV 폴더의 singer2.csv 파일을 상대경로로 불러오려면?
filename = './CSV/singer2.csv'
df = pd.read_csv(filename, index_col=None, encoding='CP949')

df_sort1 = df.sort_values(by=['평균 키'], axis=0)
print(df_sort1)