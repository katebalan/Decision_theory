import operator

train_document = open('1.txt', 'r')

profile = []
for line in train_document:
    profile.append([])
    for symbol in line.split():
        profile[len(profile) - 1].append(symbol)

train_document.close()
print profile

def relative_majority(profile):
    result = {}
    for i in range(len(profile[0])):
        if profile[1][i] not in result:
            result[profile[1][i]] = int(profile[0][i])
        else:
            temp = result[profile[1][i]]
            result[profile[1][i]] = int(profile[0][i]) + temp

    winner = max(result.iteritems(), key = operator.itemgetter(1))[0]
    return winner

def condorcet(profile):
    pass


print "Winner (relative majority): {}".format(relative_majority(profile))
