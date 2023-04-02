def get_positive_numbers():
    numbers = input("Enter a sequence of numbers separated by commas: ").split(',')
    positive_numbers = [int(num) for num in numbers if int(num) > 0]
    return positive_numbers


print(get_positive_numbers())
