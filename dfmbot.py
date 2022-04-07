def main():
    from time import sleep
    from os import system
    import sys
    
    # clearing terminal
    system("cls")

    # getting user input
    print("LOGIN DETAILS\n-------------")
    email = input("EMAIL: ")
    password = input("PASSWORD: ")
    print("\n\nBOT DETAILS\n-----------")
    
    # if user doesn't input float -> make sleeptime = 0.3
    try: sleeptime = float(input("QUESION DELAY TIME: "))
    except ValueError: sleeptime = 0.3
    
    # if user doesn't input bool -> make useEnter = true
    try: useEnter = bool(input("USE ENTER: "))
    except ValueError: useEnter = True
    print("\n\nPROCESS LOGS\n------------")
    

    # selenium and webdriver_manager imports
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import ElementNotInteractableException
    from selenium.common.exceptions import NoSuchElementException
    from webdriver_manager.chrome import ChromeDriverManager

    # installing chromdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # opening dr frost maths timestables game
    driver.get("https://www.drfrostmaths.com/timestables-game.php")


    # logging in
    driver.find_element(By.NAME, "login-email").send_keys(email)
    driver.find_element(By.NAME, "login-password").send_keys(password)
    driver.find_element(By.NAME, "login-password").submit()

    # clicking start button
    # check for incorrect email/password -> print a log
    try: driver.find_element(By.LINK_TEXT, "Start the Clock").click()
    except NoSuchElementException:
        print("\n\n\nINCORRECT EMAIL/PASSWORD\n\nDFMBot\nby Aaron Chauhan")
        sys.exit()


    # loop 100 times
    for _ in range(100):
        sleep(sleeptime)

        # getting question, splitting it up into a list
        qlist = list(driver.find_element(By.ID, "question").text)
        
        # converting symbols
        if "×" in qlist: qlist[qlist.index("×")] = "*"
        elif "÷" in qlist: qlist[qlist.index("÷")] = "/"
        
        # joining up list, finding answer
        a = str(int(eval("".join(qlist))))

        try:
            # input answer, press enter (only if useEnter = true)
            driver.find_element(By.ID, "calculator-display").send_keys(a)
            if useEnter: driver.find_element(By.ID, "calculator-display").send_keys(Keys.ENTER)

        # if game finished (inputting answer returns an error), break loop
        except ElementNotInteractableException: break

    print("\n\n\nPROCESS FINISHED\n\nDFMBot\nby Aaron Chauhan")

if __name__ == "__main__":
    main()
