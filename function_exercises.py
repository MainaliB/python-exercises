#!/usr/bin/env python
# coding: utf-8

# In[154]:


#1.Define a function named is_two. It should accept one input and return 
#True if the passed input is either the number or the string 2, False otherwise.

# is_two() function here only takes one argument
def is_two(num):
    # next we are checking if the input is a number or the string 2
    if type(num)== int(2) or type(num)== str(2): 
        return True
    else:
        return False


# In[15]:


#2.Define a function named is_vowel. 
#It should return True if the passed string is a vowel, False otherwise.
# the function here requires a string as an input
def is_vowel(letter):
    # here we are checking if the passed string is a vowel, by saying if the letter is in the list of the vowels
    if letter.lower() in ("a","e","i","o","u"):
        return True
    else:
        return False
is_vowel("a")


# In[157]:


#3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this.

# the function here takes a string letter as an argument and checks if it is vowel using the function created above
def is_consonant(letter):
    # if the is_vowel function on the input letter equates to False then the output will be true
    if is_vowel(letter) == False:
        return True
    else:
        return False
is_consonant("B")


# In[155]:


#4.Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word if the word starts with a consonant.

# here the function takes a string word as an input
def capitalize_consonant(word):
    # using indexing to determine if the first letter of the string is not a vowel
    if word[0] not in ("a","e","i","o","u","A", "E", "I", "O", "U"):
        return word.capitalize() # if the first letter is not a vowel then the capitalize function will capitalize the word
    else:
        return word
capitalize_consonant("bravo")


# In[34]:


#5. Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# here the function takes two arguments: tip_percentage(a number between 0 and 1) and total_bill
def calculate_tip(tip_percent, total_bill):
    amount_to_tip = tip_percent * total_bill # amount to tip is calculated by multiplying the tip_percentage with total_bill
    return (f"Amount to tip is ${amount_to_tip}") # return statement is fomatted to have a statement as an output
calculate_tip(0.25, 100)


# In[161]:


#6. Define a function named apply_discount. It should accept a original price,
#and a discount percentage, and return the price after the discount is applied.

# the function here takes two arguments: original price and discount percentage
def apply_discount(original_price, discount_percentage):
    
    
    # the price after discount is calculated by subtracting the discount from the original price
    return f"Price after discount is ${(original_price - ((discount_percentage/100) * original_price))}"


apply_discount(100, 25)


# In[41]:


#7. Define a function named handle_commas. 
#It should accept a string that is a number that contains commas in it as input, and return a number as output.

# here the function takes a string that is a number with commas as an argument
def handle_commas(str_num_with_comma):
    # we are using .replace function to replace the commas and casting the strings as an integer and returning
    str_without_comma = str_num_with_comma.replace(",", "")
    return int(str_without_comma)
handle_commas("12,4,5,0,000")


# In[44]:


#8. Define a function named get_letter_grade. 
#It should accept a number and return the letter grade associated with that number (A-F).

# here the function takes an integer as the number grade
def get_letter_grade(number_grade):
    # the various else if statements are made to check what range the input falls into and return the letter grade 
    if number_grade >= 90:
        return "Your letter grade is A"
    elif number_grade >= 80:
        return "Your letter grade is B"
    elif number_grade >= 70:
        return "Your letter grade is C"
    elif number_grade >= 60:
        return "Your letter grade is D"
    else:
        return "You failed!! Your letter grade is F"
get_letter_grade(45)


# In[158]:


#9. Define a function named remove_vowels that accepts a string 
#and returns a string with all the vowels removed.

# the function here takes a string as an argument

def remove_vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u') # created a tuple of vowels
    for letter in word.lower():
        if letter in vowels: # if the letter in the input string is in the vowel then it is replace with nothing and returned
            word = word.replace(letter,"")
    return word
remove_vowels("mango")


# In[159]:


#10. Define a function named normalize_name. 
#It should accept a string and return a valid python identifier, that is:

def normalized_name(word):
    new_word = word.strip()
    new_word = new_word.lower()
    new_word = new_word.replace(" ", "_")
    new_word = new_word.replace("%", "")
    new_word = new_word.replace("#", "")
    new_word = new_word.replace("!", "")
    new_word = new_word.replace("@", "")
    return new_word
normalized_name(" %Bibek Mainali   ")


# In[100]:


#11. Write a function named cumulative_sum that accepts a list of numbers 
#and returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(lst_numbers):
    sum = 0
    for num in lst_numbers:
        sum = sum + num
    return sum
cumulative_sum([1,2,3,4])


# In[147]:


#Bonus 1.
#Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm 
#and return a string that is the representation of the time in a 24-hour format.

def twelveto24(time_as_str):
    time_as_str = time_as_str.replace(":", "")
    if time_as_str == "1200am":
        time_as_str = "0000"
    elif "am" in time_as_str:   
        time_as_str = time_as_str.replace("am", "")
        if len(time_as_str) < 4:
            time_as_str = ("0"+ time_as_str)
        else: time_as_str = time_as_str
    else:
        time_as_str = time_as_str.replace("pm", "")
        if len(time_as_str) <4:
            time_as_str = ("0" + time_as_str)
            time_as_str = int(time_as_str)
            time_as_str = str(time_as_str + 1200)
        else:
            time_as_str = int(time_as_str)
            time_as_str = str(time_as_str + 1200)
            
    return time_as_str
twelveto24("11:59pm")     


# In[153]:





# In[ ]:





# In[ ]:





# In[ ]:




