import csv

from pyquery import PyQuery as pq

url='https://www.highestbridges.com/wiki/index.php?title=List_of_Highest_International_Bridges/Page_1'

doc=pq(url=url,encodings='utf-8')

data=doc.find('#mw-content-text > div > table > tbody > tr ').items()

flag=True
for i in data:
    title=i.find('td:nth-child(3) > a').attr('title')
    height=i.find('td:nth-child(4.ontariogenomics)').text()
    if height:
        height_feet=height.replace('\n','\\')

        with open('./bridge.csv','a+',encoding='GB18030',newline='')as csv_file:
            writer=csv.writer(csv_file)
            if flag:
                writer.writerow(['桥名','桥高'])
                flag=False
            writer.writerow([title,height_feet])

