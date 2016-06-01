#Zhizhou Wang
#May 23, 2016
#Homework 1

year_of_birth = int(input("What year were you born in?"))

if year_of_birth > 2016 :
    year_of_birth = int(input("You're not born yet? Tell me the truth. What year were you born in?"))

age = 2016 - year_of_birth
heartbeat = 115200 * age * 365
bluewhale = 10 * 60 * 24 * age * 365
rabbit = 150 * 60 * 24 *365 * age / 1000000000
venus = age / 24 * 39
neptune = age / 247.92065
myAge = 24

print("You are approximately", str(age) , "years old.")
print("Your heart has beaten", str(heartbeat), "times.")
print("A blue whale's heart has beaten" , str(bluewhale), "times.")
print("A rabbit's heart has beaten", str(rabbit), "billion times.")
print("Your age in Venus years is", str(venus),"years old.")
print("Your age in Neptune years is", str(neptune), "years old.")

if age == myAge:
    print("Oh! We're at the same age!")
elif age > myAge:
    print("You're", age - myAge ,"years older than me, yeah!")
else:
    print("Well, you're", myAge - age, "years younger than me, you win.")

if year_of_birth % 2 == 0 :
    print("You were born in an even year!")
else:
    print("You were born in an odd year!")

if year_of_birth < 1974:
    print("Pittsburgh Steelers have won the Superbow 6 times since your birth.")
elif year_of_birth < 1975:
    print("Pittsburgh Steelers have won the Superbow 5 times since your birth.")
elif year_of_birth < 1978:
    print("Pittsburgh Steelers have won the Superbow 4 times since your birth.")
elif year_of_birth < 1979:
    print("Pittsburgh Steelers have won the Superbow 3 times since your birth.")
elif year_of_birth < 2005:
    print("Pittsburgh Steelers have won the Superbow 2 times since your birth.")
elif year_of_birth < 2008:
    print("Pittsburgh Steelers have won the Superbow 1 times since your birth.")
else:
    print("Pittsburgh Steelers have not won any Superbow since your birth.")

if year_of_birth < 1933:
    print("You're too old, I don't know who's the US president when you were born.")
elif year_of_birth < 1945:
    print("Franklin D. Roosevelt was in office when you were born.")
elif year_of_birth == 1945:
    print("Franklin D. Roosevelt was in office when you were born if you were born before March, otherwise Harry S. Truman was in office.")
elif year_of_birth < 1953:
    print("Harry S. Truman was in office when you were born.")
elif year_of_birth == 1953:
    print("Harry S. Truman was in office when you were born if you were born before April, otherwise Dwight D. Eisenhower was in office.")
elif year_of_birth < 1961:
    print("Dwight D. Eisenhower was in office when you were born.")
elif year_of_birth == 1961:
    print("Dwight D. Eisenhower was in office when you were born if you were born before January 20, otherwise John F. Kennedy was in office.")
elif year_of_birth < 1961:
    print("John F. Kennedy was in office when you were born.")
elif year_of_birth == 1961:
    print("John F. Kennedy was in office when you were born if you were born before November, otherwise Lyndon B. Johnson was in office.")
elif year_of_birth < 1969:
    print("Lyndon B. Johnson was in office when you were born.")
elif year_of_birth == 1969:
    print("Lyndon B. Johnson was in office when you were born if you were born before January 20, otherwise Richard Nixon was in office.")
elif year_of_birth < 1974:
    print("Richard Nixon was in office when you were born.")
elif year_of_birth == 1974:
    print("Richard Nixon was in office when you were born if you were born before August, otherwise Gerald Ford was in office.")
elif year_of_birth < 1977:
    print("Gerald Ford was in office when you were born.")
elif year_of_birth == 1977:
    print("Gerald Ford was in office when you were born if you were born before January 20, otherwise Jimmy Carter was in office.")
elif year_of_birth < 1981:
    print("Jimmy Carter was in office when you were born.")
elif year_of_birth == 1981:
    print("Jimmy Carter was in office when you were born if you were born before January 20, otherwise Ronald Reagan was in office.")
elif year_of_birth < 1989:
    print("Ronald Reagan was in office when you were born.")
elif year_of_birth == 1989:
    print("Ronald Reagan was in office when you were born if you were born before January 20, otherwise George H. W. Bush was in office.")
elif year_of_birth < 1993:
    print("George H. W. Bush was in office when you were born.")
elif year_of_birth == 1993:
    print("George H. W. Bush was in office when you were born if you were born before January 20, otherwise Bill Clinton was in office.")
elif year_of_birth < 2001:
    print("Bill Clinton was in office when you were born.")
elif year_of_birth == 2001:
    print("Bill Clinton was in office when you were born if you were born before January 20, otherwise George W. Bush was in office.")
elif year_of_birth < 2009:
    print("George W. Bush was in office when you were born.")
elif year_of_birth == 2009:
    print("George W. Bush was in office when you were born if you were born before January 20, otherwise Barack Obama was in office.")
else:
    print("Barack Obama was in office when you were born.")
