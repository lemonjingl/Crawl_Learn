#1-300（包含1-300）的奇数进行累加，但是逢7的倍数跳过不加进来
i=1
sum=0
while i<=300 :
    if i%2!=0 and i%7!=0:
        sum+=i
    i+=1
print(sum)