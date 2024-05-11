list1 = input()
new_str=""
new_str1=""
new_str2=""
a="#"
b="?"
c="*"
for i in range(len(list1)):
    if list1[i]=="A" or list1[i]=="a" or list1[i]=="E" or list1[i]=="e" or list1[i]=="I" or list1[i]=="i" or list1[i]=="O" or list1[i]=="o" or list1[i]=="U" or list1[i]=="u" or list1[i]=="Y" or list1[i]=="y":
        new_str+=a
        new_str1+=b
        new_str2+=c
    else:
        new_str+=list1[i]
        new_str1+=list1[i]
        new_str2+=list1[i]
print(new_str)
print(new_str1)
print(new_str2)