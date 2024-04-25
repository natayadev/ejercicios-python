import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charly', 'David', 'Anne', 'Ruth'],
        'age': ['25', '35', '40', '30', '70', '65']}

original_df = pd.DataFrame(data)

df_copy = original_df.copy()

df_copy['age'] = df_copy['age'].apply(lambda i: int(i) + 5)
print(df_copy)
print("-----------")
print(original_df)
