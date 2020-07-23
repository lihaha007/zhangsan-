#函数/方法

"""
自动判断账号，账号长度5-8，账号小写开头
"""
def checkname(username):
    if len(username) >= 5 and len(username) <= 8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            print("OK")
        else:
            print("首字母必须小写开头")
    else:
        print("账号不合格，5-8位")

a = "cncdan"
checkname(a)


# def    方法的声明
# checkname   方法的名字
# username    方法参数
# 方法的说明
# 方法的逻辑代码


def jiafa(a,b):
    """
    实现两个数的相加
    """
    if type(a) is int and type(b) is int:
        return a+b
    else:
        return "输入的数据类型不正确"

a = jiafa(1,2)
print(a+3)

#异常捕获
try:
    print("a"+11)
except Exception as e:
    print("代码错误",e)


a = input("请输入你的名字：")
b = input("请输入你的年龄：")
try:
    if int(b) > 18:
        print(a,"成年")
    else:
        print(a,"未成年")
except:
    print("请输入正确的年龄")


#包
# import pymysql

"""
定义一个方法，用来判断用户输入的账号密码是否符合规定
"""
def check(username,password):
    """
    账号长度5-8，密码6-12位，账号小写开头。
    """
    if len(username) >= 5 and len(username) <= 8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            if len(password) >= 6 and len(password) <= 12:
                return True
            else:
                return "密码不符合"
        else:
            return "首字母必须小写开头"
    else:
        return "账号不合格，5-8位"

check("vdxbtbx","szdvdfb")
