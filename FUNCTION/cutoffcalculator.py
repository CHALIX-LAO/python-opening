def cutoff(m,p,c):
     return m + ((p+c)/2)
math= int(input("enter your math score:"))
physics= int(input("enter your physics score:"))    
chemistry= int(input("enter your chemistry score:"))
co= cutoff(math,physics,chemistry)
print("your cutoff score is:",co)
