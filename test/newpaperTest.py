from newspaper import Article

if __name__=='__main__':
    import newspaper
    from newspaper import Article

    # 这里的url可以填写你需要爬取的网址
    url = 'https://www.suredian.com/'
    news = Article(url, language='zh')
    news.download()
    news.parse()

    print(news.url)
    # news.url为获取网址的url
    print(news.text)
    # news.text为获取页面的所有text文字
    print(news.title)
    # news.title为获取页面的所有标题
#    print(news.html)
    # news.html为获取页面的所有源码
#    print(news.authors)
#    print(news.top_image)
#    print(news.movies)
#    print(news.keywords)
#    print(news.summary)
#    print(news.images)
#    print(news.imgs)

