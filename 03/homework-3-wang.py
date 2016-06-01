# Zhizhou Wang
# May 29, 2016
# Homework 3

# LISTS
# Make a list called "countries"
countries = ["China", "United States", "Japan" , "India", "France", "New Zealand", "Canada"]

# Using a for loop, print each element of the list
for i in countries:
    print (i)

# Sort the list permanently.
print(countries.sort())

# Display the first element of the list
print(countries[0])

# Display the second-to-last element of the list
# for i in countries:
#     if i != countries[0]:
#         print (i);
print(len(countries))
t = 0
for i in countries:
    t = t+1
    if t > 1 & t < len(countries) :
        print (countries[t-1])

# Delete one of the countries from the list using its name
countries.remove("India")
print(countries)

# Using a for loop, print each element of the list again
for i in countries:
    print (i)

# DICTIONARIES
# Make a dictionary called 'tree'
tree = {"name":"Tree of life","species":"Mesquite","age":400,"location_name":"Bahrain","latitude":26.0667, "longitude":50.5577}

# Print the sentence
print (tree["name"],"is a",tree["age"],"years old tree that is in",tree["location_name"])

#  Check to see if the tree is south of NYC
New_York_City = {"latitude":40.7128,"longitude":-74.0059}
if tree["latitude"] > New_York_City["latitude"]:
    print("The tree",tree["name"],"in",tree["location_name"],"is south of NYC.")
else:
    print("The tree",tree["name"],"in",tree["location_name"],"is north of NYC.")

# Ask the user how old they are
age_of_user = int(input("How old are you?"))
if age_of_user > tree["age"]:
    print("Your are",(age_of_user - tree["age"]),"years older than",tree["name"])
else:
    print(tree["name"],"was",tree["age"] - age_of_user,"years old when you were born.")

# LISTS OF DICTIONARIES
# Make a list of dictionaries
five_place = [{"city_name":"Moscow", "latitude":55.7558,"longitude":37.6173},{"city_name":"Tehran","latitude":35.6892,"longitude":51.3890},{"city_name":"Falkland Islands","latitude":-51.7963,"longitude":-59.5236},{"city_name":"Seoul","latitude":37.5665,"longitude":126.9780},{"city_name":"Santiago","latitude":42.8782,"longitude":-8.5448}]
# print(five_place)

# Loop through the list, printing each city's name and whether it is above or below the equator
for i in five_place:
    if i["latitude"]>0:
        print(i["city_name"],"is above the equator.")
    else:
        print(i["city_name"],"is below the equator.")
    if i["city_name"] == "Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

# Loop through the list, printing whether each city is north of south of your tree from the previous section.
for i in five_place:
    if i["latitude"] > tree["latitude"]:
        print(i["city_name"],"is north of the",tree["name"])
    else:
        print(i["city_name"],"is south of the", tree["name"])
