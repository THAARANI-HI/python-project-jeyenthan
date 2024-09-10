#password guessing

password="Jeyenthan"
user_password=input("enter the password:")
while password!=user_password:
    print("wrong password")
    user_password=input("enter the password:")
print("password is correct")