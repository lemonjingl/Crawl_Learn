'''
1.服务器反爬的原因：
    爬虫占总PV较高，浪费资源
    资源被批量抓走，丧失竞争力
    法律的灰色地带

2.服务器常反什么样的爬虫
    十分低级的应届毕业生
    十分低级的创业小公司
    失控小爬虫
    搜索引擎

3.反爬的三个方向
    基于身份识别进行反爬
    基于爬虫行为进行反爬
    基于数据加密进行反爬

4.ontariogenomics、基于身份识别进行反爬
    1.通过headers字段来反爬（headers中有很多字段，这些字段都有可能被对方服务器拿过来进行判断是否为爬虫）
        1.1通过User-Agent字段来反爬
        1.2通过referer字段或者是其他字段来反爬
        1.3通过cookie来反爬
    2.通过请求参数来反爬
        请求参数的获取方法有很多，向服务器发送请求，很多时候需要携带请求参数，通常服务器就可以通过检查请求参数是否正确来判断是否为爬虫
        2.1通过从html静态文件中获取请求参数（github登录数据）
            反爬原因：通过增加获取请求参数的难度进行反爬
            解决方法：仔细分析抓包得到的每一个包，搞清楚请求之间的联系，搞清楚请求参数的来源
        2.2通过发送请求获取请求数据
            反爬原因：通过增加获取请求参数的难度进行反爬
            解决方法：仔细分析抓包得到的每一个包，搞清楚请求之间的联系，搞清楚请求参数的来源
        2.3通过js生成请求参数
            反爬原因：js生成了请求参数
            解决方法：分析js，观察加密的实现过程，通过js2py获取js的执行结果，或者使用selenium来实现
        2.4通过验证码来反爬
            反爬原因：对方服务器通过弹出验证码强制验证用户浏览行为
            解决方法：打码平台或者是机器学习的方法识别验证码，其中打码平台廉价易用，更值得推荐

5.优质采、基于爬虫行为进行反爬
    1、基于请求频率或总请求数量
        1.1通过请求ip/账号单位时间内总请求数量进行反爬
            反爬原理：正常浏览器请求网站，速度不会太快，同一个ip/账号大量请求了对方服务器，有更大的可能性会被识别为爬虫
            解决方法：对应的请求购买高质量的ip的方式能够解决问题/购买多个账号
        1.2通过同一ip/账号之间的间隔进行反爬
            反爬原理：正常人操作浏览器浏览网站，请求之间的时间间隔是随机的，而爬虫前后两个请求之间时间间隔通常比较固定同时时间间隔较短，因此可以用来做反爬
            解决方法：请求之间进行随机等待，模拟真是用户操作，在添加时间间隔后，为了能够告诉获取数据，尽量是由代理池，如果是账号，则将账号请求之间设置随机休眠
        1.3通过对请求ip/账号每天请求次数设置阙值进行反爬
            反爬原理：正常的浏览行为，其一天的请求次数是有限的，通常超过某一个值，服务器就会拒绝响应
            解决方法：对应的通过购买高质量的ip的方法/多账号，同时设置请求间随机休眠
    2、根据爬取行为进行反爬，通常在爬取步骤上做分析
        2.1通过js实现跳转来反爬
            反爬原理：通过js实现跳转来反爬
            解决方法：多次抓包获取条状url，分析规律
        2.2通过陷阱获取爬虫ip（或者代理ip)，进行反爬
            反爬原理：在爬虫获取链接请求的过程中，爬虫会根据正则、xpath、css等方式进行后续链接的提取，此时服务器端可以设置一个陷阱url，会被提取规则获取，大师正常用户无法获取，这样就能有效区分爬虫和正常用户
            解决方法：完成爬虫的编写之后，使用代理批量爬取测试/仔细分析响应内容结果，找出页面中存在的陷阱
        2.3通过假数据反爬
            反爬原理：向返回的响应中添加假数据污染数据库，通常假数据不会被正常用户看到
            解决方法：长期运行，核对数据库中数据同实际页面中数据对应情况，如果存在问题/仔细分析响应内容
        2.4阻塞任务队列
            反爬原理：通过生产大量垃圾url，从而阻塞任务队列，降低爬虫的实际工作效率
            解决方法：观察运行过程中请求响应状态/仔细分析源码获取垃圾url生成规则，对UPL进行过滤
        2.5阻塞网络IO
            反爬原理：发送请求获取响应的过程实际就是下载的过程，在任务队列中混入一个大文件的url,当爬虫在进行该请求时将会占用网络IO，如果时多线程则会占用线程
            解决方法：观察爬虫运行状态/多线程对请求线程计时/发送请求线
        2.6运维平台综合审计
            反爬原理：通过运维平台进行综合管理，通常采用符合型反爬虫策略，多种手段同时使用
            解决方法：仔细观察分析，长期运行测试网站，检查数据采集速度，多方面处理

6.中国五矿集团采购信息.常见基于数据加密进行反爬
    1对响应中含有的数据进行特殊化处理
        1.1通过自定义字体来反爬
            反爬思路：使用自有字体文件
            解决思路：切换到手机版/解析字体文件进行翻译
        1.2通过css来反爬
            反爬思路：源码数据不为真正数据，需要通过css位移才能产生真正数据
            解决思路：计算css的偏移
        1.3通过js动态生产数据进行反爬
            反爬思路：通过js动态生成
            解决思路：解析关键js，获得数据生成流程，模拟生产数据
        1.4通过数据图片化反爬
            58同城短租（https://baise.58.com/duanzu/38018718834984x.shtml）
            解决思路：通过 使用图片解析引擎从图片中解析数据
        1.5通过编码格式进行反爬
            反爬原理：不使用默认编码格式，在获取响应之后通常爬虫使用utf-8格式进行解码，此时解码结果将会时乱码或者报错
            解决思路：根据源码进行多格式解码，或者真正的解码格式
            

'''