def find(items: list=[], index: int=0) -> str:
    items = items.copy()
    for i in range(len(items[0])):
        # Loop break condition
        if len(items) == 1:
            break
        
        s = ''.join([x[i] for x in items])
        
        condition = collections.Counter(s).most_common(2)
        if len(condition) > 1:
            if condition[0][1] == condition[1][1]:
                condition = str(1-index)
            else:
                condition = condition[index][0]
        else:
            condition = condition[0][0]

        items = [x for x in items if x[i] == condition]
    
    return items[0]

def main():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [x.replace("\n", "") for x in lines]
    
    o2 = find(lines, 0)
    co2 = find(lines, 1)

    print(int(o2, base=2) * int(co2, base=2))

if __name__ == "__main__":
    import collections
    main()