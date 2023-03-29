# importing the module
import pandas as pd
import basedosdados as bd

# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_bcb_estban',
table_id='agencia',
billing_project_id="treinamentomysql")

# making the data
scores = {'Name': ['a', 'b', 'c', 'd'],
          'Score': [90, 80, 95, 20]}

# creating the DataFrame
df = pd.DataFrame(scores)

# displaying the DataFrame
print(df)

# converting to CSV file
df.to_csv("dadosBCB.csv", encoding = 'utf-8')