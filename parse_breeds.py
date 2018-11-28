with open('wiki_breeds.txt', 'r') as file:
    counter = 0
    dog_groups = dict()
    for line in file:
        counter += 1
        if (':' in line) and (counter < 272):
            line = line.split(': ')
            dog_groups[line[0]] = line[1]

print