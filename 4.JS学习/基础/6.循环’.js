// for(i=0;i<10;i++){
//     console.log(i,'循环体')
// }

//以j++作为截止条件
// for (i=0,j=0;i<10,j<15;i++,j++){
//     console.log(i,j)
// }

// for、in
a=['a','perry',1,'逆向']
for (i in a){
    if (i==1){
        continue
    }
    console.log(a[i])
}

//while/do、while

i=0
while(i<10){
    console.log(i)
    i++
}

i=100
do{
    console.log(i);
    i++;
}
while(i<10)
