import requests
import random
import string
import time

# import only system from os

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

print('\033[32m')

print('\033[1m')


print('''░▒
                                                                  
 ####### ####      #####   ### ###  ###  ### 
  ##   #  ##      ### ###   ## ##    ##  ##  
  ##      ##      ##   ##   ####      ####   
  ####    ##      ##   ##   ###        ##    
  ##      ##      ##   ##   ####       ##    
  ##      ##  ##  ### ###   ## ##      ##    
 ####    #######   #####   ### ###    ####   
                                             
                                                              
''')
print("Made By @i3mk.floky")



i=input('''PLEASE USE FOR EDUCATIONAL PURPOSE !!

''')

u=input('𝙎𝙀𝙇𝙀𝘾𝙏 𝙍𝙀𝘼𝙎𝙊𝙉 : ')

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
j = input('𝐄𝐧𝐭𝐞𝐫 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : ')
def report(j):
    url = 'https://www.instagram.com/users/report/'
    data = {
        'source_name': 'source',
        'report_type': 'other',
        'selected_reasons': [u],
        'free_form_report': username,
        'is_hidden': False,
        'content_type': '',
        'object_type': '',
        'object_id': '',
        'fb_report_id': '',
        'entry_point': '',
        '__user': '',
        '__a': '',
        '__dyn': '',
        '__csr': '',
        '__req': '',
        '__beoa': '',
        '__pc': '',
        '__bhv': '',
        '__s': ''
    }

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.instagram.com/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-IG-App-ID': '936619743392459',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'close',
    })
    session.cookies.update({
        'ig_did': random_string(32),
        'mid': 'XwF9FQAEAAE8zJ9xg8y5y5Tf2Yw-',
        'ig_nrcb': '1',
        'csrftoken': random_string(32),
    })

    response = session.post(url, data=data)
    if response.status_code == 200:
        print(f'{u} Report sent from {username} ✅')
    else:
        print(f'{u} Failed to send report for {username} ❎')

# Example usage
usernames = ['user1 ', 'user2 ', 'user3 ' , 'user4 ' , 'user5 ' , 'user6 ' , 'user7 ','user8 ','user9 ','user10 ','user11 ','user12 ','user13 ', 'user14 ','user15 ','user16 ' , 'user17 ' , 'user18 ' ,'user 19' ,'user20','user21' , 'user22' , 'user23' , 'user24' ,'user25' ,'user26','user27','user28','user29','user30','user31', 'user32','user33','user34','user35','user36','user37','user38','user39','user40','user41','user42','user43','user44','user45','user46','user47','user48','user49','user50','user51','user53','user54','user55','user56','user57','user58','user59','user60','user61','user62','user63','user64','user65','user66','user67','user68','user69','user70','user71','user72','user73','user74','user75','user76','user77','user78','user79','user80','user81','user82','user83','user84','user85','user86','user87','user88','user89','user90','user91','user92','user93','user94','user95','user96','user97','user98','user99','user100','user101','user102','user103','user104','user105','user106','user107','user108','user109','user110' , 'user111', 'user112','user113','user113','user114','user115','user116','user117','user118','user119','user120','user121',]
for username in usernames:
    report(username)
    time.sleep(1)  # Sleep for 5 seconds to avoid rate limiting
