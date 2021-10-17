
#nested dictionary
mydict1 = {
    'UET' : {'best dept':'software','avg dept':'electrical'},
    'NUST': {'best dept':'civil', 'avg dept':'mechanical'},
}
#1 way to get the values from a dictionary
print(f"Best Department of UET is {mydict1.get('UET').get('best dept')}")
print(f"Average Department of NUST is {mydict1.get('NUST').get('avg dept')}")

#2 way to get the values from a dictionary
print(f"Average Department of UET is {mydict1['UET']['avg dept']}")
print(f"Best Department of Nust is {mydict1['NUST']['best dept']}")

#we can add items in already made dictionary
mydict1['PIEAS'] = {'best dept': 'Mechanical', 'avg dept':'BS Physics'}
print(mydict1)
print(f"Best dept of PIEAS -> {mydict1.get('PIEAS').get('best dept')}")

#we can delete items from the dictionary
# print("Dictionary before deletion of PIEAS key-value pair", mydict1)
# del mydict1['PIEAS']
# print("Dictionary after deletion of PIEAS key-value pair", mydict1)

#we can update an item in dictionary
print(f"Mydict1 before updating PIEAS -> {mydict1['PIEAS']}")
mydict1.update({'PIEAS':{'best dept':'Electrical'}})
print(f"Mydict1 after updating PIEAS -> {mydict1['PIEAS']}")

#we can copy a dictionary to create another dictionary
mydict2 = mydict1.copy()
print(f"content of mydict1 -> {mydict1} \ncontent of mydict2 -> {mydict2}")

#if you assign a dictionary without using copy() then it will be pointing to the original dictionary
# mydict3 = mydict2
#in this case what happens is whenever you are working with mydict3, it will make changes to original mydict2

#we can get the keys and items(keys+vals) of a dictionary 
#show keys
print(mydict2.keys())
#show keys+vals
print(mydict2.items())