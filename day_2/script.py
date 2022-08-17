import sys
import copy 

with open("input.txt") as file:
    day_2_input = file.read().split(",")

day_2_input = [int(i) for i in day_2_input]
p1_input = copy.deepcopy(day_2_input )
p1_input[1] = 12
p1_input[2] = 2

#def split_into_groups(list_of_numbers):
    #counter = 0
    #four_counter = 0
    #while counter <= len(list_of_numbers) - 1:
        #print(list_of_numbers[counter])
        #counter += 1
        #if four_counter = 3: four_counter = 0

#split_into_groups(state_before_1202)
#split_state = state_before_1202

def process_input_nums(input_nums):
    counter = 0
    while counter <= len(input_nums) - 1:
        
        opcode = input_nums[counter]
        
        # for debugging
        #print(input_nums)
        #print(opcode)

        if opcode == 99:
            break
        else:
        # definitions come after checking not 99 in case 99 at end of program 
        # and they can't be assigned
            first_num_position = input_nums[counter + 1]
            second_num_position = input_nums[counter + 2]
            result_position = input_nums[counter + 3]
            first_num = input_nums[first_num_position]
            second_num = input_nums[second_num_position]
            
            if opcode == 1:
                input_nums[result_position] = first_num + second_num
                counter += 4
            elif opcode == 2:
                input_nums[result_position] = first_num * second_num
                counter += 4
            else:
                print(opcode, "not found")

    return(input_nums)       

if process_input_nums([1,0,0,0,99]) != [2,0,0,0,99]:
    print("first test failed")
elif process_input_nums([2,3,0,3,99]) != [2,3,0,6,99]:
    print("second test failed")
elif process_input_nums([2,4,4,5,99,0]) != [2,4,4,5,99,9801]:
    print("third test failed")
elif process_input_nums([1,1,1,4,99,5,6,0,99]) != [30,1,1,4,2,5,6,0,99]:
    print("fourth test failed")

print("answer to part 1:", process_input_nums(p1_input)[0])

def change_input(input, noun, verb):
    new_input = copy.deepcopy(input)
    new_input[1] = noun
    new_input[2] = verb
    return(new_input)

test = copy.deepcopy(day_2_input)
test = change_input(test, 12, 2)
if process_input_nums(change_input(test, 12, 2))[0] != 4090701:
    print("input changer function not working")


def try_values(input, noun, verb):
    new_input = change_input(input, noun, verb)
    output = process_input_nums(new_input)[0]
    return(output)

def seek_input_combo(input, target_output):
    for noun in range(0, 99):
        for verb in range(0, 99):
            output = try_values(input, noun, verb)
            if output == target_output:
                return(100 * noun + verb)

if seek_input_combo(day_2_input, 4090701) != 1202:
    print("seek input function not working")

print("answer to part 2:", seek_input_combo(day_2_input, 19690720))

