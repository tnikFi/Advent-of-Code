def main():
    with open("input.txt") as file:
        lines = file.readlines()
    
    samples_increased = 0
    previous_line = None

    for line in lines:
        if previous_line and int(line) > previous_line:
            samples_increased += 1
        
        previous_line = int(line)
    
    print(samples_increased)

if __name__ == "__main__":
    main()