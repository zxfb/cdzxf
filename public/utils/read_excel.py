import xlrd
from conf.config import data_path
import os
file=os.path.join(data_path,"data.xls")
class Read_Excel(object):
    def __init__(self,file,sheetname):
        self.book=xlrd.open_workbook(file)
        self.sheet=self.book.sheet_by_name(sheetname)
    def get_excel_value(self,row,low):
        return self.sheet.cell_value(row,low)
if __name__=='__main__':
    r=Read_Excel(file,"Sheet1")
    print(r.get_excel_value(2,0))