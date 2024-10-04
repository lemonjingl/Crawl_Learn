// 基础类型 number string null undefined boolean symbol(独一无二)
// 引用类型 Object

var a=10;
var b=a;//实际值
a=20;
console.log(b,a)


var c={
    age:20
}
var d=c;//引用地址
c.age=100
console.log(d.age,c.age)

aa=100
cc={
    age:20
}

function test(aa,cc){
    aa=99
    cc.age=88
}
test(aa,cc)
console.log(aa,cc)