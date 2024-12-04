# 1
for i in range(12, 24 + 1, 1):
    print(i, end=" ")
print()

# 2
for i in range(7, 31 + 2, 2):
    print("ODD", i, end=" ")
print()

# 3
for i in range(10, 20 + 1, 2):
    print("EVEN", i, end=" ")
print()

# 4
for i in range(1, 45 + 1, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz(3 and 5)")
    elif i % 3 == 0:
        print("Fizz(*3)")
    elif i % 5 == 0:
        print("Buzz(*5)")
    else:
        print(i)

# 5
def calculates_array(sum_array):
    array=0
    for sum_array in sum_array:
        array+=sum_array
    return array

example_array = [1, 13, 22, 123, 49, 34, 5, 24, 57, 45]
example = calculates_array(example_array)
print(example)

# 6-  לחזור!!
# def del_function(students,objects):
#     for student in students:
#         if objects in student:
#             del student[objects]
#
#
#
# students = [
#     { "id":25023221, "first name":"adi", "last name": "lasri", "age": 25, "country":"israel", "city":"jerusalem" },
#     { "id":31270051, "first name":"deke", "last name": "tal", "age": 30, "country":"israel", "city":"bat yam"},
#     { "id":30209679, "first name":"Yair", "last name": "paz", "age": 28, "country":"israel", "city":"dimona"},
#     { "id":36578901, "first name":"avi", "last name": "zagםri", "age": 40, "country":"israel", "city":"tel aviv"}
# ]
#
# del_function(students,"")
# print(del_function,"לאחר הסרת המאפיין 'עיר':")








#7
our_pets = [
{
"animal_type": "cat",
"names": [
"Meowzer",
"Fluffy",
"Kit-Cat"
]
},
{
"animal_type": "dog",
"names": [
"Spot",
"Bowser",
"Frankie"
]
}
]

#1
def cat(pet_name):
    for name in pet_name:
        if name ["animal_type"] == "cat":
           print(name)
cat(our_pets)

#2
def cat(pet_name):
    for name in pet_name:
        if name ["animal_type"] == "cat":
           print(name)
cat(our_pets)

def dog(pet_name):
    for name in pet_name:
        if name ["animal_type"] == "dog":
           print(name)
dog(our_pets)

#3
def add_name_pet(pets, pet_name):
    for name in pets:
        if pet_name not in name["names"]:
            name["names"].append(pet_name)

new_name = "lucky"
add_name_pet(our_pets, new_name)

print("new name pet:")
print(our_pets)
