__author__ = 'Joseph'


list_a = [1, 3, 5, 3, 3, 2, 3, 3, 3, 3]


def majority(a):
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]
    half = int(len(a)/2)
    left = majority(a[0:half])
    right = majority(a[half:])
    if left == right:
        return left
    left_count = len([x for x in a if x == left])
    if left_count > half + 1:
        return left
    right_count = len([x for x in a if x == right])
    if right_count > half + 1:
        return right
    return "No majority element"


def majority_linear(a):
    x = prune(a)
    count = len([y for y in a if y == x])
    if count > len(a)/2:
        return x
    else:
        return "No majority element"


def prune(s):
    n = len(s)
    if n == 1:
        return s[0]
    if n % 2 != 0:
        n -= 1
    s1 = s[::2]
    s2 = s[1::2]
    result = []
    for i in range(0, n/2):
        if s1[i] == s2[i]:
            result.append(s1[i])
    return prune(result)
