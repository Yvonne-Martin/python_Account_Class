def hello(name):
    print(f"hello {name}")

def year_of_birth(name,age):
    print(f"hello {name} you were born in {2024-age}")

def my_country(country="kenya"):
    print(f"Hello AkiraChix from {country}")

"Check whether a given key already exists in a dictionary"
def key_in_dict(d,key):
    return (key in d)
students={'yvonne':20,
          'leila':30,
          'martin':80}
print(students)
print(key_in_dict(students,"leila"))

d={1:20,2:40,5:90}
def is_key_present(x):
    if x in d:
        print('key present')
    else:
        print('key not present')
is_key_present(1)   

     # Prompt the user to input a number and store it in the variable 'n'.
n = 5
d = dict()
for x in range(1, n + 1):
    d[x] = x * x
print(d) 

def are_anagrams(str1,str2):
    if sorted(str1.lower())==sorted(str2.lower()):
       print(f"{str1} and {str2} are anagrams")
    else:
        print(f"{str1} and {str2} are not anagrams")
    
str1="cat"
str2="act"
are_anagrams(str1,str2)

def vowel_count(str):
    count=0
    vowels=set("a,e,i,o,u,A,E,I,O,U")
    for alphabets in str:
        if alphabets in vowels:
            count+=1
            print(count)
str = "Apple"
vowel_count(str)

def my_vowels(name,vowels):
    count1 =sum(name.count(vowel)for vowel in vowels)
    print(count1)

name="yvonnemartin"
vowels="aeiouAEIOU"
my_vowels(name,vowels)

def unique(integers):
    integers=set(integers)
    integers=list(integers)
    print(integers)
integers=[2,4,5,6,7,6,5,4,3,2,1]
unique(integers)

def reversed_sentence(sentence):
    sentence=list(sentence)
    sentence.reverse()
    sentence=''.join(sentence)
    print(sentence)
sentence="i am yvonne"
reversed_sentence(sentence)

def sorting_array(arr1,arr2):
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    arra3=sorted(arr1+arr2)
    print(arra3)
sorting_array([4,6,7,8,9],[0,1,2,3,])

# def my_string(word):
#     new_list=list(word)
#     new_list.reverse()
#     new_list="".join(new_list)
#     print(new_list)
# my_string("I love coding")



def addition(numbers):
    sum = 1
    for num in numbers:
        sum*=num
    print(sum)
numbers = [1,3,5,3,2]
addition(numbers)

def greet(*name):
    print(f"hello {name}")
    for name in names:
        print(f"hello {name}")