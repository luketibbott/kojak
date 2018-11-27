# Parses a wikipedia page listing dog breeds recognized by the American Kennel Club and the
# group of dog each breed belongs to.

import wikipedia

dog_breeds = wikipedia.page('List of dog breeds recognized by the American Kennel Club')

counter = 0
dog_groups = dict()


for line in dog_breeds.content.split('\n')[1:]:
    counter += 1
    split = False
    # Catch text error with no space after comma
    if (', ' in line) and (counter < 272):
        line = line.split(', ')
        split = True

    elif (',' in line) and (counter < 272):
        line = line.split(',')
        split = True
    # Split being true means the line we're interested in has dog breed info
    if split:
        dog_groups[line[0]] = line[1]

print(dog_groups)