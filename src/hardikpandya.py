def bubble_sort(arr: list = []) -> None:
    """
    This function sort array or list given inplace
    :param arr: iterable array or list
    :return: None
    """
    size = len(arr)
    for i in range(size-1):
        flag = 0
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
        print(arr)
        if flag == 0:
            break



print("Bubble sort working step by step\n")
bubble_sort([3, 7, 4, 2, 1])


