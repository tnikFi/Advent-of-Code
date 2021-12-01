def main():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [int(x) for x in lines]
    
    samples_increased = 0

    for index, line in enumerate(lines):
        if index + 4 <= len(lines):
            sum1 = sum(lines[index:index+3])
            sum2 = sum(lines[index+1:index+4])
            if sum2 > sum1:
                samples_increased += 1
        else:
            break
    
    print(samples_increased)

if __name__ == "__main__":
    main()