# Style 1

# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid Argument')

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))



#  Style 2

def spam(divideBy):
    return 42 / divideBy


try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
        print('Error: Invalid Argument')
