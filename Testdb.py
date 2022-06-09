import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('testdb_credentials.json', scope)
client =gspread.authorize(credentials)


# sheet = client.create("FirstTest")
# sheet.share('nelumindralal@gmail.com', perm_type ='user', role='writer')

sheet = client.open("FirstTest")

# df = pd.read_csv('sales_data.csv')
with open('sales_data.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(sheet.id, data=content)
