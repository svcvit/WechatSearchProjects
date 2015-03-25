递归抓取微信搜索结果
使用Scrapy方法 或者 使用requests+BeautifulSoup


使用Scrapy方法：
	将querystring替换为你要查询的单词
	type可以选择
	i的range范围可以调整，对应查询的搜索结果页面数目
#############################################################################################
'''微信搜索程序'''
name = "wechat"

start_urls = []
querystring = u"清华"
type = 2 # 2-文章，1-微信号
for i in range(1, 5, 1):
	start_urls.append("http://weixin.sogou.com/weixin?type=%d&query=%s&page=%d" % (type, querystring, i))
# print start_urls



