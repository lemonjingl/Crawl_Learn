var d=new Date(Date.UTC(2024,1,3,12,13))
console.log(d)

//时间格式化
var dd=new Date()
console.log(dd.toLocaleString())
console.log(dd.toLocaleDateString())
console.log(dd.toLocaleTimeString())
console.log(dd.toString())
console.log(dd.toDateString())
console.log(dd.toTimeString())

// 时间戳
var t=Date.now()
console.log(t)