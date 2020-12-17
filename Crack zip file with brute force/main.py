"""
main.py
This program crack a zip file using brute force

Writed by TOTOW
Program from : Neuralnine : https://www.youtube.com/watch?v=V5eFw8hdts8&list=PL7yh-TELLS1GmTcE9tLKsrQ5iCAtnLAc1&index=2
"""

import zipfile

charlist = 'abcdefghijklmnopqrstuvwxyz'
length_of_password = 4
complete = []

# algorithm of brute force
for current in range(length_of_password):
    a = [i for i in charlist]
    for x in range(current):
        a = [y + i for i in charlist for y in a]
    complete = complete + a

print(complete)

z = zipfile.ZipFile('secret.zip')

tries = 0

# Try to write the password
for password in complete:
    try:
        tries += 1
        z.setpassword(password.encode('ascii'))
        z.extract('secret.txt')
        print(f"Password was found after {tries} tries! It was {password}!")
        break

    except:
        pass


