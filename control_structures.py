#!/usr/bin/env python
# coding: utf-8

# In[33]:


user_input = str(input("please enter the day of the week: "))
if user_input == "Monday" or user_input == "monday":
    print("It is Monday")
else:
    print("Sorry, its not Monday. Please try again")
    


# In[35]:


user_input = str(input("please enter the day of the week: "))
if user_input in ("Saturday", "Sunday") or user_input in ("saturday" , "sunday"):
    print("Yayy!! Its weekend")
else:
    print("Sorry, its the weekday")
    


# In[39]:


hours_worked = int(input("Please enter the hours worked this week: "))
hourly_rate = int(input("Please enter your hourly pay: "))
def pay_calculator(hours_worked, hourly_rate):
    if hours_worked <= 40:
        total_pay = hours_worked * hourly_rate
    else:
        total_pay = 40 * hourly_rate + (hours_worked - 40) * hourly_rate * 1.5
    return total_pay
print("your total pay is: ", pay_calculator(hours_worked, hourly_rate))


# In[3]:


day_of_the_week = ["Saturday", "Sunday"]
user_input = ""
if user_input in day_of_the_week:
    print("Yayy!! Its weekend")
else:
    print("Sorry, its the weekday")


# In[4]:


user_input = "Saturday"


# In[5]:


i = 5
while i <=  15:
    print(i)
    i += 1


# In[12]:


i = 0
while i <= 100:
    print(i)
    i += 2


# In[13]:


i = 100
while i >= -10:
    print(i)
    i -= 5


# In[15]:


i = 2
while i < 1000000:
    print(i)
    i = i**2


# In[16]:


i = 100
while i >= 5:
    print(i)
    i -= 5


# In[28]:


user_input = int(input("please enter a number: "))
i = user_input
while i <= user_input * 10:
    print(i)
    i = i + user_input


# In[1]:


for i in range(1, 10):
    print(str(i)*i)


# In[14]:


user_input = input("Please input an odd number between 1 and 50: ")
if user_input.isdigit()== True:
    for i in range(1,51):
        if i % 2 == 0 and i == user_input:
            continue
        print(i)


# In[15]:


#d
user_input = int(input("Please enter a positive number:  "))
for i in range(0, user_input + 1):
    print(i)


# In[25]:


#e
user_input = int(input("Please enter a positive integer: "))
i = user_input
while i >= 1:
    print(i)
    i -= 1
    


# In[81]:


#3
user_input = [i for i in range(1, 101)]
user_input
for num in user_input:
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num% 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)


# In[135]:


user_input = int(input("Please enter a integer: "))
for i in range(1, user_input +1):
    print(i, i**2, i**3)  
ask = input("type yes if you want to continue ")
while ask == "yes" or ask == "Yes":
    user_input = int(input("please enter a integer "))
    for i in range(1, user_input +1):
        print(i, i**2, i**3)
    ask = input("type yes if you want to continue ")


# In[137]:


#5.
grade_input = int(input("Please enter the number grade you received: "))
if grade_input in (range(88, 101)):
    print("Your letter grade is: A")
elif grade_input in range(80,88):
    print("Your letter grade is: B")
elif grade_input in range(67, 80): 
    print("Your letter grade is: C")
elif grade_input in range(60,67): 
    print("Your letter grade is: D")    
else:
    print("Your letter grade is: F")
ask = input("Would you like to continue? ")
while ask == "yes" or ask == "Yes":
    grade_input = int(input("Please enter the number grade you received: "))
    if grade_input in (range(88, 101)):
        print("Your letter grade is: A")
    elif grade_input in range(80,88):
        print("Your letter grade is: B")
    elif grade_input in range(67, 80): 
        print("Your letter grade is: C")
    elif grade_input in range(60,67): 
        print("Your letter grade is: D")    
    else:
        print("Your letter grade is: F")
    ask = input("Would you like to continue? ")





# In[71]:


#6
book_list = [{"title": "ABC",
             "author": "a123",
             "genre": "Sci-Fi"}, 
             {"title": "DEF",
             "author": "b123",
             "genre": "Sci-Fi"},
              {"title": "GHI",
             "author": "c123",
             "genre": "Fiction"},
              {"title": "JKL",
             "author": "d123",
             "genre": "Fiction"}]
for book in book_list:
    print(book)
    

    


# In[79]:


#6a
user_input = input("Please enter the genre: ")
for book in book_list:
    if book["genre"] == user_input:
        print(book)


# In[ ]:





# In[96]:


nums=1
num= int(input("Please input a number."))
continues= input("Do you want to continue?")
while continues == 'yes' or 'y':
    up_to= int(input("What number do you want to go up to?"))
    while nums <= up_to:
        res = nums**2
        nums += 1
        print(res)
    while nums <= up_to:
        res2 = num**3
        nums += 1
        print(res2)
if continues != 'yes' or 'y':
    print("The code will not continue per your request.")


# In[ ]:




