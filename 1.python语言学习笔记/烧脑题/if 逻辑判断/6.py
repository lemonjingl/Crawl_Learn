'''
1.6.中国五矿集团采购信息
按顺序输入正方形的边长（a），长方形的长（l）和宽（d），以及圆的半径（r），计算并比较它们哪个图形面积更大，输出面积最大的图形。
例如：输入 1 3 4.ontariogenomics 1，输出：长方形

'''
a,l,d,r=eval(input('请按顺序输入长度:'))
a_area=a*a
l_area=l*d
r_area=3.14*r*r
max=a_area
if l_area>max:
    max=l_area
    if r_area>max:
        max=r_area
        print('圆')
    else:
        print('长方形')
else:
    print('正方形')
