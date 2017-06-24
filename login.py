def login(driver,url,login,password):
	driver.get(url)
	email=driver.find_element_by_id('signin-email')
	email.clear()
	email.send_keys(login) # email here
	passw=driver.find_element_by_id("signin-password")
	passw.clear()
	passw.send_keys(password) # password here
