import  unittest
from selenium import  webdriver
class Basepages(unittest.TestCase):
    @classmethod
    def set_driver(cls,driver):
        cls.driver=driver
    @classmethod
    def get_driver(cls):
        return cls.driver
    @classmethod
    def find_element(cls,element):
        type=element[0]
        value=element[1]
        if type=="id":
            elem=cls.driver.find_element_by_id(value)
        elif type=="name":
            elem=cls.driver.find_element_by_name(value)
        elif type=="class":
            elem=cls.driver.find_element_by_class_name(value)
        elif type=="xpath":
            elem=cls.driver.find_element_by_xpath(value)
        elif type=="css":
            elem=cls.driver.find_element_by_css_selector(value)
        elif type=="link_text":
            elem=cls.driver.find_element_by_link_text(value)
        else:
            raise ValueError("please input correct type!")
        return elem
    @classmethod
    def sendkeys(cls,elem,text):
        return elem.send_keys(text)
    @classmethod
    def click(cls,elem):
        return elem.click()
if __name__ == '__main__':
    from public.utils.read_ini import Read_Ini
    import os
    from conf.config import data_path
    file=os.path.join(data_path,"data_ini")
    read=Read_Ini(file)
    url=read.get_value("test01_data","url")
    Basepages.set_deiver(webdriver.Chrome())
    Basepages.get_driver().get(url)
    baidu_input=["id","kw"]
    elem=Basepages.find_element(baidu_input)
    Basepages.sendkeys(elem,"python")

