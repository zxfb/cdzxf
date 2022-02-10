'''
此模块是用来存放项目配置路径的额，方便后续在 其他模块进行导入使用

'''

import  os
base_path=os.path.dirname(os.path.dirname(__file__))
print(base_path)
data_path=os.path.join(base_path,"data")
conf_path=os.path.join(base_path,"conf")
public_path=os.path.join(base_path,"public")
pages_path=os.path.join(base_path,"public","pages")
utils_path=os.path.join(base_path,"public","utils")
report_path=os.path.join(base_path,"report")
test_path=os.path.join(base_path,"testcase")