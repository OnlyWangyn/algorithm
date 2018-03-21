import Pet
import Queue
class PetEntity:
    def __init__(self,count,pet):
        self.__count=count
        self.__pet = pet
    def getCount(self):
        return self.__count
    def getPet(self):
        return self.__pet
# cat = Pet.cat("cat")
# pe = PetEntity(1,cat)
# print pe.getCount()
# print pe.getPetType()
class PetEntityQueue:
    def __init__(self):
        self.catqueue = Queue.Queue(10)
        self.dogqueue = Queue.Queue(10)
        self.count=0
    def add(self,pet):
        if pet.getType()=="cat":
            self.catqueue.push(PetEntity(self.count,pet))
            self.count+=1
        if pet.getType()=="dog":
            self.dogqueue.push(PetEntity(self.count,pet))
            self.count+=1
    def pollAll(self):
        if self.isEmpty():
            print "This queue is empty"
            return
        if(not self.catqueue.isEmpty()) and (not self.dogqueue.isEmpty()):
            if(self.catqueue.peek().getCount() < self.dogqueue.peek().getCount()):
                return self.catqueue.poll().getPet()
            else:
                return self.dogqueue.poll().getPet()
        if not self.catqueue.isEmpty():
            return self.catqueue.poll().getPet()
        if not self.dogqueue.isEmpty():
            return self.dogqueue.poll().getPet()

    def pollDog(self):
        if(self.isDogEmpty()):
            print "The dog queue is empty"
            return
        return self.dogqueue.poll().getPet()
    def pollCat(self):
        if(self.isCatEmpty()):
            print "The cat queue is empty"
            return
        return self.catqueue.poll().getPet()
    def isEmpty(self):
        return self.catqueue.isEmpty() and self.dogqueue.isEmpty()
    def isDogEmpty(self):
        return self.dogqueue.isEmpty()
    def isCatEmpty(self):
        return self.catqueue.isEmpty()
dog1 = Pet.dog();
cat1 = Pet.cat();
dog2 = Pet.dog();
cat2 = Pet.cat();
dog3 = Pet.dog();
cat3 = Pet.cat();
peq = PetEntityQueue()
peq.add(dog1)
peq.add(cat1)
peq.add(dog2)
print peq.pollAll().getType()
print peq.pollAll().getType()
print peq.pollAll().getType()