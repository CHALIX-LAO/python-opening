def combo_string(a, b):

    if len(a)<len(b):
        short=a
        longer=b
    else:
        short=b
        longer=a

    return short + longer + short
x=input("Enter the first string: ")
y=input("Enter the second string: ")    
print(combo_string(x, y))