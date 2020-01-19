customer_dictionaries = {
    "name": "James don",
    "age": 28,
    "is_smuggler": False
}

# print(customer_dictionaries["name"])

# customer_dictionaries["name"] = " John Don"

# print(customer_dictionaries.get("dob","19 sep 1991"))

# customer_dictionaries["dob"] = "19 sep 1991"
# print(customer_dictionaries.get("dob"))

# print(customer_dictionaries.get("name"))

# number_dictionaries = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#
# }
#
# phone = input("Enter Phone : ")
# output = ''
# for num_char in phone:
#     output += number_dictionaries.get(num_char, "!") + " "
#
# print(output)

mode_dictionaries = {
    "good": "😀",
    "sad": "☹️",
    "love": "🥰",
    "cycling": "🚵",
    "party": "🥳",
    "angry": "😡",

}

mode = input("How is your mode? ").lower()

print(mode_dictionaries.get(mode, "😰"))
