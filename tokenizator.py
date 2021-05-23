from selenium import webdriver
from selenium.webdriver.firefox.options import Options
    

def get_ya_token(login, pas, client_id='d10e00848a11448991db9bada800a732'):
    driver = webdriver.Chrome(executable_path=r'C:\Users\ortar\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
    driver.get(f"https://oauth.yandex.ru/authorize?response_type=token&client_id={client_id}&login_hint={login}")

    enter = driver.find_element_by_xpath("//button[@data-t='button:action']")
    enter.click()
    driver.find_element_by_xpath("//button[@data-t='button:action']")
    webdriver(driver, 1)
    # element = wait.until()
    url  = driver.current_url
    input = driver.find_element_by_xpath("//button[@data-t='button:action']")
    text_input = driver.find_elements_by_class_name("Textinput-Box")
    text_input.send_keys(pas)

    print(url)
   

    

def get_vk_token(login, pas, client_id=7861393):
    driver = webdriver.Chrome(executable_path=r'C:\Users\ortar\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
    driver.get(f"https://oauth.vk.com/authorize?client_id={client_id}&response_type=token")

    email = driver.find_element_by_name('email')
    email.send_keys(login)
    password = driver.find_element_by_name('pass')
    password.send_keys(pas)
    enter = driver.find_element_by_id('install_allow')
    enter.click()
    token = driver.current_url[driver.current_url.find('access_token=') + 13 :\
         driver.current_url.find('&')]
    
    return token

if __name__ == '__main__':
    login = ""
    pas = ""
    get_ya_token(login, pas)
