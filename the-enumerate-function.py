# enumerate, a generator object, lets you iterate over string and keep track of its position
# always use index aka idx position first but names can be anything; idx, task aka errands
# index + 1 or enumberate(errands, 1) starts index at 1, not 0 OR use starting point after enumerate function
# the variable names index and errand are whatever you want to call them

# errands = ["Go to gym", "Grab a lunch", "Get promoted at work", "Sleep"]

# # print(enumerate(errands))

# for index, errand in enumerate(errands):         
#     print(f"{errand} is number {index + 1} on my list of things to do today!")





# Coding Exercise 20

def in_list(strings, string):
    for index, group in enumerate(strings):
        if group == string:
            return index
    return -1
print(in_list(["A", "B", "C"],"C"))




def sum_of_values_and_indices(number_list):
    values = 0
    for index, numbers in enumerate(number_list):
        values = (index + numbers) + values
    return values
print(sum_of_values_and_indices([0, 0, 0, 0]))