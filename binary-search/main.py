
a = [1,3,4,6,7,8,11,13,14,15,16,17]
target = 14

def bianry_search(a: list[int], target: int) -> int:
    l, r = 0, len(a) -1
    while l <= r:
        m = (l + r)//2
        if target == a[m]:
            return m
        elif target > a[m]:
            l = m + 1
        else:
            r = m - 1 
    return -1        

print(bianry_search(a, target))