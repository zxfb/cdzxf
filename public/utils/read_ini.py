from  configparser import ConfigParser
from conf.config import data_path
import os
class Read_Ini(ConfigParser):
    def __init__(self,file):
        super(Read_Ini,self).__init__()
        self.read(file)
    def get_value(self,section,option):
        return self.get(section,option)
file=os.path.join(data_path,"data.ini")
read=Read_Ini(file)
# if __name__=="__main__":
#     file=os.path.join(data_path,"data.ini")
#     read=Read_Ini(file)
#     url=read.get_value("test_data","url")
#     print(url)