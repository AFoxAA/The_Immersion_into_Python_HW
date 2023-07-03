for i in range(2, 11):
    for j in range(2, 6):
        result = i * j
        print(f'{j} x {i} = {result}\t', end="")
    print()

print()

for i in range(2, 11):
    for j in range(6, 10):
        result = i * j
        print(f'{j} x {i} = {result}\t', end="")
    print()


# # РЕШЕНИЕ ЧЕРЕЗ ФУНКЦИЮ

# TABLE_START = 2
# TABLE_END = 11
# TABLE_END_6 = 6
# TABLE_END_10 = 10


# def multiplication_table(start, end):
#     for i in range(TABLE_START, TABLE_END):
#         for j in range(start, end):
#             result = i * j
#             print(f'{j} x {i} = {result}\t', end="")
#         print()

# multiplication_table(TABLE_START, TABLE_END_6)
# print()
# multiplication_table(TABLE_END_6, TABLE_END_10)
