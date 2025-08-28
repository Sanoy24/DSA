def items_in_common(list1: list, list2: list) -> bool:
    container = {}
    for i in list1:
        container[i] = True
    for j in list2:
        if j in container:
            return True
    return False


list1 = [1, 2, 6]
list2 = [3, 4, 5]
print(items_in_common(list1, list2))
