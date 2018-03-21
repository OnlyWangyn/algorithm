#encoding=utf-8
class pet(object):
    def __init__(self,type):
        self.__type = type
    def getType(self):
        return self.__type
class cat(pet):
    def __init__(self):
        super(cat,self).__init__("cat")#只能用于新样式，也就是基类必须继承object
        #pet.__init__(self,type)＃可以用于旧样式的类，也就是基类无须继承object
class dog(pet):
    def __init__(self):
        pet.__init__(self,"dog")
# d = dog("dog")
# #继承object 输出(<class '__main__.dog'>, <class '__main__.pet'>, <type 'object'>)
# print d.__class__.__mro__