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

# Read Keys = Headers
for key in tp.keys():
    print(key)
