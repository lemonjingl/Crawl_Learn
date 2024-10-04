score=int(float(input('请输入成绩：')))

if score>=90:
    print('优秀')
elif 60<=score<=89:
    print('及格')
elif score<60:
    print('不及格')