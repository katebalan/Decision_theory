
train_document = open('1.txt', 'r')

profile = []
for line in train_document:
    profile.append([])
    for symb in line.split():
        profile[len(profile) - 1].append(symb)

train_document.close()
print profile
