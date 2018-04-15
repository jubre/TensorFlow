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

print("Transporting your data: ")
print(df.T)

print("Sorting by an axis: ")
print(df.sort_index(axis=1, ascending=False))

print("Sorting by values: ")
print(df.sort_values(by='B'))

print("Selecting a single column, which yields a Series, equivalent to df.A: ")
print(df['A'])

print("Selecting via [], which slices the rows: ")
print(df[0:3])

print("For getting a cross section using a label: ")
print(df.loc[dates[0]])

print("Selecting on a multi-axis by label: ")
print(df.loc[:, ['A', 'B']])

print("Showing label slicing, both endpoints are included: ")
print(df.loc['20130102':'20130104', ['A', 'B']])

print("Reduction in the dimensions of the returned object: ")
print(df.loc['20130102', ['A', 'B']])

print("For getting a scalar value: ")
print(df.loc[dates[0], 'A'])
