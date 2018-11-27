import wikipedia

dog_breeds = wikipedia.page('List of dog breeds recognized by the American Kennel Club')

counter = 0
dog_groups = dict()

for line in dog_breeds.content.split('\n')[1:]:
    counter += 1
    split = False
    if (', ' in line) and (counter < 272):
        line = line.split(', ')
        split = True

    elif (',' in line) and (counter < 272):
        line = line.split(',')
        split = True
    
    if split:
        dog_groups[line[0]] = line[1]

print(dog_groups)
print(len(dog_groups))