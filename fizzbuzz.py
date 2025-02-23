#Create a program that will run through the integers 1 to 25.
#If the number is a multiple of 3, print "Fizz"
#If the number is a multiple of 5, print "Buzz"
#If the number is a multiple of 3 and 5 print "FizzBuzz"
#If the number is not any of the stated multiples, print the number.
#Each output is on it's own line
#Also include in your repo a .drawio file that flowcharts out the logic

#Here is a section of sample output:
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz

thislist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
n = int(input())
count3,count5 = 1,1
for x in range(1,n+1):
    print("Fizzbuzz")
    count3,count5 = 0,0
elif count3 == 3:
    print("Fizz")
    couunt3 = 0
elif count5 == 5:
    print("Buzz")
    count5 = 0 
else:
    print(x)
count3 += 1
count5 += 1