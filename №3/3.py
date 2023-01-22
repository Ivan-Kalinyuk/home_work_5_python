file = open('file.txt','w')
file.write('aaaacrrrrmm')
file.close()

file = open('file.txt','r')
str1 = file.readlines()
file.close()

str1 = str (str1)
str1 = str1.replace('[','')
str1 = str1.replace(']','')
str1 = str1.replace(']','')
str1 = str1.replace("'",'')
print(str1)


list1 = []
for i in str1:
    list1.append(i)
# print(list1)

dict1 = {}
for i in list1:
    dict1[i] = dict1.get(i,0) + 1
# print(dict1)

list2 = []

for k, j in dict1.items():
    
    list2.append(j)
    list2.append(k)

print(*list2,sep='')
 

