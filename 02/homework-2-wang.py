# Zhizhou Wang
# May 25, 2016
# Homework 2

#Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22,90,0,-10,3,22,48]

#Display the number of elements in the list
print(numbers)

#Display the 4th element of this list.
print(numbers[3])

#Display the sum of the 2nd and 4th element of the list.
print(numbers[1] + numbers[3])

#Display the 2nd-largest value in the list.
sorted_numbers=sorted(numbers,reverse=True)
print(sorted_numbers[1])

#Display the last element of the original unsorted list
#print(len(numbers)) #7
print(numbers[len(numbers) - 2])

# For each number, display a number:
for i in numbers:
    answer = i
    if i < 10:
        answer = answer * 30
    if i % 2 == 0:
            answer = answer + 6
    if i != -10:
                answer = answer -1
    print(answer)

#Sum the result of each of the numbers divided by two.
result = 0
for i in numbers:
    result = result + i/2
print (result)

#Define a dictionary called movie that works with the following code
movie = {"title":"Captain America","year":2011, "director":"Joe Johnston"}
print("My favorite movie is", movie["title"] , "which was released in",movie["year"],"and was directed by",movie["director"])

# Add entries to the movie dictionary for budget and revenue
movie["budget"]=140
movie["revenue"]=370
print(abs(movie["revenue"]-movie["budget"]))

# If the movie cost more to make than it made in theaters, print "It was a flop". If the film's revenue was more than five times the amount it cost to make, print "That was a good investment."
if movie["revenue"] < movie["budget"]:
    print("It was a flop")
elif movie["revenue"] > (movie["budget"]*5):
    print("That was a good investment")
else:
    print("So so")

#Make ONE dictionary that describes the population of the boroughs of NYC
population = {"Manhattan":1600,"Brooklyn":2600,"Bronx":1400,"Queens":2300,"Staten Island":470}

#Display the population of Brooklyn.
print("The population of Brooklyn is",population["Brooklyn"],"thousands.")

#Display the combined population of all five boroughs.
print(sum(population.values()),"thousands")

#Display what percent of NYC's population lives in Manhattan.
total = sum(population.values())
print(str(round(population["Manhattan"]/total*100,2))+"%")
