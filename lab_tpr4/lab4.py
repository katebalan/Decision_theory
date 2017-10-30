# import operator
import itertools
from collections import defaultdict

document1 = open('1.txt', 'r')

profiles = []
print "Profiles: "

for line in document1:
    profiles.append([])
    for symbol in line.split():
        profiles[len(profiles) - 1].append(symbol)
    print profiles[len(profiles) - 1]

document1.close()

document2 = open('2.txt', 'r')

profiles_weight = []
for number in document2.readline().split():
    profiles_weight.append(int(number))

document2.close()

print "Profiles weight: {}".format(profiles_weight)

def relative_majority(profiles, profile_weight):
    result = {}
    for i in range(len(profiles[0])):
        if profiles[0][i] not in result:
            result[profiles[0][i]] = int(profile_weight[i])
        else:
            temp = result[profiles[0][i]]
            result[profiles[0][i]] = int(profile_weight[i]) + temp
    winner = max(result, key=result.get)
    return winner

def condorcet(profiles, profiles_weight):
    profiles_tranc = zip(* profiles)
    results = defaultdict(int)
    for iter in range(len(profiles_weight)):
        for c1, c2 in itertools.combinations(profiles_tranc[iter], 2): # combinations('ABCD', 2) --> AB AC AD BC BD CD
            assert (c1 != c2)
            mini, maxi, res = (c1, c2, profiles_weight[iter]) if c1 < c2 else (c2, c1, -profiles_weight[iter])
            results[mini, maxi] += res
    for c in {c for profile in profiles_tranc for c in profile}:
        # TO DO understand if statement
        if (all((res > 0 if c == mini else res < 0) for (mini, maxi), res in results.items() if c in [mini, maxi])):
            return c
    return None


print "Winner (relative majority): {}".format(relative_majority(profiles, profiles_weight))
print "Winner (Condorcet): {}".format(condorcet(profiles, profiles_weight))
