# names = ["Jimmy", "Jaymin", "Nayak"]
# print(names)

# names = ["Jimmy", "Jaymin", "Nayak"]
# print(names[0])

# names = ["Jimmy", "Jaymin", "Nayak"]
# print(names[-1])

# names = ["Jimmy", "Jaymin", "Nayak"]
# print(names[0:1])

# names = ["Jimmy", "Jaymin", "Nayak"]
# print(names[0:3])

# names = ["Jimmy", "Jaymin", "Nayak"]
# print(names[:])

# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# print(f"Max Number is {max(list_of_number)}")


# 2D list demo


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0][0])

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # counter_x = 0
# for row in matrix:
#     # counter_x += 1
#     # counter_y = 0
#     for item in row:
#         # counter_y += 1
#         # print(f"Item at [{counter_x}][{counter_y}] is {item_x[item_y]}")
#         print(f"Item is {item}")


# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# list_of_number.append(99)
# print(list_of_number)

# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# list_of_number.insert(list_of_number.__len__(), 99)
# print(list_of_number)

# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# list_of_number.clear()
# print(list_of_number)

# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# list_of_number.pop(0)
# print(list_of_number)

# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# print(list_of_number.index(88))


# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# print(list_of_number)
# input_number = int(input("Please enter Number : "))
#
# if input_number in list_of_number:
#     print(f"Number is exist at position {list_of_number.index(input_number)}.")
# else:
#     print("Number does not exist.")

# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# print(list_of_number)
# input_number = int(input("Please enter Number to search : "))
#
# if input_number in list_of_number:
#     print(f"""Number is exist at position {list_of_number.index(input_number)} and found {list_of_number.count(
#         input_number)} times.""")
# else:
#     print("Number does not exist.")


# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# print(list_of_number)
# list_of_number.sort()
# print(f"List in ascending order : {list_of_number}")
# list_of_number.reverse()
# print(f"List in descending order : {list_of_number}")

# list_of_number = [1, 88, 4, 7, 5, 9, 6, 4, 11]
# print(list_of_number)
# list_of_number_copy = list_of_number.copy()
# print(f"Copy of list  : {list_of_number_copy}")

# list_of_number = (1, 2, 3)
# x, y, z = list_of_number
# print(x, y, z)


list_of_number = [1, 8, 8, 4, 5, 6, 7, 9, 1, 11, 5, 9, 6, 4, 11]
print(list_of_number)

list_of_unique_number = []

for number in list_of_number:
    if number not in list_of_unique_number:
        list_of_unique_number.append(number)

print(f"Removed duplicate values   : {list_of_unique_number}")
