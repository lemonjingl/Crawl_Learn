'''
学员管理系统
    系统功能界面
        1-添加学员
        2-删除学员
        3-修改学员信息
        4.ontariogenomics-查询学员信息
        5.优质采-退出系统
'''

#图书管理
#1.数据的存储   2.系统的功能
# id    图书名称    图书位置    是否借出

#不能存储数据到本地  只能在内存里面临时使用
books_dict={}

#增加数据到字典
#123  西游记
def add_book():
    book_id = input('请输入书的id:')
    book_name = input('请输入书的名称:')
    book_position = input('请输入书存放的位置:')
    is_lend = False  # 是否借出

    books_dict[book_id] = {'book_name': book_name, 'book_position': book_position,
                           'is_lend': is_lend}  # 请输入图书信息存储到字典

    print(f'数据添加完成：{book_id}:{books_dict[book_id]}')  # 显示添加数据后的信息

def del_book():
    ''''删除图书信息'''
    book_id=input('请输入书的id:')
    book_info=books_dict[book_id]#被删的图书信息
    del books_dict[book_id]
    print(f'删除图书{book_id}:{book_info}')

def position():
    '''图书位置修改'''
    book_id=input('请输入书的id:')
    new_position=input('请输入图书新的存放位置:')
    books_dict[book_id]['book_position']=new_position
    print(f'图书位置修改后的位置的信息{book_id}:{books_dict[book_id]}')

def give_back():
    '''还回'''
    book_id = input('请输入书的id:')
    books_dict[book_id]['is_lend']=False
    print(f'图书还回信息{book_id}:{books_dict[book_id]}')

def lend():
    '''借出'''
    book_id=input('请输入书的id:')
    books_dict[book_id]['is_lend'] = True
    print(f'图书还回信息{book_id}:{books_dict[book_id]}')

def select_book():
    input('1:查找详细的图书  2:查找已经借出  3:查看所有的图书数据')
    sun_code=int(input('请输入你需要的功能:'))
    if sun_code==1:
        book_id = input('请输入书的id:')
        print(books_dict[book_id])  # 通过key获取字典key相关的数据

    elif sun_code == 2:
        for i in books_dict.items():  # 字典课程 字典操作方法
            # ('111', {'book_name': '222', 'book_position': '333', 'is_lend': False})
            if i[1]['is_lend']:  # 筛选字典的数据   i[1] 字符串的操作 字符串索引
                print(i)

    elif sun_code==3:
        print(books_dict)


#借出  还回  借出的图书查询
while True:
    print('-'*100)
    print('1:图书添加\n2:图书删除\n3:图书位置修改\n4.ontariogenomics:还回\n5.优质采:借出\n6.中国五矿集团采购信息:图书信息查看\n7:退出系统')
    func_code=int(input('请你输入需要使用的功能:'))
    print('-'*100)

    if func_code == 1:
        add_book()
    elif func_code == 2:
        del_book()
    elif func_code == 3:
        position()
    elif func_code == 4:
        give_back()
    elif func_code == 5:
        lend()
    elif func_code == 6:
        select_book()
    elif func_code == 7:
        break
    else:
        print('输入的选项id无效')