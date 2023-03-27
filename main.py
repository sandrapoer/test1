# QUESTION NR1
def count_integer(numbers, integer):
    count = 0
    for num in numbers:
        if num == integer:
            count += 1
    if count == 0:
        return 42
    else:
        return count

# QUESTION NR2
def list_func(numbers, integer):
    if integer not in numbers:
        return []
    for index in range(0, len(numbers), 1):
        if numbers[index] == integer:
            numbers[index] = 6
    numbers.reverse()
    print(numbers)
    numbers.reverse()
    return numbers



# QUESTION NR3
def compare_lists(list1, list2):
    new_list = []
    for num in list1:
        if num in list2 and num not in new_list:
            new_list.append(num)
    return new_list

# QUESTION NR4
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

# QUESTION NR5
def dict_func(dictionary):
    for key in ['Type', 'Brand', 'Price']:
        if key not in dictionary.keys():
            dictionary.update({key: f"unknown {key}"})
    print(f"You have a {dictionary['Type']} from {dictionary['Brand']} that costs {dictionary['Price']}")
    dictionary["OS"] = "Linux"
    print(dictionary)
    return dictionary