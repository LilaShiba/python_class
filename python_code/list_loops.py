#1

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
    if number % 2 == 0:
       print(number)


#2

fizz_list = ['fizz', 'butt', 'pop', 'meow', 'fizz']

def fizz_count(fizz):
    total = 0
    for f in fizz:
        if f == 'fizz':
            total = total + 1
    return total
example = fizz_count(fizz_list)
print (example)