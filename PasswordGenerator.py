import random

#lists for all possible types of characters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l", "m", "n", "o", 
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", 
           "E", "F", "G", "H", "I", "J","K","L", "M", "N", "O", "P", "Q", "R", "S", "T", 
           "U", "V", "W", "X", "Y", "Z"]
numbers = ["1","2", "3", "4", "5", "6", "7", "8","9", "0"]
sChars = ['!','$','%','^','&', '!']

#make list of all lists
allLists = [letters, numbers, sChars]

pwLen = int(input("Enter the number of characters needed for your password:"))
#set length of password
pw = [0] * pwLen
for i in range(0, pwLen):
  l = random.choice(allLists)
  pw[i] = random.choice(random.choice(l))

print(pw)
#combine all list values to one string
pwS = "".join(pw)
print(pwS)