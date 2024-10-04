function test(a){
    return a
}
var b=test(1)
console.log(b)

//匿名函数
var aa=function (){
    console.log('逆向')
}
aa()

aaa=[
    function (){console.log('初始化')},
    function (){console.log('点击登录')},
    function (){console.log('开始加密')},
    function (){console.log('发送数据')}
]
// a.push(function (){console.log('接收数据')})
for (i=0;i<aaa.length;i++){
    aaa[i]()
}