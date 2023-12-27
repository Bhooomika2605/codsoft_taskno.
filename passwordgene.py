import random
import string
print("---Random password generate---")  
while True: 
   
    def generate_random_number(length):
        if length <= 0:
            print("What length of password do you want should be a positive integer")

        random_number = ''.join(random.choice('0123456789') for _ in range(length))

        return int(random_number)

    def generate_random_password(length):
            characters = string.ascii_letters
            password=''.join(random.choice(characters) for _ in range(length))
            return password
    
    print("Type '1' for only dgits \nType '2' for only alpahabet  \nType '3' for alphabet and punctuation  \nType '4' for punctuation and digits")
    type = input("Type of password? ")
    
    if type == '1':
        desired_length = int(input("What length of password do you want? "))
        for _ in range(1):
            result = generate_random_number(desired_length)
            print("The password: ",result)
        
        
    if type == "2":
        desired_length = int(input("What length of password do you want? "))
        for _ in range(1):
            result = generate_random_password(desired_length)
            print("The password: ",result)
    
    
    if type == '3':
        def generate_random_password(length):
            characters = string.ascii_letters+string.punctuation
            password=''.join(random.choice(characters) for _ in range(length))
            return password
        
        desired_length = int(input("What length of password do you want? "))
        for _ in range(1):
            result = generate_random_password(desired_length)
            print("The password: ",result)
    
    
    if type == '4':
        def generate_random_password(length):
            characters = string.ascii_letters+string.punctuation+string.digits
            password=''.join(random.choice(characters) for _ in range(length))
            return password
        
        desired_length = int(input("What length of password do you want? "))
        for _ in range(1):
            result = generate_random_password(desired_length)
            print("The password: ",result)


    if type >= "5" or type =="0":
        print("Invalid! Please enter a valid choice")