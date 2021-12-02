import numpy

def main():
    position = [0, 0]
    with open("input.txt") as file:
        lines = file.readlines()
    
    for line in lines:
        components = line.split(" ")
        direction = components[0]
        distance = components[1]

        axis = None
        multiplier = 1

        if direction == "forward":
            axis = 0
        elif direction == "down":
            axis = 1
        elif direction == "up":
            axis = 1
            multiplier = -1
        
        if distance != None and axis != None:
            position[axis] += int(distance)*multiplier
        
    print(position)
    print(numpy.prod(position))


if __name__ == "__main__":
    main()