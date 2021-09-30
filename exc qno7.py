def birthday(input):
    if input=="parvathi":
        print(input,"birthday is",data["parvathi"])
    elif input=="navya":
        print(input,"birthday is",data[navya])
    elif input=="geeta":
        print(input,"birthday is",data["geeta"])
    else:
        print("the input you gave is not in our dictonary")
    return 0
data={
        'Parvathi': '07/09/2000',
        'navya': '07/14/2000',
        'geeta': '08/26/1999',}
print('This is the birthday dictionary. I know the birthdays of:')
for names in data:
        print(names)

input=input('Who\'s birthday do you want to look up?')
birthday(input)