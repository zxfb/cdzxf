from public.pages.basepages import Basepages
from selenium import  webdriver
from  time import  sleep
from public.utils.read_ini import  read
import unittest
from public.pages.page_element import p

class User_Centor(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_user_m(self):
        sleep(2)
        elem=Basepages.find_element(p.user_m)
        Basepages.click(elem)
