import sys

with open("input.txt") as file:
    day_3_input = file.read().split("\n")

first_wire = day_3_input[0].split(",")
second_wire = day_3_input[1].split(",")

first_wire_t1 = ['R8','U5','L5','D3']
second_wire_t1 = ['U7','R6','D4','L4']

first_wire_t2 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
second_wire_t2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

first_wire_t3 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']        
second_wire_t3 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

def trace_wire(wire_moves):
    wire_coords = [] # start as list so can see the order
    row = 0
    col = 0
    for ins in wire_moves:
        direction = ins[0]
        distance = ins[1:] 
        if direction == "R":
            for j in range(1,int(distance) + 1):
              col += 1
              wire_coords.append((col, row))
        if direction == "L":
            for j in range(1,int(distance) + 1):
              col -= 1
              wire_coords.append((col, row))
        if direction == "U":
            for j in range(1,int(distance) + 1):
              row += 1
              wire_coords.append((col, row))
        if direction == "D":
            for j in range(1,int(distance) + 1):
              row -= 1
              wire_coords.append((col, row))
    
    return set(wire_coords)

def get_overlap(set_1, set_2):
    return list(set_1.intersection(set_2))

def get_manhatten(coords):
    shortest_distance = abs(coords[0][0]) + abs(coords[0][1])
    for coord in coords:
        distance = abs(coord[0]) + abs(coord[1])
        if (distance < shortest_distance):
            shortest_distance = distance
    return shortest_distance
        
def get_solution(wire_1, wire_2):
    return get_manhatten(get_overlap(trace_wire(wire_1), trace_wire(wire_2)))

if get_solution(first_wire_t1, second_wire_t1) != 6:
    print("Error - not working for test 1.",
          "Answer should be 6 but program finds:",
          get_solution(first_wire_t1, second_wire_t1))
elif get_solution(first_wire_t2, second_wire_t2) != 159:
    print("Error - not working for test 1.",
          "Answer should be 159 but program finds:",
          get_solution(first_wire_t2, second_wire_t2))
elif get_solution(first_wire_t3, second_wire_t3) != 135:
    print("Error - not working for test 1.",
          "Answer should be 159 but program finds:",
          get_solution(first_wire_t3, second_wire_t3))

print("solution to part 1:", get_solution(first_wire, second_wire))

def get_distance_to_intersection(wire, overlaps):
    target_col = overlaps[0]
    target_row = overlaps[1]
    col = 0
    row = 0
    steps = 0
    for ins in wire:
        direction = ins[0]
        distance = ins[1:] 
        if direction == "R":
            for j in range(1,int(distance) + 1):
              col += 1
              steps +=1
              if row == target_row and col == target_col:
                  return steps
        if direction == "L":
            for j in range(1,int(distance) + 1):
              col -= 1
              steps +=1
              if row == target_row and col == target_col:
                  return steps
        if direction == "U":
            for j in range(1,int(distance) + 1):
              row += 1
              steps +=1
              if row == target_row and col == target_col:
                  return steps
        if direction == "D":
            for j in range(1,int(distance) + 1):
              row -= 1
              steps +=1
              if row == target_row and col == target_col:
                  return steps
    
    return "No intersection found"

get_distance_to_intersection(first_wire_t1, (0,1))

def get_shortest_distance(first_wire, second_wire):
    overlap = get_overlap(trace_wire(first_wire), 
                          trace_wire(second_wire))
    distances = set()
    for point in overlap:
        distances.add(get_distance_to_intersection(first_wire, point) + 
                get_distance_to_intersection(second_wire, point))
    return min(distances)
        
if get_shortest_distance(first_wire_t1, second_wire_t1) != 30:
    print("Error - not working for test 1.",
          "Answer should be 30 but program finds:",
          get_shortest_distance(first_wire_t1, second_wire_t1))
elif get_shortest_distance(first_wire_t2, second_wire_t2) != 610:
    print("Error - not working for test 1.",
            "Answer should be 159 but program finds:",
          get_shortest_distance(first_wire_t2, second_wire_t2))
elif get_shortest_distance(first_wire_t3, second_wire_t3) != 410:
    print("Error - not working for test 1.",
            "Answer should be 159 but program finds:",
          get_shortest_distance(first_wire_t3, second_wire_t3))

print("solution to part 2:", get_shortest_distance(first_wire, second_wire))




