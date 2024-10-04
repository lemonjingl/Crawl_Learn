var a=1;
var b=100;
var c='hello'

console.log(a+b)

// var d,e,f=[7,8,9];
// console.log(f)


// 常量(定义之后不能修改)
const A=100;
console.log(A)

// var声明是局部作用域，如果不适用就是全局作用域
function  test(){
    var z=1;
    d=z;
}
test()
console.log(d)

// 变量提升：简单说就是在js执行的引擎会先进行预编译，预编译期间就会将变量声明与函数声明提升至其对应作用域的最顶端
// ES6之后，使用let和const关键字不存在提升
console.log(z) // undefined
var z=100;

// let 不允许重复声明同样的变量