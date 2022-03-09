#1a) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
def changeto15():
    x = [ [5,2,3], [10,8,9] ] 
    x[1][0]=15
    print(x)
changeto15()


#1b) Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {
        'first_name':  'Michael',
        'last_name' : 'Jordan'
        },
    {
        'first_name' : 'John',
        'last_name' : 'Rosales'
        }
]

def jordanBryant():
    students[0].update({"last_name": "Bryant"})
    print(students)
jordanBryant()


#1c) In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def messiAndres():
    sports_directory['soccer'][0] = 'Andres'
    print(sports_directory['soccer'])
messiAndres()


#1d) Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

def yto30():
    z[0].update({"y": 30})
    print(z)
yto30()

#2) Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(len(students)):
        firstName = students[i]['first_name']
        lastName = students[i]['last_name']
        print(f"first_name - {firstName}, last_name - {lastName}")
print(iterateDictionary(students))



#3)Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(key_name, list_of_dictionaries):
    for dictionary in list_of_dictionaries:
        print(dictionary[key_name])
iterateDictionary("first_name", students)

def iterateDictionary(key_name, list_of_dictionaries):
    for dictionary in list_of_dictionaries:
        print(dictionary[key_name])
iterateDictionary("last_name", students)

#4)Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def iterateDictionary(dictionary_of_lists):
    for key in dictionary_of_lists:
        print(len(dictionary_of_lists[key]), key)
        for value in dictionary_of_lists[key]:
            print(value)
print(iterateDictionary(dojo))