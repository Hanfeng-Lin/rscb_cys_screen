import pandas as pd


df1 = pd.read_csv('pdb_cys.csv')
df2 = pd.read_excel('uniprot_IDmapping.xlsx')
merged_df = pd.merge(df2, df1, on='pdb_id')
merged_df.to_excel('uniprot_IDmapping.xlsx', index=False)
