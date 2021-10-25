# 1

#a = [1, 2, 3, 4, "a"]

# max = max(a)
# min = min(a)
#
# index_1 = a.index(max)
# index_2 = a.index(min)
# try:
#     a[index_1]=min
#     b[index_2]=max
# except NameError:
#     print("error: NameError")

# 2

# cube = int(input())
# day = input()
# day_off = ["saturday", "sunday"]
# try:
#     if cube % 2 == 0:
#         choco = int(input())
#         if day not in day_off:
#             if choco - 3 >= 2:
#                 print("Go to Paul")
#             else:
#                 print("Go home")
#         else:
#             print("go to Paul")
#     else:
#         print("stay home")
# except ValueError:
#     print("error: ValueError")

d = {'foo': 100, 'bar': 200, 'baz': 300}

print(d['bar':'baz'])