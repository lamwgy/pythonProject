row = eval(input("请输入行个数: "))
col = eval(input("请输入列个数: "))


# 创建一个二维数组
def init():
    return [[None] * row] * col


# 遍历二维数组
def Print(arr):
    for i in range(len(arr)):
        print(arr[i])


if __name__ == '__main__':
    start_arr = init()
    Print(start_arr)
