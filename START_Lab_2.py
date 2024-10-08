def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    if word == word[::-1]:
        return True
    else:
        return False


def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    fibonacci_sequence = []
    a, b = 0, 1
    
    while a <= number_val:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence
 
def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    return str1.count(str2)

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    if len(list1) != len(list2):
        return []
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
        
    return sum_list

    

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None
    while True:
        password = input('enter password:')
        if isValidPassword(password):
            return password
        else:
            print("not valid") 

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    
    if len(password) < 8:
        return False
    if not any(letter.isupper() for letter in password):
        return False
    if not any(letter.islower() for letter in password):
        return False
    if not any(letter.isdigit() for letter in password):
        return False
    return True

