# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time

# #for the main page:
# Email_or_phone = input("enter the Email_or_phone:-")
# Password = input("enter the Password:-")
# #finding the main page driver:-
# driver = webdriver.Chrome('chromedrive_64/chromedriver')
# driver.maximize_window()
# #finding the driver for main page
# driver.get("https://www.facebook.com/")
# Email = driver.find_element_by_id("email")
# Pass = driver.find_element_by_id("pass")
# Email.send_keys(Email_or_phone)
# Pass.send_keys(Password)
# log_in = driver.find_element_by_id("loginbutton")
# log_in.click()
# time.sleep(5)
# # finding the main page link:-
# response = driver.execute_script("return document.documentElement.outerHTML")
# soup = BeautifulSoup(response,"html.parser")
# main_div = soup.find("div",class_="_1k67 _cy7")
# sub_div = main_div.find("a")["href"]
# driver.quit()
# # for the friends page
# req = webdriver.Chrome('chromedrive_64/chromedriver')
# req.maximize_window()
# req.get(str(sub_div))
# time.sleep(5)
# Email1 = req.find_element_by_id("email")
# Pass1 = req.find_element_by_id("pass")
# Email1.send_keys(Email_or_phone)
# Pass1.send_keys(Password)
# log_in1 = req.find_element_by_id("loginbutton")
# log_in1.click()
# time.sleep(15)
# #opening of friends bar:-
# f = req.find_element_by_xpath('//*[@id="u_0_1c"]/li[3]/a').click()
# time.sleep(5)
# # #for scrolling of page:
# last_height = req.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# flag = True
# while flag:
# 	req.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# 	time.sleep(3)
# 	new_height = req.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# 	if new_height == last_height:
# 		flag = False
# 	last_height = new_height
# # finding friends_names
# res = req.execute_script("return document.documentElement.outerHTML")
# soup_for_friends = BeautifulSoup(res,"html.parser")
# friends_list = soup_for_friends.find("div",class_="_5h60 _30f")
# friends_name_tags = friends_list.find_all("div",class_="fsl fwb fcb")
# for i in friends_name_tags:
# 	a_tags = i.find("a").text
# 	print(a_tags)








