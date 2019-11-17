def add(*args):
    total = 0
    for item in args:
        total += item
    
    return total

print (add(1, 2, 3, 4))
# *args means you can put as many parameters as you would like
#when you refer to args you don't use the *