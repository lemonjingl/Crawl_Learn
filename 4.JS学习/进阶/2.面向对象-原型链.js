//1.构造器
function Teacher(name,age,major){
    this.name=name;
    this.age=age;
    this.major=major;
    this.__proto__.abc=20;
    this.teach=function (){
        console.log(`${this.name}教${this.major}`)
    }
    this.sport=function (hobby){
        this.hobby=hobby
        console.log('sport是构造器产生的')
    }
}
//2.原型对象
//prototype在Teacher的原型上添加东西
Teacher.prototype.sport=function (hobby){
    this.hobby=hobby
    console.log(`${this.name}喜欢${this.hobby}`)
}

perry=new Teacher('lzz',20,'python')
lily=new Teacher('lily',19,'java')

perry.teach()
lily.sport('游泳')


//3.原型链
//perry.constructor查看perry的构造器
//Teacher.prototype查看Teacher的原型对象
// perry.__proto__ 指向原型对象
//Teacher.prototype.__proto__ 指向Object
//Teacher.prototype.__proto__.__proto__ 指向null

// perry.hasOwnProperty('name')看perry中是否有name属性


//4.this指向