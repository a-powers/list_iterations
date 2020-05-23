# value = [3, 6, 9, 12, 15, 18, 21, 24]
# other_values = [5, 10, 15, 20, 25, 30]

# def odds_sum(numbers):
#     total = 0
#     for number in numbers:
#         if number % 2 == 1:
#             total += number
#     return total
# print(odds_sum(value))
# print(odds_sum(other_values))





# def greatest_numbers(numbers):
#     greatest = numbers[0]
#     for number in numbers:
#         if number > greatest:
#             greatest = number
#     return greatest

# print(greatest_numbers([1, 2, 3, 4, 5]))



# Coding Exercise 19

def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
print(smallest_number([5, 4, 3]))


def concatenate(words):
    alphabet = ""
    for word in words:
        if len(word) > 2:
            alphabet += word
    return alphabet
print(concatenate(["Aaa", "Bbb", "Cc"]))


def super_sum(the_strings):
    total = 0
    for string in the_strings:
        if string.find('s'):
            total += string.find('s')
    return total
print(super_sum(["Abs", "Abs"]))