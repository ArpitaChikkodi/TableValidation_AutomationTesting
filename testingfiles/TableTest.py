import time
import unittest
from selenium import webdriver


class TableTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../drivers/x32/chromedriver.exe')
        time.sleep(2)
        self.driver.maximize_window()

    # #Checking for valid value(task/assignee/status) in table
    # def test_table_fun1(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
    #     time.sleep(2)
    #     searchbar.send_keys("Wireframes")
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     searchbar.click()
    #     time.sleep(2)
    #     picture = "Images"
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Result found!")
    #     time.sleep(2)
    #
    # # checking for invalid value(which is not found) in table 1
    # def test_table_fun2(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
    #     time.sleep(2)
    #     searchbar.send_keys("Inspection")
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     searchbar.click()
    #     time.sleep(2)
    #     picture = "Images"
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("No Results found!")
    #     time.sleep(2)
    #
    # # Checking for valid username
    # def test_table_fun3(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
    #     username = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
    #     filterbtn.click()
    #     time.sleep(2)
    #     username.send_keys("jacobs")
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     username.click()
    #     time.sleep(2)
    #     picture = "Images"
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Valid username!")
    #     time.sleep(2)

    # # Checking for invalid username in table2
    # def test_table_fun4(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
    #     username = self.driver.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
    #     filterbtn.click()
    #     time.sleep(2)
    #     username.send_keys("jacobs")
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     username.click()
    #     time.sleep(2)
    #     picture = "Images"
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Invalid username!")
    #     time.sleep(2)
    #
    # # Checking for valid Firstname in table2
    # def test_table_fun5(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
    #     firstname = self.driver.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[3]/input')
    #     filterbtn.click()
    #     time.sleep(2)
    #     firstname.send_keys("Byron")
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     firstname.click()
    #     time.sleep(2)
    #     picture = "Images"
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Valid firstname!")
    #     time.sleep(2)
    #
    # # Checking for invalid Firstname
    # def test_table_fun6(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
    #     firstname = self.driver.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[3]/input')
    #     filterbtn.click()
    #     time.sleep(2)
    #     firstname.send_keys("Bryson")
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     firstname.click()
    #     time.sleep(2)
    #     picture = "Images"
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Invalid firstname!")
    #     time.sleep(2)
    #
    # # Checking for valid lastname in table2
    # def test_table_fun7(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
    #     lastname = self.driver.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[4]/input')
    #     filterbtn.click()
    #     time.sleep(2)
    #     lastname.send_keys("Samuels")
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     lastname.click()
    #     time.sleep(2)
    #     picture = "Images"
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Valid lastname!")
    #     time.sleep(2)
    #
    # # Checking for invalid lastname
    # def test_table_fun8(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
    #     lastname = self.driver.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[4]/input')
    #     filterbtn.click()
    #     time.sleep(2)
    #     lastname.send_keys("Devilliers")
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     lastname.click()
    #     time.sleep(2)
    #     picture = "Images"
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Invalid lastname!")
    #     time.sleep(2)

    # Checking for valid number in table2
    def test_table_fun9(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        num = self.driver.find_element_by_xpath(
            '/ html / body / div[2] / div / div[2] / div[2] / div / table / thead / tr / th[1] / input')
        filterbtn.click()
        time.sleep(2)
        num.send_keys("1")
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        #num.click()
        time.sleep(2)
        picture = "Images"
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Valid Number! Result foumd!")
        time.sleep(2)

    # Checking for invalid number(<1 or >5 or alphabet) in table2
    def test_table_fun10(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        num = self.driver.find_element_by_xpath(
            '/ html / body / div[2] / div / div[2] / div[2] / div / table / thead / tr / th[1] / input')
        filterbtn.click()
        time.sleep(2)
        num.send_keys("21")
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        num.click()
        time.sleep(2)
        picture = "Images"
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Invalid number! Result not foumd!")
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
