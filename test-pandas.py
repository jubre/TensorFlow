import pandas as pd
import numpy as np

# Input
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}

# Load to df
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
print(df)

# Save in csv
df.to_csv('test-pandas.csv')

# Read from csv
tp = pd.read_csv('test-pandas.csv')
print(tp)

# Read csv specifying column names, and first row is header
tp = pd.read_csv('test-pandas.csv', names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'], header=0)
print(tp)

# Read an specific column
print(tp.pop('Post-Test Score'))

# Read nombre of Keys = Headers
for key in tp.keys():
    print(key)

# Read first 3 rows
print(df.head(3))

# Read last 3 rows
print(df.tail(3))

# Read the first name column
print(df.first_name)
print(df['first_name'])

# Read the second column
print(df['last_name'])

# Creando Series
s = pd.Series([1, 2, 4, 5, 7, 8, 10])
print(s)

# Creando un Data DataFrame
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

print("Data Frame Index: ")
print(df.index)

print("Data Frame Columns: ")
print(df.columns)

print("Data Frame Values: ")
print(df.values)

print("Data Frame Describe: ")
print(df.describe())
