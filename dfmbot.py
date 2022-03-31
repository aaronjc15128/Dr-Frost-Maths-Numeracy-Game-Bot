def main():
    from time import sleep
    from os import system
    
    system("cls")

    print("LOGIN DETAILS\n-------------")
    email = input("EMAIL: ")
    password = input("PASSWORD: ")
    print("\n\nBOT DETAILS\n-----------")
    sleeptime = float(input("QUESION DELAY TIME: "))
    useEnter = bool(input("USE ENTER: "))
    print("\n\nSELENIUM\n--------")

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome('./chromedriver')

    driver.get("https://www.drfrostmaths.com/timestables-game.php")

    driver.find_element(By.NAME, "login-email").send_keys(email)
    driver.find_element(By.NAME, "login-password").send_keys(password)
    driver.find_element(By.NAME, "login-password").submit()

    driver.find_element(By.LINK_TEXT, "Start the Clock").click()

    for _ in range(100):
        sleep(sleeptime)
        qlist = list(driver.find_element(By.ID, "question").text)
        if "×" in qlist: qlist[qlist.index("×")] = "*"
        elif "÷" in qlist: qlist[qlist.index("÷")] = "/"
        a = str(int(eval("".join(qlist))))

        driver.find_element(By.ID, "calculator-display").send_keys(a)
        if useEnter: driver.find_element(By.ID, "calculator-display").send_keys(Keys.ENTER)

if __name__ == "__main__":
    main()
