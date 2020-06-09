# enumerate, a generator object, lets you iterate over string and keep track of its position
# always use index aka idx position first but names can be anything; idx, task aka errands
# index + 1 or enumberate(errands, 1) starts index at 1, not 0 OR use starting point after enumerate function
# the variable names index and errand are whatever you want to call them

errands = ["Go to gym", "Grab a lunch", "Get promoted at work", "Sleep"]

# print(enumerate(errands))

for index, errand in enumerate(errands):         
    print(f"{errand} is number {index + 1} on my list of things to do today!")





# Coding Exercise 20

# def in_list(strings, string):
#     for index, group in enumerate(strings):
#         if group == string:
#             return index
#     return -1
# print(in_list(["A", "B", "C"],"C"))




# def sum_of_values_and_indices(number_list):
#     values = 0
#     for index, numbers in enumerate(number_list):
#         values = (index + numbers) + values
#     return values
# print(sum_of_values_and_indices([0, 0, 0, 0]))





# def index_list(strings, string):
#     for index, word in enumerate(strings):
#         if index == string:
#             return word
# print(index_list(["A", "B", "C"], 2))





# Coding Exercise 21

# def length_match(strings, integer):
#     for index, animal in enumerate(strings):
#         if len(animal) == integer:
#             return index
# print(length_match(["cat", "dogs", "mouse"], 4))


# def sum_from(int_1, int_2):
#     total = 0
#     for number in range(int_1, int_2):
#         total = total + number
#     return total
# print(sum_from(3, 9))


# def same_index_values(list1, list2):
#     results = []
#     for index, value in enumerate(list1):
#         if value == list2[index]:
#             results.append(index)
#     return results
# print(same_index_values([1, 2, 3], [3, 2, 1]))