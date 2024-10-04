from fake_useragent import UserAgent

ua = UserAgent()
print(f'ie浏览器任意版本：{ua.ie}')  # 随机打印ie浏览器任意版本
print(f'ie浏览器任意版本：{ua.firefox}')  # 随机打印firefox浏览器任意版本
print(f'{ua.chrome}')  # 随机打印chrome浏览器任意版本
print(f'ie浏览器任意版本：{ua.random}')  # 随机打印任意厂家的浏览器