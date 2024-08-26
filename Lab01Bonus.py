#
# Myiah Vanderheyden
# 08/22/2024
# This program calculates the time it takes to travel
# a certain distance going a specific speed.
#
# This program also demonstrates my ability to convert part of an
# hour to minutes
#
# Note: The miles and speed entered could be a floating point
# number.
#

MINUTES_IN_HOUR = 60

# Get the number of miles.
miles = float(input('Enter number of miles: '))

# Get the speed in MPH.
speed = float(input('Enter speed in MPH: '))

# Calculate the travel time.
# 08/22/24 added new conversion to hours and minutes instead
# of just a decimal representation
travel_time_hours = miles // speed
travel_time_minutes = ((miles % speed) / speed) * MINUTES_IN_HOUR
# above calculation uses the remainder and divides it by the denominator
# to get the decimal value that will be multiplied by the constant in
# order to produce the minutes


# Display the travel time (formatted to 2 decimal places).
print(f'You should cover that distance in {travel_time_hours:.0f} hours '
      f'and {travel_time_minutes:.2f} minutes.')
# I reviewed previous coursework from CSC120 to help refresh my memory on
# conversions like this
# Source: https://github.com/myiahvdh/CSC121.PYTHON/commit/2e0cff2f3bd47bca4642c4f39dc9c036f5d043c0
