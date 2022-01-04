def union(data1, data2):
    for data in data1:
        if data in data2:
            continue
        else:
            data2.append(data)


if __name__ == '__main__':
    arr_one = [1, 2, 3]
    arr_two = [2, 3, 4]
    union(arr_one, arr_two)
    print(arr_two)
