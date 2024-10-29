ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

# type cast of list into set
s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)


s1.intersection_update(s2)
s1.intersection_update(s3)
print("after intersaction")
print(s1)


# s1.union(s2)
# print(s1)
# s1.intersection_update(s2)
# print(s1)


# join using intersection
s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)

final_list = list(final_set)
print(final_list)