import pyodbc
import pandas as pd

if __name__ == "__main__": 

    '''pandas aproch'''

connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
                            'SERVER=REXCOM;'
                            'DATABASE=CFDI33;'
                            'User=sa;'
                            'Password=Bardo28242528@;'
                            'Trusted_Connection=yes;')


query =("SELECT top 100 * from factfactura")

data = pd.read_sql(query, connection)
del connection
for i in data.index:
    print(data['FACTURA'][i], data['CONSECUTIVO'][i])


