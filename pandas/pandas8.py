import pandas as pd

'''
customers = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName":  ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders = {
    "OrderId": [10,11,12,13],
    "CustomerId": [1,2,5,7],
    "OrderData": ["2010-07-04","2010-08-04","2010-07-07","2012-07-04"]
}

df_custormers = pd.DataFrame(customers, columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders, columns=["OrderId","CustomerId","OrderData"])

print(df_custormers)
print(df_orders)

result = pd.merge(df_custormers,df_orders,how="inner")
result = pd.merge(df_custormers,df_orders,how="left")
result = pd.merge(df_custormers,df_orders,how="right")
result = pd.merge(df_custormers,df_orders,how="outer")
print(result)
'''

customersA = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName":  ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    "CustomerId": [5,6,7,8],
    "FirstName": ["Yağmur","Çınar","Cengiz","Can"],
    "LastName":  ["Bilge","Turan","Yılmaz","Turan"]
}

df_custormerA = pd.DataFrame(customersA)
df_customersB = pd.DataFrame(customersB)

result = pd.concat([df_custormerA,df_customersB])
result = pd.concat([df_custormerA,df_customersB],axis=1)

print(result)