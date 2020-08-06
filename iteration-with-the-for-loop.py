# dinner = "Steak and Potatoes"

# for character in dinner:
#     print(character)


# numbers = [2, 3, 5, 7, 10]

# for number in numbers:
#     print(number * number)




# novelists = ["Fitzgerald", "Hemingway", "Steinbeck"]

# for novelist in novelists:
#     print(len(novelist))




# total = 0

# for number in numbers:
#     total = total + number
# print(total)



# # # Coding Exercise 18

# def sum_of_lengths(chars):
#     counting = 0
#     for char in chars:
#         counting = counting + len(char)
#     return(counting)
# print(sum_of_lengths(["Frogs", "Toads"]))



# def product(numbas):
#     counts = 1
#     for num in numbas:
#         counts = counts * num
#     return(counts)
# print(product([1, 2, 3, 4, 5]))



def total_lenght(my_list):
    start_the_list = 0
    for word in my_list:
        start_the_list = start_the_list + len(word)
    return(start_the_list)
print(total_lenght(["Boo", "Too"]))


def product(the_numbers):
    the_list = 1
    for value in the_numbers:
        the_list = the_list * value
    return(the_list)
print(product([1, 2, 3]))