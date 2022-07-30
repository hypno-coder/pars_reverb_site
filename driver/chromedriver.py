from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.headless = True
#что бы не открывало бразуер

driver = wd.Chrome(
    executable_path=
    "/Users/arturdavidov/Documents/work/selenium/chromedriver/chromedriver",
    options=chrome_options)