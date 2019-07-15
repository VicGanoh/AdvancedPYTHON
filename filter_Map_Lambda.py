def is_even():#get user input and print a true if even
    number = float(input("Enter a number: "))
    if number % 2 == 0:
        print("Its an even number")
        return True
    else:
        print("Sorry please enter an even number")
        return False
# call fxn
print(is_even())
print ()

def is_even1():
    numbers = [1,56,234,87,4,76,24,69,90,135]
    print ("The even numbers are:",[number for number in numbers if number%2==0])
    print ("The odd numbers are:",[number for number in numbers if not number%2==0 ])
is_even1()

print()
#filter and lambda (alternative)
numbers = [1,56,234,87,4,76,24,69,90,135]
expo = list(filter(lambda number: (number%2==0), numbers))
print (expo)