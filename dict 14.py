dict={
    "L1":[78,54,65,89,11],
    "l2":[22,65,45,78,95],
    "l3":[32,4,89,45,2]
    }
print("\nBefore sorting:")
for i in dict.items():
    print(i)
print("\nAfter sorting:")
for a,b in dict.items():
    dict1={a:sorted(b)}
    print(dict1)
