def even_numbers(limit):
    for num in range(limit + 1):
        if num%2==0:
            yield num
            
for number in even_numbers(10):
    print(number)            