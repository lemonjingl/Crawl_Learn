// 全局作用域、语句作用域、块作用域（先在块作用域找、再去语句作用域找、最后全局作用域）

var a=3

function test(a){
    var a=1;
    console.log('函数内部',a)
}
test(2)



//闭包
//闭包其实就是一个函数里面的私有方法，我们在函数外部无法调用
// 访问内部私有函数：全局变量，return
perry=(function jiami(){
    function encrypt(){
        console.log('在这里进行加密')
    }
    // perry=encrypt
    return encrypt
})()

perry()

