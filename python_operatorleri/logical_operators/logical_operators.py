x = 6
hak = 5
devam = "e"



# and

# True, True =>  True
# Ture, False =>  False
# False, False => False

result = (x > 5) and (x < 10)
result = (hak > 0) and (devam == "e")



# or

# True, False => True
# True, True => True
# False, False => False

result = (x > 0) or (x % 2 == 0)

# not

result = not(x > 0)

result = ((x > 5) or (x < 10)) and (x % 2 == 0)



print(result)