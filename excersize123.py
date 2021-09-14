# Excersize 1
print("Excersize 1")

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

no_spaces = list(filter(lambda x: True if x.strip() else False, places))
while("" in no_spaces):
    no_spaces.remove("")
print(no_spaces)



# Excersize 2
# Hint: Use the ".sort()" method and access the key"
print("Excersize 2")

authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def seperate_name(author):
    split_name =  author.split()
    last_name = split_name[-1].lower()
    return last_name

authors.sort(key = seperate_name)
print(authors)


    
#Could not for the life of me get the sort or sorted function to work on the new_list variable OR the seperate_name() func.



# Excersize 3
print("Excersize 3")

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

#celcius_convert = list(map(lambda x:  x[-1]*(9/5) + 32, places))
#print(celcius_convert)

ans = list(map(lambda x : (x[0], (9/5)*x[1]+32), places))
print(ans)