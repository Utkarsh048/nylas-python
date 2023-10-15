def combinations(arr, k):
    if k == 0:
        return [[]]
    if not arr:
        return []
    
    item = arr[0]
    rest = arr[1:]
    
    without_item = combinations(rest, k)
    with_item = combinations(rest, k - 1)
    for combo in with_item:
        combo.append(item)
    
    return without_item + with_item

# Test the combinations function
items = [1, 2, 3, 4, 5]
k = 3
result = combinations(items, k)
for combo in result:
    print(combo)
