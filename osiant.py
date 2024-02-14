import instaloader
from os import system, name

# import sleep to show output for some time period

from time import sleep

# define our clear function

def clear():


    # for windows

    if name == 'nt':

        _ = system('cls')


    # for mac and linux(here, os.name is 'posix')

    else:

        _ = system('clear')

# print out some text

print(' \n'*10)

# sleep for 2 seconds after printing output

sleep(2)

# now call function we defined above
clear()





print("\033[1;32m")


# A simple Python program to demonstrate
# getpass.getpass() to read security question

import getpass
print('''
 ####### ####      #####   ### ###  ###  ### 
  ##   #  ##      ### ###   ## ##    ##  ##  
  ##      ##      ##   ##   ####      ####   
  ####    ##      ##   ##   ###        ##    
  ##      ##      ##   ##   ####       ##    
  ##      ##  ##  ### ###   ## ##      ##    
 ####    #######   #####   ### ###    ####   
                                             
''')

p = getpass.getpass(prompt='enter password: ')


if p=='Flokyismydad':
    clear()
    print('█▓▒▒░░░Remember ~Floky░░░▒▒▓█')
    i = input('Enter target username: ')
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context,i)
    # Print the profile's metadata
    print('User_id',profile.userid)
    print('Username' ,profile.username)
    print('Followers',profile.followers)
    print('Follwoing',profile.followees)
    print('Bio : ',profile.biography)
    print('url',profile.external_url)
    print('Is Private? -',profile.is_private)
    print('Is Verified? -',profile.is_verified)

else:
     print('Invalid')
