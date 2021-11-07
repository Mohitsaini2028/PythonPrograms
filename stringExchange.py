#Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string. Sample String : 'abc', 'xyz' Expected Result : 'xbc ayz'

a="abc"
b="xyz"

result=b[0]+a[1:]+" "+a[0]+b[1:]
print(result)
