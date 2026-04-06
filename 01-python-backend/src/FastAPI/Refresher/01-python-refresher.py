# Zoo

zoo = ['Lion', 'Tiger', 'Polar Bear', 'Penguin', 'Hyena']

zoo.pop(2)

print(zoo)

zoo.append('Polar Bear')

print(zoo)


print(zoo[0:3])




# Print each element of my list 3 times

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in my_list:
    count = 0
    if day == "Monday": # Skip Monday
        continue
    while count <= 2:
        print(day)
        count += 1


my_vehicle = {
    "model": "Explorer",
    "make": "Ford",
    "year": 2018,
    "mileage": 40000,
}

for key, value in my_vehicle.items():
    print(key, value)

my_vehicle2 = my_vehicle.copy()

my_vehicle2["number_of_tires"] = 4

print(my_vehicle, my_vehicle2)


for key, value in my_vehicle.items():
    print(key)



def name_age_dict(first_name: str, last_name: str, age: int) -> dict:
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
    }

print(name_age_dict("John", "Doe", 129))