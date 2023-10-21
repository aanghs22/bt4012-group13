import pandas as pd

full_df = pd.DataFrame()
for i in range (88):
    df = pd.read_csv(f'transactions_{i}.csv')
    full_df = pd.concat([full_df,df])


full_df.to_csv("full_transactions.csv")
