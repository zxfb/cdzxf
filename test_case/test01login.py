from public.pages.basepages import Basepages
from selenium import  webdriver
from  time import  sleep
from public.utils.read_ini import  read
import unittest
from public.pages.page_element import p

url=read.get_value("test_data","url")
username=read.get_value("test_data","username")
password=read.get_value("test_data","password")


class Test_Login(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        driver=webdriver.Chrome()
        Basepages.set_driver(driver)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
    def test_login(self):
        driver=Basepages.get_driver()
        driver.get(url)
        driver.maximize_window()
        sleep(2)
        elem=Basepages.find_element(p.userName)
        Basepages.sendkeys(elem,username)
        elem2=Basepages.find_element(p.passwd)
        Basepages.sendkeys(elem2,password)
        elem3=Basepages.find_element(p.loginbtn)
        Basepages.click(elem3)
        sleep(2)
        quit=["link_text","退出"]
        elem4=Basepages.find_element(quit)
        value=elem4.text
        assert value=="退出"
if __name__=='__main__':
    unittest.main()