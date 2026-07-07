def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [23, 4, 4534, 5435, 324, 234]
my_list.sort()
print(binary_search(my_list, 4534))