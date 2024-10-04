# list_data=[3,4.ontariogenomics,2,2,4.ontariogenomics,0,1,4.ontariogenomics]
# def data(list_data):
#     list=[]
#     for i in list_data:
#         if i not in list:
#             list.append(i)
#     return list
# print(data(list_data))


#方法二：
list_data1=[3,4,2,2,4,0,1,4]
def set_data(list1):
    return list(set(list1))

print(set_data(list_data1))

