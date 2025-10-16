# print("Sets in Python")
# set_one={'laptop','iphone','airpod','ipad','apple watch','apple TV'}
# print("Number of items in set_one are:",len(set_one))
# for item in set_one:
#     print(item,end=" ")

#clear(): remove all the items from set

# set_one.clear()
# print('\nAfter clear the number of items in set_one are:',len(set_one))
# for item in set_one:
#     print(item, end=" ")

# set_one={'laptop','iphone','airpod','ipad','appleWatch'}
# print("Number of items in set_one are:",len(set_one))
# for item in set_one:
#     print(item,end=" ")

# #set.remove(item):updates the set and removes item from set
# set_one.remove('appleWatch')
# print('\nAfter removing one item from set:',len(set_one))
# for item in set_one:
#     print(item,end= " ")

#UNION,INTERSECTION,DIFFERENCE
# set_one={'skintific','wardah','glad2glow','timephoria'}
# set_two={'maybelline','loreal','hadalabo','clarins','ysl'}

#UNION
# #s1.union(s2): Returns a new set with all items from both sets s1,s2.
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# unionset=set_one.union(set_two)
# print(f'Union of set_one and set_two contains: {len(unionset)} following items')
# print(unionset)


#INTERSECTION
# set_one={'skintific','wardah','glad2glow','timephoria','ysl'}
# set_two={'maybelline','loreal','hadalabo','clarins','ysl'}

# #s1.intersection(S2):Return set which contains only item in sets s1,s2
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# newset=set_one.intersection(set_two)
# print(f'intersection of set_one and set_two contains: {len(newset)} following items')
# print(newset)


# #DIFFERENCE
# set_one={'skintific','wardah','glad2glow','timephoria','ysl'}
# set_two={'maybelline','loreal','hadalabo','clarins','ysl','wardah,','glad2glow'}

# #s1.difference(S2):Return set which contains only item those are in s1 but not in s2..
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# newset=set_one.difference(set_two)
# print(f'difference of set_one and set_two contains: {len(newset)} following items')
# print(newset)