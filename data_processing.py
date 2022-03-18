import json
import psycopg2 as psdb
import urllib
import requests

# loads the data directly from  a local file
with open('files/malaria_facilities.json', 'r') as f:
    data = json.load(f)

# Load the data from an API
# url = ''
# data = json.load(urllib.urlopen(url))

# Initialise a database connection to postgre
conn = psdb.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123456")

# Separate the list of facilities whose report has been updated.
f_list = [i for i in data['rows'] if i[2] == '1.0']

cursor = conn.cursor()
for fa in f_list:
    print(fa)
    facility_id = fa[1]
    status = fa[2]
    sql_query = f"UPDATE rdt_facilities SET report_count = 1 WHERE uid = '{facility_id}'"
    sql_query1 = "SELECT * FROM public.rdt_facilities"
    cursor.execute(sql_query)
    cursor.execute(sql_query1)

print(cursor.fetchall())
conn.commit()


conn.close()