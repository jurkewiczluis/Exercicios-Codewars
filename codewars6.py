def invert(lst):
    inverted_list = []

    for item in lst:
        inverted_item = item * -1
        inverted_list.append(inverted_item)

    return inverted_list    

input_list = [1, 2, 3, 4, 5]
print(invert(input_list))

input_list = [-1, -2, -3, -4, -5]
print(invert(input_list))

input_list = [1, -2, 3, -4, 5]
print(invert(input_list))

input_list = []
print(invert(input_list))