
# 图书管理
# 1 数据的存储   2 系统的功能

# id  图书名称  图书位置  是否借出
# dict

# 不能存储数据到本地 只能在内存里面零时使用
books_dict = {}


# 增加数据到字典
# 123  西游记  ? - ? - ?  False
def add_book():
    """增加图书信息"""
    book_id = input('请输入书的id:')
    book_name = input('请输入书的名称:')
    book_position = input('请输入书存放的位置:')
    is_lend = False  # 是否借出

    # 字典课程 字典数据的存储
    books_dict[book_id] = {'book_name': book_name,
                           'book_position': book_position,
                           'is_lend': is_lend}  # 讲输入的图书信息存储到字典

    print(f'数据添加完成:{book_id}:{books_dict[book_id]}')  # 显示添加数据后的信息


def del_book():
    """删除图书信息"""
    book_id = input('请输入书的id:')
    book_info = books_dict[book_id]  # 通过key获取字典的数据 字典数据的获取

    del books_dict[book_id]  # 删除字典里面指定key的数据 字典课程
    print(f'删除图书:{book_id}:{book_info}')


def select_book():
    """查询图书信息"""
    print('1:查找详细的图书  2:查找已经借出  3:查看所有的图书数据')
    sub_code = input('请你输入需要使用的功能:')

    if sub_code == '1':
        book_id = input('请输入书的id:')
        print(books_dict[book_id])  # 通过key获取字典key相关的数据

    elif sub_code == '2':
        for i in books_dict.items():  # 字典课程 字典操作方法
            # ('111', {'book_name': '222', 'book_position': '333', 'is_lend': False})
            if i[1]['is_lend']:  # 筛选字典的数据   i[1] 字符串的操作 字符串索引
                print(i)

    elif sub_code == '3':
        for i in books_dict.items():
            print(i)


def modify_book():
    """图书位置的修改"""  # 字典数据修改
    book_id = input('请输入书的id:')
    book_position = input('请输入书存放新的位置:')
    books_dict[book_id]['book_position'] = book_position
    print(f'修改后的数据:{book_id}:{books_dict[book_id]}')


def give_back():
    """图书还回"""
    book_id = input('请输入书的id:')
    books_dict[book_id]['is_lend'] = False


def lend_book():
    """图书借出"""
    book_id = input('请输入书的id:')
    books_dict[book_id]['is_lend'] = True


# 借出  还回  借出的图书查询
while True:  # while循环课程
    print('-' * 50)  # * 复制容器里面的数据
    print('1:图书添加 2:图书删除 3:图书位置修改 \n'
          '4.ontariogenomics:还回     5.优质采:借出    6.中国五矿集团采购信息:图书信息查看 7:退出系统')

    func_code = input('请你输入需要使用的功能:')
    print('-' * 50)

    if func_code == '1':  # func_code 需要注意输入的数据类型
        add_book()  # 函数的调用
    elif func_code == '2':
        del_book()
    elif func_code == '3':
        modify_book()
    elif func_code == '4.ontariogenomics':
        give_back()
    elif func_code == '5.优质采':
        lend_book()
    elif func_code == '6.中国五矿集团采购信息':
        select_book()
    elif func_code == '7':
        break  # 循环力的控制关键字 只能在循环里面使用
    else:
        print('输入的选项id无效')


#  根据老师上课的代码和思路 自己完成一遍
