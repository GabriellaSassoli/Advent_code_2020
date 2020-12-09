file = open("day_3.txt", "r")
read_file = file.read()

splitted_lines = read_file.split("\n")

board = [list(s) for s in splitted_lines]
width = len(board[0])
print(width)
height = len(board)
print(height)
y = 0
x = 0
trees = 0
print(board[31][0])
while( y < height -1):
    if x == (width - 3):
        print("index - 3")
        x = 0
        y += 1
    elif (x == (width - 2)):
        print("index - 2")
        x = 1
        y +=1
    elif x == (width - 1):
        print("index - 1")
        x = 2
        y += 1
    else:
        x += 3
        y += 1
    print(x,y)
    if x == width:
        print("THis shouldn't happen")
    if y == height:
        print("THis shouldn't happen")
    if board[y][x] == '#':
        trees += 1
        print(trees)
print(trees)



# class cell:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Field:
#
#     def __init__(self, splitted_lines):
#         self.board = [list(s) for s in splitted_lines]
#         self.width = len(self.board[0])
#         self.height = len(self.board)
#
#     def move(self):
#         y = 0
#         x = 0
#         trees = 0
#         while( y < board):
#             if x == (width - 3):
#                 print(x)
#                 x = 1
#                 y += 1
#             elif (x == (width - 2)):
#                 x = 2
#                 y +=1
#             # elif x == (width - 1):
#             #     x = 3
#             #     y += 1
#             else:
#                 x += 3
#                 y += 1
#             if self.board(x,y) == '#':
#                 trees += 1
#
#         return trees;

