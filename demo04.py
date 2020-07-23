#类

class Boy():
    def __init__(self,sex,high,weight,hair,age):
        self.sex = sex
        self.age = age
        self.high = high
        self.weight = weight
        self.hair = hair

    def caiyi(self,num):
        """
        才艺
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的男孩开始了自己的才艺表演之：")
        if num == 1:
            print("唱跳RAP篮球")
        elif num == 2:
            print("胸口碎大石")
        else:
            print("单手开瓶盖")
    
    def chuyi(self):
        """
        厨艺
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的男孩开始了自己的厨艺表演之：")
        print("精通八大菜系！")

    def work(self):
        """
        工作
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的男孩开始了自己的工作之：")
        print("开挖掘机")

#类的实例化
zhangsan = Boy("男","180cm","60kg","光头","32岁")

zhangsan.caiyi(1)
zhangsan.work()
print(zhangsan.age)


#继承、重写
# Boy：父类
# Boyfriend：子类
class Boyfriend(Boy):
    def work(self):
        print("修电脑")    #重写

zhangsan = Boyfriend("男","179cm","58kg","光头","25岁")
zhangsan.caiyi(1)

