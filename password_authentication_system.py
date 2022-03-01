import getpass
def pass_auth_sys():
    user_pass_dict={'vishal_vs':'9999','harsh_vs':'5678','bhagwan':'1234'}
    username=input("Enter Your Username: ")
    password=getpass.getpass("Enter your Password: ")
    for i in user_pass_dict.keys():
        if username==i:
            while password!=user_pass_dict[username]:
                password=getpass.getpass("Enter your password again:")
            break
    print("Verified")