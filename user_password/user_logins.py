'''
Bryan Coleman
personal project for python #1
'''

from password_hashing import hash_password

import yaml

def are_credentials_valid():
    print('SIGN IN')
    username = input('Please enter your username: ')
    username = username.lower()
    password = input('Please enter your password: ')
    result = hash_password(password)

    with open('credentials.yml') as f:
        credentials_doc = yaml.safe_load(f)

    for pass_check in credentials_doc:
        if pass_check['username'] == username and pass_check['password_hash'] == result.hexdigest():
            return True
    return False

def main():
    username_password_pair = {}
    #select_exit = True

    
    print('SIGN UP')
    username = input('Please enter your desired username: ')
    username = username.lower()
    password = input('Please enter your desired password: ')
    result = hash_password(password)
    password = ''

    with open('credentials.yml','r') as f:
        credentials_doc = yaml.safe_load(f)

    for new_pass in credentials_doc:
        if new_pass['username'] == username:
            new_pass['password_hash'] = result.hexdigest()
            break
    
    with open('credentials.yml','w') as f:
        yaml.safe_dump(credentials_doc,f,default_flow_style = False)

    if are_credentials_valid():
        print('Welcome. Here is my deepest secret')
    else:
        print('Get lost')

if __name__ == '__main__':
    main()
