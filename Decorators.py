def divide(a, b):                   # defined a function.
    print("result is = ", a/b)

def smart_divide(original_function):    #using this function to add extra features to the above function. this method is called DECORATORS.
    def checker(a, b):                   #funtion will check for the condition.
        if a < b :
            a, b = b, a
        return original_function(a,b)   #call the original function divide(a, b).
    return checker                      #call the checker function to check the condition.

divide = smart_divide(divide)
divide(2,4)

#Decorators are nothing but, changing the feature of a function without altering the body of that particular function.