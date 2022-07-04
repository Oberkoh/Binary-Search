# l is a given list
# we search using the regular method
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# searching using binary search
# for this search to work, the list must be sorted
def binary_search(l, target, low = None, high = None):
    if high == None:
        high = len(l) - 1
    if low == None:
        low = 0
    if high < low: # not in list
        return -1

    midpoint = (low+high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)
        

if __name__ == '__main__':
    l = [1, 3, 5, 10, 15]
    target = 10
    print(f"The position of {target} in the list is position: {naive_search(l, target)}")
    print(f"The position of {target} in the list is position: {binary_search(l, target)}")