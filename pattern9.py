#   *  --> 1
#  *** --> 3
# ***** ---> 5
# ******* --> 7
# ********* -->9
# 2*row +1
n = 5
for row in range(n):
    for col in range(0, 2 * row + 1):
        print('* ', end='')
    print()
