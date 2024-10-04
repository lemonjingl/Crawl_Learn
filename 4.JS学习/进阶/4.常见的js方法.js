// 1.call和apply方法（改变this指向）
// function Teacher(name,age,major){
//     this.name=name;
//     this.age=age;
//     this.major=major;
//     this.teach=function (h1,h2){
//         console.log(`${this.name}教${this.major},喜欢${h1},${h2}`)
//     }
//     this.sport=function (hobby){
//         this.hobby=hobby
//         console.log('sport是构造器产生的')
//     }
// }
// lzz=new Teacher('lzz',20,'python')
// lily=new Teacher('lily',19,'java')
// lzz.teach('游戏','打篮球')
// lzz.teach.call(lily,'游戏','化妆')
// lily.teach.apply(lzz,['打篮球','轮滑'])

// function test(){
//     console.log('hello')
// }
// test.call(this)
// test.apply('99')



// 2.箭头函数（基本用法、简写、this指向）
// a=()=>{
//     console.log('逆向简单个屁')
// }
// a()
//
// b=(a,b)=>{
//     console.log(a+b)
// }
// b(1,2)
//
// //一个参数可以省略一个括号
// c=c=>{
//     console.log(c)
// }
// c(14)
// //去掉花括号
// d=(a,b)=>a+b;
// console.log(d(14,12))
//
// //this指向
// perry={
//     num:22,
//     f1:function (){
//         console.log(this.num)
//     },
//     f2:()=>{
//         console.log(this.num)
//     }
// }
// perry.f1()
// perry.f2()


// 3.定时器（setTimeout、setInterval）
x=setTimeout(function (){console.log('开始捣乱了')},2000)
x
//清除
clearTimeout(x)

y=setInterval(function (){console.log('开始发疯了')},3000)
y
clearInterval(6)

//无限debugger
z=setInterval(function (){
    debugger;
},3000)


// 4.eval（基本功能、还原eval内容）
s='console.log("逆向真简单")'
eval(s)

// a1=1;
// b1=2;
// z1=a1+b1;
// console.log(z1)将其进行eval加密
eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)d[e(c)]=k[c]||e(c);k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('2=0;3=1;6=2+3;4.5(6)',62,7,'1|2|a1|b1|console|log|z1'.split('|'),0,{}))