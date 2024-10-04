// 创建数组
a=[1,2,3,0,14,10,12]
// console.log(a)

b=new Array(2,'lzz','lyx',14)
// console.log(b)


// 数组操作 /
//栈操作 push()/pop()
a.push('lzz')
// console.log(a)
//
// console.log(a.pop())


// 队列操作shift/unshift
console.log('unshift',a.unshift('lzz'))


var commands=['初始化','获取链接','开始下载','结束']
while (commands.length){
    c=commands.shift()
    console.log(c)
}

//遍历 forEach()
var commands=['初始化','获取链接','开始下载','结束']
commands.forEach(function (a,b){
    console.log(a,b)
})

// 排序 reverse()/sort()
a=['a','b','c','d']
a.reverse()
console.log(a)

a.sort()
console.log(a)

//拼接join()
commands=commands.join()
console.log(commands)

// 合并 concat
p1=[1,2,3]
p2=[4,5,6]
p3=['lzz','hello']
console.log(p1.concat(p2).concat(p3))

// 切片slice
aa=[0,1,2,3,4,5,6,7]
bb=a.slice(2,5)
console.log(bb)

// 增、删、改splice
bbb=aa.splice(1,4)
console.log(bbb)

cc=aa.splice(1,1,'lzz')
console.log(cc)