# a program which let you count the total characters in the sentence and also what character appear how much time that is also told in putput by the software.
import collections


from collections import Counter

user_input=input("type please:\n")
modified=user_input.replace(" ", "")
#print(collections.Counter(modified))
char_count={}
char_count=collections.Counter(modified)
#print(char_count)
for x in char_count.items():
    print(x)
Temp=0
for y in char_count.values():
    y=Temp+y
    #print(y)
    Temp=y
print(f"The total number of characters used in your typing is: {Temp}")
print("Thank you for using Character Counter")









    
      
      






