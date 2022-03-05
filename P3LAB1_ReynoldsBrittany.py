color_1 = int(input())
color_2 = int(input())
color_3 = int(input())
gray = 50

if color_1 >= 50 and not color_1 >= 255:
    color_1 = color_1 - gray

if color_2 >= 50 and not color_2 >= 255:
    color_2 = color_2 - gray

if color_3 >= 50 and not color_3 >= 255:
    color_3 = color_3 - gray

print(color_1, color_2, color_3)