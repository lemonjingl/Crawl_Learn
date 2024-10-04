# Scrapy settings for baidufanyi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'baidufanyi'

SPIDER_MODULES = ['baidufanyi.spiders']
NEWSPIDER_MODULE = 'baidufanyi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baidufanyi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':' gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection':' keep-alive',
'Content-Length': '21',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'BIDUPSID=CE8C6E709313A41A0518DB276E42F71D; PSTM=1674197245; BAIDUID=CE8C6E709313A41A270A5DDD24BE9C6E:FG=1; BAIDUID_BFESS=CE8C6E709313A41A270A5DDD24BE9C6E:FG=1; ZFY=G:AM7nBhmbzW0B9KYPDV7cjzvjf7NEhyNLM5qibMJLY4:C; BAIDU_WISE_UID=wapp_1674389608767_772; __bid_n=185d965dcff851f73f4207; FPTOKEN=UBrlTA/1T9ww9CSQpV2ojzcxgQWmY60FZ24ucouZtiraaQFC4TZda0z1noisGzzyck7aQwfXa4FanKzHIytTLEnSMWWFR86+9SI7p10HOh3kSWRz7b+8pfAqmojNN6+xrgaGDXmdMm0jgbQ9xM2W0+7/UU+7LnSc1nzde+qcEXUyb1YxFqB1QhPbJOLCsi65dQsABGU/wvKK9fZrdwfDeZ5mn/ZWWf2L8nyj8MzQtcDObpFmxjLwXihCvuKgrjJztcIe61rMOU834CrFLMCXsfaWCzkLstJe/ye3D9IG/tbG/Ej7ahg/ZFIieCuAIJHvczYmActkPzwGaiVzqEb6k4U+XWK27/URJhC84NgywNNLqVUAQ+jyjfHF73Eh86/6pLRNyyCU+oW6g/i5vsjadhuLLiP+Bi1lwvpNTHsVTHXXGDyJRV4fXGAp/XpI4tEd|va1FYJzmQhX0wqhkZtTIzpdfuCcFNYFTMqTwbBpxo0U=|10|b409f3cb50412e0c86dc90479a07cdd5; RT="z=1&dm=baidu.com&si=83a6c7d4-ee6f-4263-bb4c-2a19e79e0cb7&ss=ld8uxc02&sl=3&tt=9yz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1942&ul=73tj&hd=73ve"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1674833443; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1674837079; ab_sr=1.0.1_MDJlYjUyZDVmODI5YWQxMjM5YTRjMWQ0NDNhZDNiOTgxZDY2Y2EwZGY1M2JjNTYxNWQyYmFiZjY3MTNlNTk1MjYwMGMzNWM3OTU5OWM3OWZmMTk0MWQxMzA0OGUxMDhjN2RjY2M4NDQxMGUzMjkyNzJiYjNmNjgwZTcxMTVhNjJjMzM5ZTJkNmQ2MDAwNGI1OTI3MmE0NjE5YjBjNmFhYg=='
,'Host': 'fanyi.baidu.com',
'Origin': 'https://fanyi.baidu.com',
'Referer': 'https://fanyi.baidu.com/',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Windows',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode':' cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'baidufanyi.middlewares.BaidufanyiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'baidufanyi.middlewares.BaidufanyiDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'baidufanyi.pipelines.BaidufanyiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5.优质采
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
