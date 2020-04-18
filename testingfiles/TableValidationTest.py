import time
import unittest
from selenium import webdriver

class TableValidationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../drivers/x32/chromedriver.exe')
        time.sleep(2)
        self.driver.maximize_window()

    # checking for invalid value(which is not found) in table 1 and table 2
    def test_table_fun1(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        username = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
        filterbtn.click()
        time.sleep(2)
        username.send_keys("jill")
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        username.click()
        picture = "Images"
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Invalid username! Username not found in table2")
        time.sleep(2)
        searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        time.sleep(2)
        searchbar.send_keys("Inspection")
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        searchbar.click()
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("No Results found in table 1!")
        time.sleep(2)

        #valid for table1 and invalid for table2
    def test_table_fun2(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        username = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
        filterbtn.click()
        time.sleep(2)
        username.send_keys("jill")
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        username.click()
        picture = "Images"
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Invalid username! Username not found in table2")
        time.sleep(2)
        searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        time.sleep(2)
        searchbar.send_keys("Wireframes")
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        searchbar.click()
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Result found in table 1!")
        time.sleep(2)

        #invalid for table1 and valid for table2
    def test_table_fun3(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        username = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
        filterbtn.click()
        time.sleep(2)
        username.send_keys("jacobs")  #found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        username.click()
        picture = "Images"
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Username found in table2")
        time.sleep(2)
        searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        time.sleep(2)
        searchbar.send_keys("Inspection")  #not found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        searchbar.click()
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Result not found in table 1!")
        time.sleep(2)

        # valid task for table1 and valid number for table2
    def test_table_fun4(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        num = self.driver.find_element_by_xpath(
            '/ html / body / div[2] / div / div[2] / div[2] / div / table / thead / tr / th[1] / input')
        filterbtn.click()
        time.sleep(2)
        num.send_keys("1")  # found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        num.click()
        picture = "Images"
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Number/Id found in table2")
        time.sleep(2)
        searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        time.sleep(2)
        searchbar.send_keys("SEO tags")  # not found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        searchbar.click()
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Task found in table 1!")
        time.sleep(2)

    # valid assignee for table1 and valid username for table2
    def test_table_fun5(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        username = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
        filterbtn.click()
        time.sleep(2)
        username.send_keys("jacobs")  # found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        username.click()
        picture = "Images"
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Username found in table2")
        time.sleep(2)
        searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        time.sleep(2)
        searchbar.send_keys("John Smith")  # found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        searchbar.click()
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Assignee found in table 1!")
        time.sleep(2)

        # valid status for table1 and valid firstname for table2
    def test_table_fun6(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        firstname = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[3]/input')
        filterbtn.click()
        time.sleep(2)
        firstname.send_keys("Byron")  # found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        firstname.click()
        picture = "Images"
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Firstname found in table2")
        time.sleep(2)
        searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        time.sleep(2)
        searchbar.send_keys("in progress")  # found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        searchbar.click()
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Status found in table 1!")
        time.sleep(2)

    # valid status for table1 and valid lastname for table2
    def test_table_fun7(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        lastname = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[4]/input')
        filterbtn.click()
        time.sleep(2)
        lastname.send_keys("Samuels")  # found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        lastname.click()
        picture = "Images"
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Lastname found in table2")
        time.sleep(2)
        searchbar = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        time.sleep(2)
        searchbar.send_keys("in progress")  # found
        timer1 = time.strftime("%Y%m%d = %H%M%S")
        searchbar.click()
        time.sleep(2)
        self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
        print("Status found in table 1!")
        time.sleep(2)

    #valid lastname only
    # def test_table_fun9(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     # filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
    #     lastname = self.driver.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[4]/input')
    #     # filterbtn.click()
    #     time.sleep(2)
    #     lastname.send_keys("Samuels")  # found
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     lastname.click()
    #     picture = "Images"
    #     time.sleep(2)
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Lastname found in table2")
    #     time.sleep(2)

    # def test_table_fun10(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    #     #filterbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
    #     lastname = self.assertTrue(self.driver.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[4]/input'),msg="Filter button is disabled!")
    #     # filterbtn.click()
    #     # time.sleep(2)
    #     #self.assertTrue(lastname.send_keys("Samuels"),msg="Filter button is disabled!")  # found
    #     timer1 = time.strftime("%Y%m%d = %H%M%S")
    #     #lastname.click()
    #     picture = "Images"
    #     time.sleep(2)
    #     self.driver.save_screenshot("../screenShots/" + picture + timer1 + ".png")
    #     print("Lastname found in table2")
    #     time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()