import sys

with open("input.txt") as file:
    day_1_input = file.read().splitlines()

module_masses = [int(i) for i in day_1_input]

def get_fuel(mass):
    fuel = (mass // 3) - 2
    return(fuel)

if (get_fuel(100756) != 33583):
    sys.exit("Error: get_fuel function not working")

fuel_needed = 0
for mod in module_masses:
    fuel_needed += get_fuel(mod)

print("solution to part 1:", fuel_needed)

def get_fuel_corrected(mass):
    total_fuel = get_fuel(mass)
    extra_fuel = get_fuel(mass)
    while get_fuel(extra_fuel) > 0:
      total_fuel += get_fuel(extra_fuel)
      extra_fuel = get_fuel(extra_fuel)
    return total_fuel

if (get_fuel_corrected(100756) != 50346):
    sys.exit("Error: get_fuel_corrected function not working")

corrected_fuel_needed = 0
for mod in module_masses:
    corrected_fuel_needed += get_fuel_corrected(mod)

print("solution to part 2:", corrected_fuel_needed)

