#Basic If-Else:


#Q1.
#Solution:
num = int(input("Enter a number:"))
if num > 0:
    print("Positive")
if num < 0:
    print("Negative")
else:
    print("Zero")

#Q2.
#Solution:
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q3.
#Solution:
num = int(input("Enter a year:"))
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#Q4.
#Solution:
num1 = int(input("Enter A:"))
num2 = int(input("Enter B:"))
if num1 > num2:
    print("A is greater")
if num1 < num2:
    print("B is greater")
else:
    print("A and B are equal")

#Q5.
#Solution:
num = int(input("Enter your age:"))
if num >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Q6.
#Solution:
a = input("Enter a single letter:")
if not a.isalpha() or len(a) != 1:
    print("Invalid input")
else:
    b = a.lower()
    if (b == 'a' or 
        b == 'e' or 
        b == 'i' or 
        b == 'o' or 
        b == 'u'):
        print(a, "is a Vowel.")
    else:
        print(a, "is a Consonant.")

#Q7.
#Solution:
num = int(input("Enter a number:"))
if num % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

#Q8.
#Solution:
num = (input("Enter a number:"))
if len(num) == 1:
    print("Number is single-digit")
if len(num) == 2:
    print("Number is two-digit")
else:
    print("Number is more than two-digit")

#Q9.
#Solution:
num = int(input("Enter your marks:"))
if num >= 40:
    print("You're pass")
else:
    print("You're fail")

#Q10.
#Solution:
num = int(input("Enter a number:"))
if num % 3 == 0 and num % 7 == 0:
    print("Number is divisible by both 3 and 7")
else:
    print("Number is not divisible by 3 and 7")


#Ladder If & Nested If:


#Q1.
#Solution:
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a >= b and a >= c:
    print(a, "is greatest")
elif b >= a and b >= c:
    print(b, "is greatest")
else:
    print(c, "is greatest")

#Q2.
#Solution:
num = int(input("Enter your age:"))
if num < 13:
    print("You are child")
elif num < 20:
    print("You are teenager")
elif num < 60:
    print("You are adult")
else:
    print("You are senior citizen")

#Q3.
#Solution:
num = int(input("Enter your marks:"))
if num >= 90:
    print("Grade A")
elif num >= 75:
    print("Grade B")
elif num >= 50:
    print("Grade C")
elif num >= 35:
    print("Grade D")
else:
    print("Fail")

#Q4.
#Solution:
a = int(input("Enter side A:"))
b = int(input("Enter side B:"))
c = int(input("Enter side C:"))
if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a triangle")

#Q5.
#Solution:
a = input("Enter a single character:")
if len(a) == 1:
    if a.isupper():
        print("It is uppercase letter")
    elif a.islower():
        print("It is lowercase letter")
    elif a.isdigit():
        print("It is a digit")
    else:
        print("It is a special symbol")
else:
    print("Invalid")

#Q6.
#Solution:
num = int(input("Enter units consumed:"))
a = 0
if num <= 100:
    a = num * 5
elif num <= 200:
    a = (100 * 5) + ((num - 100) * 7)
else:
    a = (100 * 5) + (100 * 7) + ((num - 200) * 10)
print("Your electricity bill is ₹", a)

#Q7.
#Solution:
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))
if a > b:
    if a > c:
        if a > d:
            lar = a
        else:
            lar = d
    else:
        if c > d:
            lar = c
        else:
            lar = d
else:
    if b > c:
        if b > d:
            lar = b
        else:
            lar = d
    else:
        if c > d:
            lar = c
        else:
            lar = d
print("The largest number is:", lar)

#Q8.
#Solution:
num = int(input("Enter a year:"))
if num % 100 == 0:
    if num % 400 == 0:
        print("It is a century and leap year")
    else:
        print("It is a century year but not a leap year")
else:
    if num % 4 == 0:
        print("It is a leap year but not a century year")
    else:
        print("It is neither a century year nor a leap year")

#Q9.
#Solution:
num = float(input("Enter your BMI value:"))
if num < 18.5:
    print("Underweight")
elif num <= 24.9:
    print("Normal")
elif num <= 29.9:
    print("Overweight")
else:
    print("Obese")

#Q10.
#Solution:
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))  
c = int(input("Enter third number:"))
if a < b:
    if a < c:
        min = a
    else:
        min = c
else:
    if b < c:
        min = b
    else:
        min = c
print("The smallest number is:", min)


#For Loop::


#Q1.
#Solution:
print("Armstrong numbers b/w 100 and 999 are:")
for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    sum = (a ** 3) + (b ** 3) + (c ** 3)
    if i == sum:
        print(i)

#Q2.
#Solution:
n = int(input("Enter how many prime numbers you want: "))
count = 0
num = 2
print(f"The first {n} prime numbers are:")
while count < n:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1

#Q3.
#Solution:
print("All numbers from 1 to 500 divisible by 3 with digit sum ≤ 10:")
for i in range(1, 501):
    if i % 3 == 0:
        sum = 0
        temp = i
        while temp > 0:
            sum += temp % 10
            temp //= 10
        if sum <= 10:
            print(i)

#Q4.
#Solution:
n = int(input("Enter the height of the pyramid: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2*i - 1))

#Q5.
#Solution:
a = input("Enter a string: ")
a = a.lower()
letters = set()
for i in a:
    if i.isalpha():  
        letters.add(i)
if len(letters) == 26:
    print("The string is a pangram")
else:
    print("The string is not a pangram")

#Q6.
#Solution:
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Twin primes between 1 and 100:")
for num in range(2, 99):
    if is_prime(num) and is_prime(num + 2):
        print(f"({num}, {num+2})")

#Q7.
#Solution:
num = int(input("Enter a number: "))
sum = 0
for i in str(num):
    sum += int(i)
if num % sum == 0:
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")

#Q8.
#Solution:
n = int(input("Enter number of rows: "))
for i in range(n):
    print(" " * (n - i), end="")
    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()

#Q9.
#Solution:
n = int(input("Enter the value of n: "))
tot = 0
for i in range(1, n + 1):
    tot += i ** 2
print("Sum of the series 1² + 2² + ... +", n, "² is:", tot)

#Q10.
#Solution:
num = int(input("Enter a number: "))
a = num
sum = 0
for i in str(num):
    fact = 1
    for j in range(1, int(i) + 1):
        fact *= j
    sum += fact
if sum == a:
    print(a, "is a Strong number")
else:
    print(a, "is not a Strong number")


#While Loop:


#Q1.
#Solution:
num = int(input("Enter a number:"))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print("Reversed number:", rev)

#Q2.
#Solution:
tsum = 0
while tsum <= 100:
    num = input("Enter a number: ")
    if not num.isdigit():
        print("Please try again")
        continue
    curr = 0
    for digit in num:
        curr += int(digit)
    tsum += curr
    print("Sum of digits for", num, "is", curr)
    print("The running total is now:", tsum)
print("Program ended as sum exceeded 100")

#Q3.
#Solution:
num = input("Enter a number: ")
if num[0] == '0':
    print(num, "is not a Duck number")
else:
    a = False
    i = 0
    while i < len(num):
        if num[i] == '0':
            a = True
            break
        i += 1
    if a:
        print(num, "is a Duck number")
    else:
        print(num, "is not a Duck number")

#Q4.
#Solution:
num = int(input("Enter a number:"))
a = num
b = set()
while num != 1 and num not in b:
    b.add(num)
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 2
        temp //= 10
    num = sum
if num == 1:
    print(a, "is a Happy number")
else:
    print(a, "is not a Happy number")

#Q5.
#Solution:
num = int(input("Enter a number: "))
a = num
fact = 2
lar = 0
while num > 1:
    if num % fact == 0:
        lar = fact
        num //= fact
    else:
        fact += 1
print("The largest prime factor of", a, "is:", lar)

#Q6.
#Solution:
while True:
    text = input("Enter text:")
    if text == text[::-1]:
        print("'", text, "' is a palindrome.")
        break
    else:
        print("'", text, "' is not a palindrome.")

#Q7.
#Solution:
num = int(input("Enter a number:"))
while num >= 10:
    sum = 0
    temp = num
    while temp > 0:
        a = temp % 10
        sum += a
        temp //= 10
    num = sum  
print("Digital root is:", num)

#Q8.
#Solution:
n = int(input("Enter a number to generate its Collatz sequence:"))
print("Collatz sequence:")
print(n, end=" ")
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n, end=" ")

#Q9.
#Solution:
num = int(input("Enter a number:"))
a = num
while True:
    numsq = num ** 2
    b = str(numsq)
    length = len(str(num))
    right = int(b[-length:]) if b[-length:] else 0
    left = int(b[:-length]) if b[:-length] else 0
    if left + right == num:
        print(num, "is a Kaprekar number")
    else:
        print(num, "is not a Kaprekar number")
    choice = input("Do you want to check another number? (y/n): ")
    if choice != "y":
        break
    num = int(input("Enter a number:"))

#Q10.
#Solution:
bal = 1000  
while True:
    print("--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    num = int(input("Choose one (1-4):"))
    if num == 1:
        print("Your current balance is $", bal)
    elif num == 2:
        dep = int(input("Enter amount to deposit: $"))
        if dep > 0:
            bal += dep
            print("$", dep, "deposited successfully")
        else:
            print("Invalid deposit amount")
    elif num == 3:
        withdraw = int(input("Enter amount to withdraw: $"))
        if withdraw <= bal:
            bal -= withdraw
            print("$", withdraw, "withdrawn successfully")
        else:
            print("Insufficient balance!")
    elif num == 4:
        print("Goodbye")
        break
    else:
        print("Invalid. Please select from 1 to 4.")