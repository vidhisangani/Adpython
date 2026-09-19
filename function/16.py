
def largest(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

print(largest([10, 25, 15, 40, 20]))

