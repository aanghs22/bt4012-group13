import pandas as pd

full_df = pd.DataFrame()
i = 0
while True:
    try:
        df = pd.read_csv(f'data/queried/transactions_{i}.csv')
        full_df = pd.concat([full_df,df])
        i += 1
    except:
        full_df.to_csv('data/queried/full_transactions.csv', index=False)
        break