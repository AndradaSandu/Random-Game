# import random



# start = int(input("Enter the start for the interval: "))
# stop =  int(input("Enter the stop fot the interval: "))
# if start < stop:
#     for el in range(start, stop+1):
#         print (el)
# # try:
# #     for el in reversed(range(start, stop+1)):
# #         print(el)
# # except ValueError:
# #     print("oops")
#
# x = int(input("Enter the guess number: "))
# y = random.randint(start, stop+1)
# print(f'The random number is: {y}')
# if x == y:
#     print("It is corect. You are a genius!!")
# else:
#     print("It's incorect, try again!!")



lst = [2, 4, 5, 7, 8]

for i in range(len(lst)):
    for item in range(len(lst)):
        if i > item:
                print("max is:", lst[i])

