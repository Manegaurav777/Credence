# 1)Write a program to detect double spaces in a string. (count of double space or count of any char)

from itertools import count
a="my_name_is_gaurav"
print(a.count("_"))


#2) Write a program to detect double spaces in a string. (count of double space or count of any char)



print("Dear  Candidate,\n\t We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.\n\tThank you,\n\tHR ")

#3) From above solution (2) replace ‘Candidate’ with your name and HR name with some other name. By using some string operation function
string="Dear  Candidate,\n\t We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.\n\tThank you,\n\tHR "

print(string.replace("Candidate","Gaurav"))


#4) Replace the double spaces from problem 3 with single spaces
string="Dear  Candidate,\n\t We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.\n\tThank you,\n\tHR "

print(string.replace("  "," "))