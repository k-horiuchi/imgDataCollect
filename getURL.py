from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

url = "https://www.irasutoya.com/2019/06/blog-post_734.html"
browser = webdriver.PhantomJS()
browser.implicitly_wait(5)
browser.get(url)
sleep(5)

for i in range(100):
	for img in browser.find_elements_by_css_selector('.separator a img'):
		with open('url-list.txt', 'a') as f:
			print(img.get_attribute("src"), file=f)
	b = browser.find_element_by_xpath('//*[@id="randompost"]/a/img')
	b.click()
	sleep(5)

browser.quit()
exit()
