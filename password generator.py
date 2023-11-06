import random
import array

#now fixing the length of password
MAX_LEN=12

DIGITS=['0','1','2','3','4','5','6','7','8','9']

LOWER_CASE=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z']

UPPER_CASE=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
            'R','S','T','U','V','W','X','Y','Z']

SYMBOLS=['!','@','#','$','%','=','<','>','?','/','*',')',':','|','~','&']

COMBINED_LIST= DIGITS + LOWER_CASE + UPPER_CASE + SYMBOLS

#generating random numbers using random function()

rand_digits=random.choice(DIGITS)
rand_lower= random.choice(LOWER_CASE)
rand_upper= random.choice(UPPER_CASE)
rand_symbols= random.choice(SYMBOLS)

temp_pass = rand_digits + rand_lower + rand_upper + rand_symbols

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
    
password = ""
for x in temp_pass_list:
        password = password + x
        
print(password)