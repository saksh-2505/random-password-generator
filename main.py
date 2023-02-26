import random

list = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '}', '{', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a',  's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']

password = []
f = open('idea.txt' , 'a')
website = input("enter the name of website")
username = input("enter you username")
for i in range(1,17):
    password.append(list[random.randint(0,len(list)-1)])
print(password)
password_in_string = ""
for i in password:
    password_in_string += i
print(password_in_string)
f.write(username +" "+ website +" " + password_in_string + '\n')