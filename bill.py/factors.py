""" def factors(x):
    x=int(input("give me number:"))
    factor=[]
    for i in range (1,x+1):
        if x % i == 0:
            factor.append(i)
    print(f"the factors of, {x} are {factor}")

factors(1) """
import math
number=int(input("give number"))
number2=int(input("give number again"))
gcf=math.gcd(number,number2)
print("the gcf of", number,"and",number2,"is:", gcf)