

h = '''
List
Tuple
Dictionary
Sets

function(UDF, Built-in): arguments positional, keyword 
lambda function 
Module:
standard module: math, random, time, re
third party module: numpy, pandas

File handling: reading and writing operation with local files
Regular Expression: re 
Exception Handling

'''

# amirkhan1092.c1.biz/dict.pdf

# dictionary creation
# empty
d = {}
print(d, type(d))  # {} <class 'dict'>

d = dict()  # dict constructor
print(d, type(d))  # {} <class 'dict'>




H = ['Vaibhav', 20, 8.0, 'Sec 3', 'GLA']

D = {'name':['Vaibhav', 'sachine'], 'rolln':20, 'institute':'GLA', 'section': 'Sec 3'}

print(H[0])
print(D['name'])




# dictionary operation
dct = { 'rolln':30, 'cpi':8.0, 'section':'A', 'name':'akshay'}
print(dct, type(dct))


d = dct['name']  # element at given key
print(d) #accessing the element
d = dct['address']
print(d)  # keyError

dct['name'] = 'Abhinav'
dct['address'] = 'GLA University'
print(dct)



lst = ['hello', 'Hi', 'address', 'gla']
print(list(range(len(lst))))


# keys() : get all the keys of dict
dct = {'name': 'Govind', 'rolln':30, 'cpi':7.0, 'section':'A'}
out1 = dct.keys()
print(out1, type(out1))  # dict_keys(['name', 'rolln', 'cpi', 'section'])
# <class 'dict_keys'>

print(list(out1))  # ['name', 'rolln', 'cpi', 'section']

# values()
out2 = dct.values()
print(out2, type(out2))  # dict_values(['Govind', 30, 7.0, 'A'])
# <class 'dict_values'>



# update value at key
lst = [2, 4, 5]
lst[4] = 9

dct = {'name':'Govind', 'rolln':30, 'cpi':7.0, 'section':'E'}
dct['name'] = 'akshay'
dct['section'] = 'O'
dct['address'] = 'GLA University'
print(dct)

del dct['name']
print(dct)
dct['Name'] = 'akshay'
print(dct)



d = {1:0, 2:0, 3:0}
print(d)

# clear : to clear the dictionary object as empty
# to clear the items
d = {1: 3, 0: 43}
print(d)
print(id(d))
d.clear()
print(d)
print(id(d))
# {1: 3, 0: 43}
# 237627984
# {}
# 237627984


# copy
d = {1: 3, 0: 43}
y = d.copy()
y.clear()
print(y)
print(d)



# get
d = {'one': 3, 0: 43, (2, 4): 'tuple'}
out = d.get('Address', 'NA')
print(out)  # NA


# fromkeys()
k = ['name', 'rolln', 'section', 'cpi']
d = dict.fromkeys(k, 0)
print(d)  # {'name': 0, 'rolln': 0, 'section': 0, 'cpi': 0}



d = {'entry1':{'name':'Sachin', 'section':'O'}, 'entry2':{'name':'Ravi', 'section':'T'}}

# 1,5,15,23,29,48,52,53,55


# items() : pure form dictionary
dct = {'name':'Govind', 'rolln':30, 'cpi':7.0, 'section':'E'}
pureform = list(dct.items())
print(pureform)
# [('name', 'Govind'), ('rolln', 30), ('cpi', 7.0), ('section', 'E')]



k = [(1, 2), (5, 4), (6, 7)]
d = dict(k)
print(d, type(d))
# {1: 2, 5: 4, 6: 7, 'H': 'i'} <class 'dict'>




# items()
D = {1:3, 4:0}

out = list(D.items())
print(out)  # dict_items([(1, 3), (4, 0)])

ls = [6, 89, 9]
k = ls.pop()


# pop()
D = {'name':'sachin', 'section':'O', 'rolln':30}
del D['rolln']  # deletion statement
k = D.pop('rolln') # return
print(k)
print(D)
# 30
# {'name': 'sachin', 'section': 'O'}


# popitem()
D = {'name':'sachin', 'section':'O', 'rolln':30}
k = D.popitem()
print(k)  # ('rolln', 30)


# update()
D1 = {'Name':'Sachin', 'Section':'O', 'Rolln':30}
D2 = {'CPI':9.0, 'Name':0}
D1.update(D2)
print(D1)  # {'Name': 'Ravi', 'Section': 'O', 'Rolln': 30, 'CPI': 9.0}


# setdefault()
D1 = {'Name': 'Sachin', 'Section': 'O', 'Address': 'IIT Delhi', 'Rolln':20}
D1.setdefault('Rolln', 'NA')
print(D1)



D = {'a': 1, 'b': 5, 'c': 4}
k = D['a', 'b']

h = D.get('a', 'b') # 1


print(k)  # 1







D = {2: 6}
k = D.get(67)
print(k)


fruits = {}
def addone(k):
    if k in fruits:
        fruits[k] += 1
    else:
        fruits[k] = 1
addone('Apple')
addone('Banana')
addone('apple')
print(len(fruits))  # 3





D = {1.0: 20}
D[1] = 100
print(D)  # {1.0: 100}














fr = {}
fr[1] = 1
fr['1'] = 2
fr[1] += 1
s = 0
for i in fr:
    s += fr['1']

print(s)

d = {1.0: 2}
d[1] = 10
print(d)











