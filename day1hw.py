# Exercise 1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

cube = 0
for num in range(0,20):
    if cube >= 1000:
        break
    else:
        cube = num**3
        print(cube)


# Exercise #2
# Get first prime numbers up to 100
# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break


prime_list = []
for num in range(2, 101):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime_list.append(num)

print(prime_list) 



# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = int(input("Enter your age: "))
if age < 18 and age >= 0:
    print ("Kids")
elif age >= 18 and age <= 65:
    print("Adults")
elif age > 65:
    print("Seniors")
else:
    print("Invalid entry!!")