'''
1.2
门票的序列号必定是系统里总序列的子序列，请你核对门票的真实性。
从键盘接收两个字符串a 和b，请你判断字符串a 是否包含字符串b，是的话输出“Yes”，否则输出“No”。有多组测试用例，每个测试用例占一行，两个字符串之间用空格隔开。
例如：输入JavaStudy Java 则输出Yes     Student School 则输出 No
注意 ：判断后者是否存在与前者里面  请用循环完成

'''
a,b=input('请输入序列号:').split(' ')
if b in a:
    print('Yes')
else:
    print('No')
