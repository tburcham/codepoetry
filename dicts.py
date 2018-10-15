person = {
    "first_name": "Karl",
    "last_name": "Marx",
    "age":235,
    "pet": {
        "name":"Proleterry",
        "species": "parrot",
        "age": 12
    }
}

print(person)
print(person["age"])
print(person.get("abc")) # returns a truthy/falsy None if not found

for key in person:
    print(key)
    print(person[key])
