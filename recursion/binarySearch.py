def binary_search(my_list, low, high, elem):
    if high >= low:
        mid = (high + low) // 2
        if my_list[mid] == elem:
            return mid
        elif my_list[mid] > elem:
            return binary_search(my_list, low, mid - 1, elem)
        else:
            return binary_search(my_list, mid + 1, high, elem)
    else:
        return -1


if __name__ == "__main__":

    my_list = [1, 9, 11, 21, 34, 54, 67, 90]
    elem_to_search = 1
    print("The list is")
    print(my_list)

    my_result = binary_search(my_list, 0, len(my_list) - 1, elem_to_search)

    if my_result != -1:
        print("Element found at index ", str(my_result))
    else:
        print("Element not found!")
