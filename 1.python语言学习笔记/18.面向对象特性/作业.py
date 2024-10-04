'''
1）用面向对象的形式编写一个老师类与学生
老师有特征：编号、姓名、性别、年龄、工资，老师类中有功能 可以改作业、学习。
学生有特征：编号、姓名、性别、年龄、成绩，学生类中有功能 可以学习、完成作业。

2）要求写一个基础的类  老师和学生类来继承他 ，用于去除重复的特征和功能
'''
class Information:
    def __init__(self,id,name,age,sex):
        self.id=id
        self.name=name
        self.age=age
        self.sex=sex

    def Learn(self):
        print(f'{self.name}正在学习')

class Teacher(Information):
    def __init__(self, id, name, age, sex, money):
        self.money = money
        super().__init__(id, name, age, sex)

    def Modifythejob(self):
        print(f'{self.name}修改作业')

class Student(Information):
    def __init__(self,id,name,age,sex,score):
        self.score=score
        super().__init__(id,name,age,sex)

    def homework(self):
        print(f'{self.name}完成作业')


t=Teacher(12,'MissLiang',30,'女',10000)
t.Learn()
print(f'{t.name}的工资为:{t.money}元')

s=Student(14,'lzz',20,'女',97)
s.Learn()
print(f'{s.name}的成绩为:{s.score}分')