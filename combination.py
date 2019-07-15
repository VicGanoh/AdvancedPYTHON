def is_even():
    numbers = [1,56,234,87,4,76,24,69,90,135]
    print("The odd numbers are:",[number for number in numbers if not number%2==0])
# call fxn
is_even()