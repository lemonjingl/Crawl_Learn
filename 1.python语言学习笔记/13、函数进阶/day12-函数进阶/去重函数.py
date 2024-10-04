l = [1, 1, 1, 3, 2, 2, 2]
l1 = [1, 1, 3, 2, 2, 2]


def my_set(list_object):
    new_lsit = []
    for i in list_object:
        if i not in new_lsit:
            new_lsit.append(i)
    return new_lsit


print(my_set(l))


# def my_set(list_object):  # 参数？ 参数是让函数变得更加灵活
#     return list(set(list_object))
#
# data = my_set(l)
# print(data)
# print(my_set(l1))
