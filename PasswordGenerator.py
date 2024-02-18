#password generator project
import random

symbles=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=[1,2,3,4,5,6,7,8,9,0]
sp_chrt=['!','@','#','$','%','*']

len_of_pass=int(input("what is the length of your password\n"))
letters=int(input("How many letters ?\n"))
num=int(input("How many numbers ?\n"))
sp=int(input("How many sp symbles ?\n"))

password_chosen=[]
for i in range(letters):
    password_chosen.append(random.choice(symbles))
for i in range(num):
    password_chosen.append(random.choice(numbers))
for i in range(sp):
    password_chosen.append(random.choice(sp_chrt))

random.shuffle(password_chosen)

for i in password_chosen:
    print(i, end="")



