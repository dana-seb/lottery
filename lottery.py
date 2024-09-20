import pandas as pd

print('\n')

df_day = pd.read_excel('day_night_lottery.xlsx', sheet_name = 2)
# print(df_day)

df_night = pd.read_excel('day_night_lottery.xlsx', sheet_name = 3)
# print(df_night)

# print(df_night.describe())
first = df_night['first'].value_counts()
second = df_night['second'].value_counts()
fourth = df_night['fourth'].value_counts()
third = df_night['third'].value_counts()

print(first)
print(second)
print(fourth)
print(third)

# df_night_I = df_night['Result'].str.replace('',"")
# print(df_night_I)








print('\n')





