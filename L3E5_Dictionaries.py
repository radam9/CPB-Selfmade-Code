#dictionary
mydic = {'key1':'value1', 'key2':'value2'}
print(mydic)
print(mydic['key1'])
prices = {'apple':2.99,'orange':1.99,'milk':5.80}
print(prices['orange'])
#flexibility of dictionaries
d = {'k1':123,'k2':[4,5,6],'k3':{'ik1':100,'ik2':'abc'}}
print(d['k2'])
print(d['k3']['ik2'])#the second key is for the dictionary inside the dictionary d
print(d['k2'][2])
d1 = {'k1':['a','b','e']}
print(d1['k1'][2].upper())
#addint items to a dictionary
d2 = {'k1':100,'k2':200}
d2['k3'] = 300
print(d2)
#assigning new values to exisitng keys
d2['k1'] = 'NEW VALUE'
print(d2)
#grab keys, value or items from a dictionary
d = {'k1':100,'k2':200,'k3':300}
print(d.keys())#print dictionary keys
print(d.values())#print dictionary values
print(d.items())#print dictionary pairs (they end up being tuples)
