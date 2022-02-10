import unittest
from conf.config import test_path,report_path
from report.HTMLTestRunner3_New import HTMLTestRunner
import os
from time import strftime
start_dir=test_path
now=strftime("%Y-%m-%d_%H_%M_%S")
file=os.path.join(report_path,now+"_UI自动化测试报告.html")
f=open(file,"wb")
discover=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="test*.py")
runner=HTMLTestRunner(stream=f,
                      title="UI自动化测试报告",
                      description="用例情况执行如下：",
                      tester="zxf")
runner.run(discover)