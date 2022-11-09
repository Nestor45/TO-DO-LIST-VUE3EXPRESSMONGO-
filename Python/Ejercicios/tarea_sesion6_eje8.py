

list1 = [3, 7, 2, 8, 1, 5, 13]
list2 = [7, 10, 5, 4, 0, 9, 3]
def count_in_common(list1, list2):  
    change_to_set1 = set(list1)
    change_to_set2 = set(list2)
    return len(change_to_set1.intersection(change_to_set2))

print("d =",count_in_common(list1, list2))
