import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#quanzhan
def getUrl():
    # 实现无可视化界面得操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/home?tab=top')
    driver.implicitly_wait(5)
    result=[]
    for i in range(1,11):
        xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a'
        el = driver.find_element(By.XPATH,xpath)
        new_url = el.get_attribute("href")
        title=el.get_attribute('title')
        result.append(str(i)+'\n'+title+'\n'+new_url)
        #result.append(str(i)+'\n'+title+'\n')
    driver.quit()
    text = '\n'.join(result)
    return "全天热点:"+'\n'+text

def get36krUrl():
    # 实现无可视化界面得操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=36kr')
    driver.implicitly_wait(5)
    result=[]
    for i in range(1,6):
        #xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a'
        xpath='//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div/a'
        el = driver.find_element(By.XPATH,xpath)
        new_url = el.get_attribute("href")
        title=el.get_attribute('title')
        result.append(str(i)+'\n'+title+'\n'+new_url)
        #result.append(str(i)+'\n'+title+'\n')
    driver.quit()
    text = '\n'.join(result)
    return "36氪:"+'\n'+text

def getXueqiuUrl():
    # 实现无可视化界面得操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=xueqiu')
    driver.implicitly_wait(5)
    result=[]
    for i in range(1,6):
        #xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath='//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div/div[2]/a'
        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH,xpath)
        new_url = el.get_attribute("href")
        xpath_title=xpath+'/div/p'
        title= driver.find_element(By.XPATH, xpath_title).text
        #title=el.text
        result.append(str(i)+'\n'+title+'\n'+new_url)
        #result.append(str(i)+'\n'+title+'\n')
    driver.quit()
    text = '\n'.join(result)
    return "雪球:"+'\n'+text


def getZhihuUrl():
    # 实现无可视化界面得操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=zhihu')
    driver.implicitly_wait(5)
    result=[]
    for i in range(1,6):
        #xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath='//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/a'
        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH,xpath)
        new_url = el.get_attribute("href")
        title=el.get_attribute('title')
        result.append(str(i)+'\n'+title+'\n'+new_url)
    driver.quit()
    text = '\n'.join(result)
    return "知乎:"+'\n'+text


def getHuxiuUrl():
    # 实现无可视化界面得操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=huxiu')
    driver.implicitly_wait(5)
    result=[]
    for i in range(1,6):
        #xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath='//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/a'
        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH,xpath)
        new_url = el.get_attribute("href")
        title=el.get_attribute('title')
        result.append(str(i)+'\n'+title+'\n'+new_url)
    driver.quit()
    text = '\n'.join(result)
    return "虎嗅:"+'\n'+text

def getTemplate(url,name):
    # 实现无可视化界面得操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get(url)
    driver.implicitly_wait(5)
    result=[]
    for i in range(1,6):
        #xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath='//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/a'
        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH,xpath)
        new_url = el.get_attribute("href")
        title=el.get_attribute('title')
        result.append(str(i)+'\n'+title+'\n'+new_url)
    driver.quit()
    text = '\n'.join(result)
    return name+':'+'\n'+text

def getPengpaiUrl():
    return getTemplate('https://rebang.today/?tab=thepaper',"澎湃")

def getAifanUrl():
    return getTemplate('https://rebang.today/?tab=ifanr',"爱范儿")

def getPojieUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=52pojie')
    driver.implicitly_wait(5)
    result = []
    for i in range(1, 6):
        # xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath = '/ html / body / div[1] / div / div[2] / div[2] / main / div / div[2] / ul / li['+str(i)+'] / div[1] / a'

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH, xpath)
        new_url = el.get_attribute("href")
        title = el.text
        result.append(str(i) + '\n' + title + '\n' + new_url)
    driver.quit()
    text = '\n'.join(result)
    return '吾爱破解' + ':' + '\n' + text

def getGuanfengwangUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=guancha-user')
    driver.implicitly_wait(5)
    result = []
    for i in range(1, 6):
        # xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath = '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div/a'

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH, xpath)
        new_url = el.get_attribute("href")
        title = el.get_attribute("title")
        result.append(str(i) + '\n' + title + '\n' + new_url)
    driver.quit()
    text = '\n'.join(result)
    return "观风网" + ':' + '\n' + text
    #return getTemplate('https://rebang.today/?tab=guancha-user',"观风网")

def getDongfangCaifuUrl():
    # 实现无可视化界面得操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=eastmoney')
    driver.implicitly_wait(5)
    result=[]
    for i in range(1,6):
        #xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath='//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div/div[2]/a'
        #xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH,xpath)
        new_url = el.get_attribute("href")
        xpath_title=xpath+'/div/p'
        title= driver.find_element(By.XPATH, xpath_title).text
        #title=el.text
        result.append(str(i)+'\n'+title+'\n'+new_url)
        #result.append(str(i)+'\n'+title+'\n')
    driver.quit()
    text = '\n'.join(result)
    return "东方财富:"+'\n'+text

def getLandianUrl():
    return getTemplate('https://rebang.today/?tab=landian', "蓝点网")

def getXiaozhongUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=appinn')
    driver.implicitly_wait(5)
    result = []
    for i in range(1, 6):
        # xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath = '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div/a'

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH, xpath)
        new_url = el.get_attribute("href")
        title = el.get_attribute("title")
        result.append(str(i) + '\n' + title + '\n' + new_url)
    driver.quit()
    text = '\n'.join(result)
    return "小众软件" + ':' + '\n' + text
    #return getTemplate('https://rebang.today/?tab=appinn', "小众软件")

def getFandouXianTuUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=apprcn')
    driver.implicitly_wait(5)
    result = []
    for i in range(1, 6):
        # xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath = '//*[@id="home-body"]/main/div/div[2]/ul/li[' + str(i) + ']/div/a'

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH, xpath)
        new_url = el.get_attribute("href")
        title = el.get_attribute("title")
        result.append(str(i) + '\n' + title + '\n' + new_url)
    driver.quit()
    text = '\n'.join(result)
    return "反斗限兔" + ':' + '\n' + text
    #return getTemplate('https://rebang.today/?tab=apprcn', "反斗限兔")


def getJuejinUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=juejin')
    driver.implicitly_wait(5)
    result = []
    for i in range(1, 6):
        # xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath = '//*[@id="home-body"]/main/div/div[2]/ul/li[' + str(i) + ']/div[1]/div[2]/a'
        el = driver.find_element(By.XPATH,xpath)
        new_url = el.get_attribute("href")
        xpath_title=xpath+'/div/p'
        title= driver.find_element(By.XPATH, xpath_title).text
        #title=el.text
        result.append(str(i)+'\n'+title+'\n'+new_url)
    driver.quit()
    text = '\n'.join(result)
    return "掘金" + ':' + '\n' + text
    #return getTemplate('https://rebang.today/?tab=juejin', "掘金")

def getJishuUrl():
    return getTemplate('https://rebang.today/?tab=journal-tech', "技术期刊")

def getGithubUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=github')
    driver.implicitly_wait(5)
    result = []
    for i in range(1, 6):
        # xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath = '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div/p/a'

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH, xpath)
        new_url = el.get_attribute("href")
        title = el.text
        result.append(str(i) + '\n' + title + '\n' + new_url)
    driver.quit()
    text = '\n'.join(result)
    return "Github" + ':' + '\n' + text
    #return getTemplate('https://rebang.today/?tab=github', "Github")

def getITUrl():
    return getTemplate('https://rebang.today/?tab=ithome',"IT之家")

def getShaoshupaiUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://rebang.today/?tab=sspai')
    driver.implicitly_wait(5)
    result = []
    for i in range(1, 6):
        # xpath= '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a';

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[1]/div/div[2]/a'
        xpath = '//*[@id="home-body"]/main/div/div[2]/ul/li[' + str(i) + ']/div/a'

        # xpath='//*[@id="home-body"]/main/div/div[2]/div/div/div[1]/div/ul/li[2]/div/div[2]/a'
        el = driver.find_element(By.XPATH, xpath)
        new_url = el.get_attribute("href")
        title = el.get_attribute("title")
        result.append(str(i) + '\n' + title + '\n' + new_url)
    driver.quit()
    text = '\n'.join(result)
    return "少数派" + ':' + '\n' + text
    #return getTemplate('https://rebang.today/?tab=sspai',"少数派")

def getOpOnlineUrl():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Edge(chrome_options)
    # 访问url
    driver.get('https://optimization-online.org/repository/')
    driver.implicitly_wait(5)
    result = []
    el = driver.find_element(By.TAG_NAME,'a')
    return el.text

if __name__=="__main__":
    #print(getUrl())
#     print(getZhihuUrl())
#     print(getITUrl())
#     print(getShaoshupaiUrl())
#    print(get36krUrl())
#    print(getXueqiuUrl())
#    print(getHuxiuUrl())
#    print(getPengpaiUrl())
#    print(getAifanUrl())
#    print(getPojieUrl())
#    print(getGuanfengwangUrl())
#    print(getDongfangCaifuUrl())
    #print(getLandianUrl())
    #print(getXiaozhongUrl())
#    print(getFandouXianTuUrl())
#   print(getJuejinUrl())
#    print(getJishuUrl())
#    print(getGithubUrl())
    print(getOpOnlineUrl())