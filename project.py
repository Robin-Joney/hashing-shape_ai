import hashlib

stri=input("Enter string : ")
result=hashlib.md5(stri.encode())

#Hexadecimal Hash value
print("The Hexadecimal Hash value of String is : ",end ="")
print(result.hexdigest())

#Byte Equivalent value 
print("The Byte Equivalent of Sting is : ",end ="")
print(result.digest())

#Salting
str=result.hexdigest()+stri
print("The Salted String is : ",str)


