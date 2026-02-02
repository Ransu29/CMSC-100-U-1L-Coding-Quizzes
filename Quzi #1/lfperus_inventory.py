#LANCE JOSEPH F. PERUS
#CMSC 100 U-1L CODING QUIZ #1

slots = int(input())


items = {}

for i in range(slots):
    curr = input().split()
    item = curr[0]
    quantity = int(curr[1])
    
    if item in items:
        items[item] += quantity
    else:
        items[item] = quantity

for k,v in items.items():
    slot = 1
    while v > 64:
        slot += 1
        v -= 64
    print(k, slot)
