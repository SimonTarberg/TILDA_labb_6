def binary_search(the_list, key):
    low = 0
    high = len(the_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if the_list[mid] == key:
            return key
        elif the_list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return None


def main():
    indata = input().strip()
    the_list = indata.split()

    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()


main()
