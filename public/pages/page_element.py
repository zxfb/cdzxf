class Page_elem(object):
    userName=["id","userAccount"]
    passwd=["id","loginPwd"]
    loginbtn=["id","loginBtn"]
    user_centor=["xpath",'//*[@id="menu-user"]/dt']
    user_m=["xpath",'//*[@id="menu-user"]/dd/ul/li[1]/a']
    browsing=["xpath",'//*[@id="menu-user"]/dd/ul/li[2]/a']
    # user_centor=["xpath",'//*[@id="menu-user"]/dd/ul/li[4]/a']
    shared=["xpath",'//*[@id="menu-user"]/dd/ul/li[4]/a']
p=Page_elem()