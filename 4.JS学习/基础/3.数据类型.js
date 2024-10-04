// 查看变量类型
// undefiend和null
// 布尔Boolean
// 数字Number
// 字符串

// 查看变量类型
var a=100;
console.log(typeof(a));

var b;
console.log(typeof (b));

var c=null;
console.log(typeof (c));

var d='lzz';
console.log(typeof (d))

// undefiend和null

// undefiend 同var/let声明，但不赋值；null 是空对象指针，类型是object
// 相同点：某个变量赋值为undefiend或null,实际上没有太大的差别，两者都是表示某个变量的值为”空“；if语句中，都会被自动转成false
// 区别：undefiend表示一个变量初始化状态值，而null则表示一个变量被人为的设置为空对象，而不是原始状态；
// 在实际使用过程中，不需要对一个变量显式赋值undefined，当需要释放一个对象时，直接赋值为null即可。让一个变量为null,直接给该变量赋值为null即可。


// 布尔Boolean

// 只有true和false，小写
// 字符串非空为true,反之为false
// 数字非0为true，
// 对象非null为true
// undefined为false

var aa='',bb='js'
console.log(Boolean(aa),Boolean(bb))
var cc=0,dd=-1;
console.log(Boolean(cc),Boolean(dd))

// 数字Number
//
// 数值范围最小Number.MIN_VALUE/最大Number.MAX_VALUE;Infinity无穷，比如1/0 （判断一个数字是不是可以表示的，使用isFinite()
// NaN 错误捕捉
// 数值转化 转数字Number()/转整形parseInt()/转浮点parseFloat()
var min_value=Number.MIN_VALUE
var max_value=Number.MAX_VALUE
console.log(min_value,max_value)

var aaa=1/0 // 输出无穷大
console.log(aaa)
//判断一个数字是不是可以表示的，使用isFinite()
console.log(isFinite(aaa))

var bbb='js',ccc='1',ddd='3.14';
console.log(parseInt(ccc),parseFloat(ddd))

// 字符串
//toString()转成字符串类型
// 字符串操作：截取字符串（substr/substring）、切割（split）、查找位置（indexOf/lastindex）、取长度（length）
// 改变大小写（toLowerCase()/toUpperCase()）
// 取字符：charAT()/charCodeAt()
var aaaa='hello',bbbb='World',cccc='你好';
console.log(aaaa+bbbb+cccc)

console.log(aaaa.substr(1,3))