import pandas as pd
import numpy as np

# Input
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}

# Load to df
df = pd.DataFrame(raw_data, columns=['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
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

###############################################################################
# Ejemplo de uso de Pandas
###############################################################################

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

print("For getting fast access to a scalar (equiv to the prior method): ")
print(df.at[dates[0], 'A'])

# Selecting by posicion
print("Selecting by posicion: ")
print(df.iloc[3])

print("By integer slices, acting similar to numpy/python: ")
print(df.iloc[3:5, 0:2])

print("By lists of integer position locations, similar to the numpy/python style: ")
print(df.iloc[[1, 2, 4], [0, 2]])

print("For slicing rows explicitly: ")
print(df.iloc[1:3, :])

print("For slicing columns explicitly: ")
print(df.iloc[:, 1:3])

print("For slicing columns explicitly: ")
print(df.iloc[1, 1])

print("For getting fast access to a scalar (equiv to the prior method): ")
print(df.iat[1, 1])

# Bollean Indexing
print("Using a single column’s values to select data.: ")
print(df[df.A > 0])

print("Selecting values from a DataFrame where a boolean condition is met: ")
print(df[df > 0])

# Using the isin() method for filtering
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2[df2['E'].isin(['two', 'four'])])

# Setting a new column automatically aligns the data by the indexes

print("Setting: ")
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print(s1)
df['F'] = s1

# Setting by label
df.at[dates[0], 'A'] = 0

# Setting by position
df.iat[0, 1] = 0

# Setting by assingning with a numpy array
df.loc[:, 'D'] = np.array([5]*len(df))
print(df)

# Operations
# Operations in general exclude missing data

print(df.mean())

print(df.mean(1))

# Applying functions to the data
print(df.apply(np.cumsum))

# Applying lambda
print(df.apply(lambda x: x.max() - x.min()))

# Histogramming
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)

# values count
print(s.value_counts())

# String Methods
 s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
 print(s.str.lower())

###########
# MERGE
###########

# Concat
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
