# Dictionaries --> Key Value pairs
# fast access by using key 
dic={
    "harry":"human being",
    "Spoon":"object",
    7673:"Kewl"
}
print(dic["harry"])
print(dic.get('name')) # prints none if key not exist
print(dic.keys())
print(dic.values())
for key in dic.keys():
    print(f" The value corresponding to the key {key} is {dic[key]}")

print(dic.items()) #prints all key value pairs

for key,value in dic.items():
    print(f" The value corresponding to the key {key} is {dic[key]}")