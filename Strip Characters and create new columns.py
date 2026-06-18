import pandas as pd 

FILE_PATH = r"File Path"
FILTER_COL = 'Add as many filter columns as you want'
FILTER_COL2 = 'This was a column i added'

df = pd.read_csv(FILE_PATH, lineterminator = '\n', encoding = 'utf-8-sig')
df = df.drop(columns=['\r']) # I was woring with a csv, it got rid of an 'empty' column filled with \r
df[FILTER_COL]= df[FILTER_COL].str.strip()
df[FILTER_COL] = df[FILTER_COL].astype(str)
df[FILTER_COL2] = df[FILTER_COL].str[-4:-1] #indexed the characters i wanted from the column already in the data set and created a new column populated with the values
#df[FILTER_COL2] = df[FILTER_COL2].str.strip(')')
df[FILTER_COL] = df[FILTER_COL].str[:-7] # stripped off the characters i no longer wanted in the original column

print(df.head())


df.to_csv(r"File Path", index=False)
