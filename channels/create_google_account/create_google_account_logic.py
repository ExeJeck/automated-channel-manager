import random

from selenium import webdriver
from selenium.webdriver.common.by import By


class CreateGoogleAccount:
    def create_symbols_tuple():
        digits = tuple(str(number) for number in range(10))
        uppercase_letters = tuple(chr(code) for code in range(ord('A'), ord('Z') + 1))
        lowercase_letters = tuple(chr(code) for code in range(ord('a'), ord('z') + 1))
    
        symbols_tuple = digits + uppercase_letters + lowercase_letters

        return symbols_tuple
    

    def create_google_account(self):
        driver = webdriver.Chrome()
        driver.get("https://accounts.google.com/lifecycle/steps/signup/name?continue=https://myaccount.google.com/&ddm=1&dsh=S1209235751:1738035373831115&ec=GAlAwAE&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ru&service=accountsettings&TL=AO-GBTcMH_Vf8xSYkWqkycXPsEdYMGz0uAJd2Oa5UsXX4lgy6E1Qgw1I3Ur3p77I")
        driver.implicitly_wait(1)

        first_name_input = driver.find_element(By.ID, "firstName")
        last_name_input = driver.find_element(By.ID, "lastName")

        first_button_next = driver.find_element(By.TAG_NAME, "button")

        first_name_input.send_keys("")
        last_name_input.send_keys("")

        first_button_next.click()

        

    def main_logic(self):
        random_number = random.randint(1, 10)
        symbols_tuple = self.create_symbols_tuple()


if __name__ == "__main__":
    create_google_account = CreateGoogleAccount()
    create_google_account.main_logic()

