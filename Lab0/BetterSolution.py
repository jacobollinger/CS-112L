# Lab 0
# author: Jacob Bollinger and Nathan Massey

# a) Design a solution to convert miles to kilometers.

# Initialize variables.
mi = 10
mkRate = 1.60934

# Convert miles to kilometers and round.
km = round(mi * mkRate, 2)

# Show results.
print (mi, 'miles is equal to', km, 'kilometers')

# b) Design a general solution to convert kilometers per minutes and seconds to miles per hour.

# Initialize variables.
kpm = 2000
kps = 10000
kph2mphRate = 0.621371

# Add kpm and kps and convert to kph.
kph = kpm / 60 + kps / 3600

# Convert kph to mph and round.
mph = round(kph * kph2mphRate, 1)

# Show results.
print(kpm, 'kilometers per minute plus', kps, 'kilometers per second are equal to', mph, 'miles per hour')

# c) Design a solution to convert miles per hour to kilometers per minute.

# Initialize variables.
mph = 50
mph2kpmRate = 1.60934 * 60

# Convert mph to kpm and round.
kpm = round(mph * mph2kpmRate)

# Show results.
print(mph, 'miles per hour is equal to', kpm, 'kilometers per minute')

# d) Design a solution to convert pounds to kilograms.

# Initialize variables.
lb = 46
lb2kgRate = 0.453592

# Convert lb to kg and round.
kg = round(lb * lb2kgRate, 2)

# Show results.
print(lb, 'pounds is equal to', kg, 'kilograms')

# e) Design a solution to convert degrees Fahrenheit to degrees Celsius.

# Initialize variable.
f = 105

# Convert Fahrenheit to Celsius and round.
c = round((f - 32) * 5 / 9)

#Show results.
print(f,'degrees Fahrenheit is equal to', c, 'degrees Celsius.')

