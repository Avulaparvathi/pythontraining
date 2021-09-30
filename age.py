name=input("enter name")
age=int(input("enter age"))
year=str((2021-age)+100)
print(name+ " will be 100 years old in the year " +year)


def age(name,age):
    year = str((2021 - age) + 100)
    print(name + " will be 100 years old in the year " + year)
    return 0
age("parvathi",21)