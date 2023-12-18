from bs4 import BeautifulSoup
import requests
import re, time


class Weather():
    def __init__(self) -> None:
        self.cityID = {'广东-广州': '101280101', '陕西-西安': '101110101', '广东-深圳': '101280601','吉林-长春':'101060101'}

    def getHTML(self,url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r
        except Exception as err:
            print(err)

    def readHTML(self,html, ls=None):
        if ls is None:
            ls = []
        soup = BeautifulSoup(html.text, 'lxml')
        ll = soup.select('div[id="7d"] input[id="hidden_title"]')
        #if (len(re.findall(r'\d.*C', str(ll))) > 0):
        #    ls.append(re.findall(r'\d.*C', str(ll))[0])
        ll = soup.select('ul[class="t clearfix"] li')
        for i in ll:
            s = ''
            for j in i.text:
                if j not in [' ', '\n']:
                    s += j
            if (len(re.findall(r'\d.+/.+℃', s)) > 0):
                ls.append(re.findall(r'\d.+/.+℃', s)[0])
        return ls

    def getweather(self):
        s, n = len(self.cityID), 1
        # print("执行开始".center(s // 2, "-"))
        start = time.perf_counter()
        result = []
        for i, j in self.cityID.items():
            url = 'http://www.weather.com.cn/weather/' + self.cityID[i] + '.shtml'  # ;print(url)
            HTML = self.getHTML(url)
            tx = self.readHTML(HTML)
            report = '\n'.join(tx)
            modified_str = re.sub(r'(\d+日)（(.*?)）(\D+)(-?\d+℃)/(-?\d+℃)', r'\1（\2）\3 \4/ \5', report)
            result.append("======" + i + "======" + "\n" + modified_str)
        final_report = '\n'.join(result)
        return "天气预报:"+'\n'+final_report


if __name__ == "__main__":
    w = Weather()
    print(w.getweather())
