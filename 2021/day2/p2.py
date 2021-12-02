import numpy

def main():
    aim = 0
    position = [0, 0]
    with open("input.txt") as file:
        lines = file.readlines()
    
    for line in lines:
        components = line.split(" ")
        direction = components[0]
        distance = int(components[1])

        if direction == "forward":
            position[0] += distance
            position[1] += aim*distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    print(position)
    print(numpy.prod(position))


if __name__ == "__main__":
    main()