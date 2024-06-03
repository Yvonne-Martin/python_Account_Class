def add(x,y):
    result=x+y
    return result
answer=add(1000,400)
answer=add(1.2,5.8)
print(answer)

def subtract(r,g):
    result=g-r
    return result
answer=subtract(10,20)
print(answer)

def divide(f,l):
    result=f/l
    return result
answer=divide(200,10)
print(answer)

def multiply(r,g):
    result=g*r
    return result
answer=multiply(10,20)
print(answer)

def modulus(r,g):
    result=g%r
    return result
answer=modulus(11,20)
print(answer)

def exponent(r):
    result=r**r
    return result
answer=exponent(2)
print(answer)

def sum(*numbers):#use the asteric to allow the function to take a multiple arguments
    total=0
    for number in numbers:
        total+=number
    return total


def multiplying_many(*numberz):
    total=1
    for number1 in numberz:
        total*=number1
    return total

#keyword arguments
def create_sentece(**words):
    print(words)
    sentence=""
    for word in words.values():
        sentence+=word
        sentence+=" "
    return sentence

def sum_and_greet(*args,**kwargs):
    total=0
    for x in args:
        total+=x
    f=kwargs["first_name"]
    l=kwargs["last_name"]
    greeting=f"hello {f} {l} the sum of your numbers is {total}"
    return greeting    

def check_followers(user_Id,follower_Id):
    user={}
    for user_Id in user:
        if user_Id in user:
            print("user exists")
        else:
            user.update(user_Id)
    for follower_Id in user_Id:
        if follower_Id in user_Id:
            print("follower exists")
        else:
            user[follower_Id]=user[follower_Id]
    check_followers(10,5)

def subject_scores(**scores):
    sum=0
    for score in scores.values():
        sum+=score
    average_score=sum/len(score.values)
    print(average_score)



class Products:
 def __init__(self,product):
        self.product_information = []
        self.product = product

        def add_item(product_information):
           if product_information in self.product_information:
                print("Already exist")
           else:
                print(self.product_information.append(product_information))

       


rice = Products("Rice") 
rice.add_item("150$")
print(rice)







        

    