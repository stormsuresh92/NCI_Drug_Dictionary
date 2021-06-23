import requests
import pandas as pd

drug_list = []
 
file = open('drugs.txt', 'r')
urls = file.readlines()
for url in urls:
    print(url)
    r = requests.get(url)
    json_obj = r.json()
    for data in json_obj['results']:
        id = data['termId']
        drug_name = data['name']
        try:
            Desc = data['definition']['text']
        except:
            Desc = ''
        infos = {
            'ID' : id,
            'Drug_Nmae' : drug_name,
            'Definition' : Desc
        }
        drug_list.append(infos)

df = pd.DataFrame(drug_list)
df.to_csv('NCI_drug_data.csv', index=False)
print('urls downloaded')
