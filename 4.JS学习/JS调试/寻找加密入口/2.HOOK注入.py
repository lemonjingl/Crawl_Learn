'''
HOOK注入：
    1.注入原理
        替换原函数执行流程，从而拦截原函数的一些参数名和返回值
        Object.defineProperty()方法会直接再一个对象上定义一个心得属性，或者修改一个对象的现有属性，并返回此对象。

    2.注入工具
        （1）浏览器手动注入
            只能Hook全局变量
            找到第一个js加载文件位置打断点
            事件监听load->on load打断点
        （2）油猴注入
        （3）fiddler注入

    3.常用Hook方法
        JSON.stringify
        JSON.parse
        Hook eval
'''
