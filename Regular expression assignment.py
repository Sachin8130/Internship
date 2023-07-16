#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1- Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).


# In[2]:


import regex as re


# In[8]:


String1="Hello Data Science Class 42"
x=re.findall("\w",String1)
print(x)


# In[9]:


#1.Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
def check_string_characters(string):
    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    for char in string:
        if char not in allowed_characters:
            return False
    return True

# Test cases
strings = ["abc123", "HelloWorld", "OpenAI", "12345!", "Special_Chars", "7890"]
for string in strings:
    if check_string_characters(string):
        print(f"The string '{string}' contains only the specified characters.")
    else: 
        print(f"The string '{string}' contains characters outside the specified set.")


# In[14]:


#1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
def string_char(string):
    allowed_char=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    for char in string:
        if char not in allowed_char:
            return False
        return True
            
strings=["xyz123","rutx1122","HelloRegex","Joker2kl","1230"]
for string in strings:
    if string_char(string):
        print(f"The string'{string}'contains only specified character")
    else:
        print(f"The string '{string}'contains charater outside the specified set")


# In[21]:


#Q2.Create a function in python that matches a string that has an a followed by zero or more b's
import re

def match_pattern(text):
    pattern = r'a(b*)'  # RegEx pattern: 'a' followed by zero or more 'b's
    matches = re.findall(pattern, text)
    
    if matches:
        return True
    else:
        return False
    
text1 = 'ab'    
text2 = 'abb'
text3 = 'ac'      
text4 = 'abcd'    
text5 = 'def'     

print(match_pattern(text1))  # Output: True
print(match_pattern(text2))  # Output: True
print(match_pattern(text3))  # Output: True
print(match_pattern(text4))  # Output: True
print(match_pattern(text5))  # Output: False


# In[7]:


#Question 3-  Create a function in python that matches a string that has an a followed by one or more b's
import regex as re
def match_pattern(string):
    pattern=r'^ab+'
    match=re.findall(pattern,string)
    
    if match:
        return True
    else:
        return False
    
text1= 'a'
text2= 'abcd'
text3='aabb'
text4='badc'
text5='abbb'

print(match_pattern(text1))
print(match_pattern(text2))
print(match_pattern(text3))
print(match_pattern(text4))
print(match_pattern(text5))


# In[10]:


#Question 4- Create a function in Python and use RegEx that matches a string that has an a followed by zero or one 'b'.
import regex as re
def match_pattern(string):
    pattern=r'^ab?'
    match=re.findall(pattern,string)
    
    if match:
        return True
    else:
        return False
    
text1='a'
text2='abc'
text3='aab'
text4='bad'
text5='aabb'
print(match_pattern(text1))
print(match_pattern(text2))
print(match_pattern(text3))
print(match_pattern(text4))
print(match_pattern(text5))


# In[27]:


#Question 5- Write a Python program that matches a string that has an a followed by three 'b'.
import regex as re
def match_pattern(string):
    pattern=r'^abbb'
    match=re.findall(pattern,string)
    
    if match:
        return True
    else:
        return False
    
text1='a'
text2='abb'
text3='abbb'
text4='abbbb'
text5='xyaabbb'
print(match_pattern(text1))
print(match_pattern(text2))
print(match_pattern(text3))
print(match_pattern(text4))
print(match_pattern(text5))


# In[24]:


#Question 6- Write a regular expression in Python to split a string into uppercase letters.
import regex as re
def uppercase(string):
    pattern=r'(?=[A-Z])'
    result=re.split(pattern,string)
    return result

string="ImportanceOfRegularExpressionInPython"
result=uppercase(string)
print(result)


# In[33]:


#Question 7- Write a Python program that matches a string that has an a followed by two to three 'b'.
import regex as re
def match_string(string):
    pattern=r'^a(bb|bbb)$'
    match=re.findall(pattern,string)
    
    if match:
        return True
    else:
        return False
    
text1='ab'
text2='abb'
text3='abbb'
text4='abbbb'
text5='aabbbs'

print(match_string(text1))
print(match_string(text2))
print(match_string(text3))
print(match_string(text4))
print(match_string(text5))


# In[34]:


#Question 8- Write a Python program to find sequences of lowercase letters joined with a underscore.
import regex as re
def match(string):
    pattern=r'[a-z]+_[a-z]+'
    matches=re.findall(pattern,string)
    return matches

string="My_name is Sach_in and i am learn_ing pyt_hon"
result=match(string)
print(result)


# In[51]:


#Question 9- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import regex as re
def match(string):
    pattern=r'^a.*b$'
    matches=re.findall(pattern,string)
    
    if matches:
        return True
    else:
        return False
    
text1='aman'
text2='anjali'
text3='adverb'
text4='absob'

print(match(text1))
print(match(text2))
print(match(text3))
print(match(text4))


# In[68]:


#Question 10- Write a Python program that matches a word at the beginning of a string.
import re

def match(string):
    pattern = r'^a\w+'
    match = re.match(pattern, string)
    
    if match:
        return True
    else:
        return False

text1 = 'abc'     
text2 = 'bad'     
text3 = 'aabcde'  
text4 = 'bacd'    

print(match(text1))
print(match(text2))
print(match(text3))
print(match(text4))


# In[4]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
import re

def is_valid_string(input_string):
    pattern = r'^\w+$'
    return re.match(pattern, input_string) 

# Test the program
strings = [
    "Hello_World123",
    "123456",
    "AbC_dEf_123",
    "!@#$%",
    "AbC_dEf_123!",
    "hello world",
]

for string in strings:
    if is_valid_string(string):
        print(f"{string} is valid.")
    else:
        print(f"{string} is not valid.")


# In[6]:


#Question 12- Write a Python program where a string will start with a specific number.
def match(string):
    pattern=r'^\d'
    matches=re.findall(pattern,string)
    
    if matches:
        return True
    else:
        return False
    
text1="1oijfh"
text2="achbddf"
text3="439485"
text4="#455jfbcj"

print(match(text1))
print(match(text2))
print(match(text3))
print(match(text4))


# In[5]:


#Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r"\b([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)? \d{4})\b"

match = re.match(pattern, text)

if match:
    date_string = match.group
    print("Date found:", date_string)
else:
    print("No date found.")


# In[6]:


#Question 15- Write a Python program to search some literals strings in a string. Go to the editor
def search_literals(string, literals):
    found_literals = []
    for literal in literals:
        if literal in string:
            found_literals.append(literal)
    return found_literals

text = "This is a sample string to demonstrate the search functionality."
search_terms = ["sample", "functionality", "notfound"]

found_terms = search_literals(text, search_terms)

print("Found literals:")
for term in found_terms:
    print(term)


# In[7]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
def search_string(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    locations = []

    for i in range(text_length - pattern_length + 1):
        if text[i:i+pattern_length] == pattern:
            locations.append(i)

    return locations

text = "Hello, how are you? Hello, nice to meet you!"
pattern = "Hello"

result = search_string(pattern, text)

if result:
    print(f"Pattern '{pattern}' found at position(s): {', '.join(map(str, result))}")
else:
    print(f"Pattern '{pattern}' not found in the text.")


# In[8]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
def convert_date(date):
    # Split the date into year, month, and day
    year, month, day = date.split('-')

    # Rearrange the date components
    new_date = f"{day}-{month}-{year}"

    return new_date

# Example usage
date = "2023-07-16"

converted_date = convert_date(date)

print(f"Original date: {date}")
print(f"Converted date: {converted_date}")


# In[9]:


#Question 20- Write a Python program to find all words starting with 'a' or 'e' in a given string.
import re

def find_words_starting_with_a_or_e(text):
    # Split the text into individual words
    words = re.findall(r'\b[a-zA-Z]+\b', text)

    filtered_words = [word for word in words if word[0].lower() in ['a', 'e']]

    return filtered_words

text = "An apple a day keeps the doctor away. Eat your carrots and enjoy life."

words_starting_with_a_or_e = find_words_starting_with_a_or_e(text)

print("Words starting with 'a' or 'e':")
for word in words_starting_with_a_or_e:
    print(word)


# In[10]:


#Question 22- Write a regular expression in python program to extract maximum numeric value from a string
import re

def extract_max_numeric_value(text):
    numeric_values = re.findall(r'\d+', text)
    if numeric_values:
        max_numeric_value = max(map(int, numeric_values))
        return max_numeric_value
    else:
        return None

text = "The maximum value is 42, but there are also other numbers like 17 and 99."

max_value = extract_max_numeric_value(text)

if max_value is not None:
    print(f"The maximum numeric value is: {max_value}")
else:
    print("No numeric values found in the text.")


# In[12]:


#Question 23- Write a Regex in Python to put spaces between words starting with capital letters
import re

def add_spaces_between_capital_words(text):
    spaced_text = re.sub(r'(?<!\s)(?=[A-Z])', ' ', text)
    return spaced_text

text = "ThisIsAnExampleTextWhereWordsAreConcatenated"

spaced_text = add_spaces_between_capital_words(text)

print("Original text:")
print(text)
print("Text with spaces between capital words:")
print(spaced_text)


# In[13]:


#Question 25- Write a Python program to remove duplicate words from Sentence using Regular Expression
import re

def remove_duplicate_words(sentence):
    deduplicated_sentence = re.sub(r'\b(\w+)\b\s+(?=.*\b\1\b)', '', sentence)
    return deduplicated_sentence

sentence = "This is is a sample sentence with duplicate words words."

deduplicated_sentence = remove_duplicate_words(sentence)

print("Original sentence:")
print(sentence)
print("Sentence with duplicate words removed:")
print(deduplicated_sentence)


# In[14]:


#Question 27-Write a python program using RegEx to extract the hashtags.
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

hashtags = extract_hashtags(text)

print("Hashtags extracted from the text:")
print(hashtags)


# In[ ]:





# In[16]:


#Question 30- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
def replace_space_comma_dot_with_colon(text):
    replacements = [' ', ',', '.']
    for char in replacements:
        text = text.replace(char, ':')
    return text

text = 'Python Exercises, PHP exercises.'

replaced_text = replace_space_comma_dot_with_colon(text)

print("Original text:")
print(text)
print("Text with space, comma, and dot replaced by colon:")
print(replaced_text)


# In[ ]:




