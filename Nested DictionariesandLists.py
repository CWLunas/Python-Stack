#1.0

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1
x[1][0]=15
print (x)
#1.2
students[0]['last_name'] = "Bryant"
print (students[0]['last_name'])
#1.3
sports_directory['soccer'][0] = "Andres"
print (sports_directory['soccer'][0])
#1.4
z[0]['y']=30
print (z[0]['y'])
print (z)

#2.0
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(name_list):
    for x in range(0, len(name_list),1):
        student = ""
        for k,v in name_list[x].items():
            student = student + f"{k} - {v},"
        print(student)

iterate_dictionary(students)


#3.0
def iterate_dictionary2(key_item, new_list):
    for x in range(0, len(new_list),1):
        for k,v in new_list[x].items():
            if k == key_item: 
                print(v)

iterate_dictionary2('first_name',students)
iterate_dictionary2('last_name',students)

#4.0
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dojo_dict):
    for k,v in dojo_dict.items():
        print (f'{len(v)} {k.upper()}')
        for attribute in v:
            print (attribute)

print_info(dojo)



