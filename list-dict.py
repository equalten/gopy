fruit_list = ["apple", "apple", "banana", "peach", "banana", "tomato", "apple"]

count_table = {}

for fruit in fruit_list:
    if fruit in count_table:
        count_table[fruit] = count_table[fruit] + 1
    else:
        count_table[fruit] = 1

print(count_table)