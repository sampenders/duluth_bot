import requests
import json
import sqlite3

# this script gets a list of records
# that incldue some keywords, and updates
# a working copy of the database with that

con = sqlite3.connect('photoDB.db')
cur = con.cursor()

#base_url = 'https://collection.mndigital.org/catalog.json?f%5Bcontributing_organization_ssi%5D%5B%5D=University+of+Minnesota+Duluth%2C+Kathryn+A.+Martin+Library%2C+Northeast+Minnesota+Historical+Collections&f%5Btype_ssi%5D%5B%5D=Still+Image&per_page=100'
base_url = 'https://collection.mndigital.org/catalog.json?f%5Bcontributing_organization_ssi%5D%5B%5D=Iron+Range+Research+Center&f%5Btype_ssi%5D%5B%5D=Still+Image&per_page=100'

records = []

for i in range(1,12):

    url = base_url + '&page=' + str(i)
    r = requests.get(url)
    data = json.loads(r.text)['response']['docs']
    new_records = []

    for j in range(0,len(data)):
        new_records.append(data[j]['id'].split(':')[1])

    records += new_records

print(records)

for id_ in records:
    coll = 'irrc'
    full_id = coll + '_' + id_

    cur.execute('''INSERT OR IGNORE INTO photos (id, collection, record)
        VALUES (?, ?, ?)''', (full_id, coll, id_)) 

con.commit()
con.close()
