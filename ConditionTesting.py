print('Please input your name:')
name = input()
if name == 'Tony':
    print('Hello, Tony')
    print('Input your password:')
    password = input()
    if password == 'megamanzero2':
        print('Access granted.')
    else:
        print('Incorrect password')
        print('Access Denied.')
else:
    print('User not authorized for entry.')
    print('Access Denied.')