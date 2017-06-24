# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from login import login
import time

''' 
	Please remove lines above(10-13) and use just driver=webdriver.Firefox() in case you do not want to use Phantom JS and want to test explicitly.
	And if you have other preference related to user agent specify it  at line 12
	@Author Albert Stepanyan 1felisidad1@gmail.com 
'''

caps = DesiredCapabilities.PHANTOMJS
caps["phantomjs.page.settings.userAgent"]="Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
username=""  #twitter username here
driver = webdriver.PhantomJS(desired_capabilities=caps)
#driver = webdriver.Firefox()
driver.set_window_size(1924,1020)
login(driver,"https://twitter.com","your login here","password")
driver.find_element_by_css_selector('button.submit').click()
time.sleep(2)
driver.get("https://www.twitter.com/%s" % username)
time.sleep(1)
count=0
for item in driver.find_elements_by_css_selector("div.IconContainer.js-tooltip"):
	time.sleep(2)
	item.click()
	driver.save_screenshot("lt.png")
	driver.find_elements_by_css_selector("li.js-actionDelete")[0].click()
	print 1
	time.sleep(2)
	driver.save_screenshot("t.png")
	driver.find_element_by_css_selector("button.EdgeButton.EdgeButton--danger.delete-action").click()
	count+=1
	driver.save_screenshot("result.png")
	time.sleep(2)
	print "%d twit(s) is gone " % count
