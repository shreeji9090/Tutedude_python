School_data = {
    "Raghav":98,
    "Suresh": 78,
    "Mahesh":87,
    "Fogesh":66
}

print(School_data)

name = input("enter name which you want to value of: ")

if name in School_data:
    print(f"{name}'s marks:  {School_data[name]}")
else:
    print(f"School_data '{name}' not found in the record.")

