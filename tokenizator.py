    from selenium import webdriver
    

def get_token(login, pas, client_id=7861393):
    driver = webdriver.Chrome(executable_path='C:\\Users\\Ortariot\AppData\\Local\\Programs\\Python\\Python38-32\\lib\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe')

    driver.get(f"https://oauth.vk.com/authorize?client_id={client_id}&response_type=token")

    # username = '//*[@id="login_submit"]/div/div/input[6]'
    # password = '//*[@id="login_submit"]/div/div/input[7]'
    # login = '//*[@id="install_allow"]'

    email = driver.find_element_by_name('email')
    email.send_keys("@rambler.ru")
    password = driver.find_element_by_name('pass')
    password.send_keys("Raduga")
    enter = driver.find_element_by_id('install_allow')
    enter.click()
    # token = driver.current_url[driver.current_url.find('access_token=') + 13 :  ]
    print(driver.current_url)

