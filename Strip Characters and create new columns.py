import pandas as pd 

FILE_PATH = r"File Path"
FILTER_COL = 'Add all the cols you need'
FILTER_COL2 = 'A column i created'

df = pd.read_csv(FILE_PATH, lineterminator = '\n', encoding = 'utf-8-sig')
df = df.drop(columns=['\r']) # gets rid of any columns that are empty and start with \r, useful if importing csv's
df[FILTER_COL]= df[FILTER_COL].str.strip()
df[FILTER_COL] = df[FILTER_COL].astype(str)
df[FILTER_COL2] = df[FILTER_COL].str[-4:] # creates a new column based of the old one
df[FILTER_COL2] = df[FILTER_COL2].str.strip(')')
df[FILTER_COL] = df[FILTER_COL].str[:-7]

print(df.head())


df.to_csv(r"File Path ")
