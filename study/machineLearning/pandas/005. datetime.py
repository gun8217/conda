import pandas as pd

date = pd.to_datetime('2/2/2020', format='%m/%d/%Y').strftime('%m월 %d일 %Y년')
print(date)