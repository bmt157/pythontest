import requests
import json
import csv 


# API_KEY = '4a1c3b012b15793cff8ce8f359fe1f26'
# PASSWORD = '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'
# SHOP_NAME = 'gonn113'

rep = requests.get('https://4a1c3b012b15793cff8ce8f359fe1f26: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@gonn113.myshopify.com/admin/api/2021-01/customers.json')
stri = rep.text
# print(stri)
data = json.loads(stri)
# print(data.keys())
# print(data)
customersList = data['customers']
print(customersList)
# with open('customersShopify.csv', 'w') as f:
#     csv_coumns = customersList[0].keys()
#     writer = csv.DictWriter(f, fieldnames=csv_coumns)
#     writer.writeheader()
#     for dt in customersList:
#         writer.writerow(dt)



# print(jsonCustomer)





