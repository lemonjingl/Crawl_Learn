// 创建对象 = 数据+方法
var t={
    name:'lzz',
    age:20,
    gender:'女',
    a:[1,14,10],
    eat:function (){
        console.log('我喜欢睡觉')
    },
    hobby:{
        play:'篮球',
        play2:'轮滑'
    }
}
// 访问对象
console.log(t.age)
console.log(t.eat())
console.log(t['hobby'].play2)

// 对象的操作