# Good Morning Sir

from time import strftime

# print(strftime("%H"))
hrs = int(strftime("%H"))

name = input("Enter your name: ").capitalize()

if hrs < 12 and hrs >= 5:
    print("Good morning,", name)
elif hrs < 18:
    print("Good afternoon,", name)
elif hrs <= 23:
    print("Good evening,", name)
else:
    print("Hi,", name)
