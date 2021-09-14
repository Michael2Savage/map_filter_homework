# Excersize 1
print("Excersize 1")

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

no_spaces = list(filter(lambda x: True if x.strip() == x else False, places))
while("" in no_spaces):
    no_spaces.remove("")
print(no_spaces)



# Excersize 2
# Hint: Use the ".sort()" method and access the key"
print("Excersize 2")

authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def seperate_name():
    new_list = []
    for author in authors:
        split_name =  author.split()
        last_name = split_name[-1]
        new_list.append(last_name)
    return new_list

print(seperate_name())
    
#Could not for the life of me get the sort or sorted function to work on the new_list variable OR the seperate_name() func.



# Excersize 3
print("Excersize 3")

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

celcius_convert = list(map(lambda x:  y*(9/5) + 32, places))
print(celcius_convert)