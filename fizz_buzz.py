#code starts here.
#
#Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, 
#all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.
#When the number is not divisible by 3 or 5, the number itself should be returned.
#
def fizz_buzz(n):
#check if n is divisible by 3 and 5,return FizzBuzz
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
        #check if nis divisible by 3,print Fizz
    elif n % 3 == 0:
        return 'Fizz'
        #check if n is divisible by 5,return Buzz
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
        
#print result
print(fizz_buzz(5))



print(fizzbuzz(5))

