
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
        el = driver.find_element(By.XPATH, '//*[@id="home-body"]/main/div/div[2]/ul/li['+str(i)+']/div[2]/div/div/a')
        new_url = el.get_attribute("href")
        result.append(str(i)+'\n'+el.text+'\n'+new_url+'\n')
    driver.quit()
    text = '\n'.join(result)
    return text

if __name__=="__main__":
    print(getUrl())