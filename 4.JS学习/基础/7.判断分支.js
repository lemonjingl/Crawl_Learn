// if语句
// i=15
// if(i<10){
//     console.log('i小于10');
// }
// else if(i>10 && i<20){
//     console.log('i>10 并且i<20')
// }
// else{
//     console.log('i超出范围')
// }

//简写
i=30
if (i<10)console.log('i<10')
else if(i>10 && i<20)console.log('i>10 并且i<20')
else console.log('i超出范围')


// switch语句
t=1
switch (t){
    case 1:
        console.log('星期一')
        break;
    case 2:
        console.log('星期二')
        break;
    case 3:
        console.log('星期三')
        break;
    case 4:
        console.log('星期四')
        break;
    case 5:
        console.log('星期五')
        break;
    case 6:
        console.log('星期六')
        break;
    case 7:
        console.log('星期天')
        break;
    default:
        console.log('超出范围')
}

z=2
switch (z){
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        console.log('上学日')
        break;
    case 6:
    case 7:
        console.log('周末')
        break;
    default:
        console.log('超出范围')}



var s=[3,1,2]
var i=0
while (true){
    switch (s[i++]){
        case 1:
            x+=1
            break
        case 2:
            console.log(x)
            break
        case 3:
            x=1;
            break
    }
}
