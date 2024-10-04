// this指向

// 1.浏览器环境（全局（window）、方法（window）、对象（指向对象本身）
//浏览器的全局变量window包括控制浏览器的方法和属性
//window.innerHeight查看窗口高度
//this谁引用它它就指向谁

// 2.NodeJS环境（全局（空对象）、方法（global）、对象（指向对象本身））
name='perry'
console.log(global.name)
console.log(global.name===name)

console.log(this)



function test(){
    console.log(this)
}
test()

// 对象
var t={
    name:'perry',
    test1:function (){
        console.log(this)
    }
}

t.test1()