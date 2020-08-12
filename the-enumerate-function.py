# enumerate, a generator object, lets you iterate over string and keep track of its position
# always use index aka idx position first but names can be anything; idx, task aka errands
# index + 1 or enumberate(errands, 1) starts index at 1, not 0 OR use starting point after enumerate function
# the variable names index and errand are whatever you want to call them

errands = ["Go to gym", "Grab a lunch", "Get promoted at work", "Sleep"]

# print(enumerate(errands))

for index, errand in enumerate(errands):         
    print(f"{errand} is number {index + 1} on my list of things to do today!")