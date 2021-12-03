def main():
    with open("input.txt") as file:
        lines = file.readlines()
    
    # Generate a list of lists, where bits[n] is a list of all values of the nth bit from each input line.
    bits = [[line[x] for line in lines] for x in range(len(lines[0])-1)]

    # Pick the most common character from each list in bits
    gamma = ''.join([collections.Counter(''.join(bit)).most_common(1)[0][0] for bit in bits])
    
    # Replace all ones with zeroes and vice versa of the gamma value
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

    print(int(gamma, base=2) * int(epsilon, base=2))

if __name__ == "__main__":
    import collections
    main()