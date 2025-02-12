

def product_sum(lst: list[int]) -> list[int]:
    prefix = [1 for _ in lst]
    postfix = [1 for _ in lst]

    prefix[0] = lst[0]
    for i in range(1, len(lst)):
        prefix[i] = prefix[i-1] * lst[i]

    postfix[-1] = lst[-1]
    for i in range(len(lst)-2, -1, -1):
        postfix[i] = postfix[i+1] * lst[i]

    result = [1 for _ in lst]

    result[0] = postfix[1]
    result[-1] = prefix[-2]
    for i in range(1,len(lst)-1):
        result[i] = prefix[i-1] * postfix[i+1]

    return result

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [-10, 15, 7, 11, -3, 8]

assert(product_sum(l1) == [3628800,1814400,1209600,907200,725760,604800,518400,453600,403200,362880])
assert(product_sum(l2) == [-27720,18480,39600,25200,-92400,34650])