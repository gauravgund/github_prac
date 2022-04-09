import pandas as pd

l = ['a', 'b', 'c']
l1 = [i for i in range(3)]

df = pd.DataFrame({'col1': l, 'col2':l1})

df.head(2)