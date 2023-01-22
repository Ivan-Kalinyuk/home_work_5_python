file = open('file1.txt','w')
file.write('8a3b1c')
file.close()

file = open('file1.txt','r')
str1 = file.readlines()
file.close()

str1 = str (str1)
str1 = str1.replace('[','')
str1 = str1.replace(']','')
str1 = str1.replace(']','')
str1 = str1.replace("'",'')
print(str1)
print(type(str1))
str2 = ''
hp = ''

for i in str1:
    if i.isdigit():
        hp = hp + i
    else:
        str2 = str2 + i * int(hp)
        hp=''
print(str2)
  


