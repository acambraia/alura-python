import plotly.express as px
import pandas as pd
#import mysql.connector
from dash.dependencies import Output, Input

import mysql.connector
con = mysql.connector.connect(host='172.16.13.112',database='disparador',user='appPython',password='DiwAToT7')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")


#cnx = mysql.connector.connect(user='appPython', password='DiwAToT7', host='172.16.13.112')
#cursor=cnx.cursor()
#query='SELECT * FROM disparador.app_disp_email;'
#df = pd.read_sql(query, cnx)
#cnx.close()

#print(df.head(20))
#print(df.info())
