def feed(l):
    for i in l:
        yield i

l =['1 to 100','100 to 200','200 to 300']
load = feed(l)
print(next(load))
print(next(load))

## Inheritence
class Status:
    def uploadImage(self,imageurl):
        self.image = imageurl
        print(f"{self.image} is uploaded to your status")

class statusV1(status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')
    
    sravani = Status()
    sravani.uploadImage('self.png')

    hema = statusV1()
    hema.uploadImage('goodmorning.png')
    hema.addCaption("morning frnds")

    ##
class Instagaram:
    def __init__(self,username):
        self.username=username
        print(f"{self.username} user is created!")

class InstaV1:
    def __init__(self,username):
        self.username=username
        print(f"{self.username} user is created!parent-2")

class Instav2(Instagaram,InstaV1):
    def __init__(self, username):
        super().__init__(username)
        InstaV1.__init__(self,username)
        print("creating users from version 3")

i = Instav2("username---xyz")


##polymorphism:
class normalUser:
    def playvideo(self,name):
        print(f"\n{name} is playing vedio with :\n1.Normal quality\n2.ads run\n3.no background quality\n4.limited vedio download\n5.music with ads")
    def likes():
        pass
    def comments():
        pass
    def share():
        pass
    def tittle():
        pass
    def description():
        pass
    def subscription():
        pass
class premiumuser(normalUser):
    def playvideo(self,name):
        print(f"\n{name} is playing vedio with :\n1.High quality\n2.Ads free\n3.background play")
def play_vedio(user,username):
    user.playvideo(username)
dinesh = normalUser()
sanjay = premiumuser()
pardhu = premiumuser()
dattu = normalUser()
arun = normalUser()


play_vedio(dinesh,"dinesh")
play_vedio(sanjay,"samjay")
play_vedio(pardhu,"pardhu")
play_vedio(dattu,"dattu")
play_vedio(arun,"arun")


###
#Polymorphism
# Operator overloading
class number:
    def _init_(self,n):
        self.n = n
    def _add_(self,other):
        return self.n+other.n
    def _sub_(self,other):
        return self.n-other.n
    def _mul_(self,other):
        return self.n * other.n
    def _str_(self):
        return f"{self.n}"
    def _lt_(self,other):
        return self.n<other.n
    def _gt_(self,other):
        return self.n>other.n
    def _eq_(self,other):
        return self.n == other.n
number1 = number(10)
number2 = number(20)
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1)
print(number1<number2)
print(number1>number2)
print(number1==number2)
















