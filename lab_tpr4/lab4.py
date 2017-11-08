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

def relative_majority(profiles, profiles_weight):
    result = defaultdict(int)
    for i in range(len(profiles[0])):
        result[profiles[0][i]] += profiles_weight[i]
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
    return "can't be find"

def alternative_votes_method(profiles, profiles_weight):
    result = defaultdict(int)
    profiles_count = len(profiles[0])
    last = len(profiles[0]) - 1
    while( last > 1 ):
        for iter in range(profiles_count):
            result[profiles[last][iter]] += profiles_weight[iter]

        worst = max(result, key=result.get)

        profiles_tranc = [list(i) for i in zip(* profiles)]
        for profile in profiles_tranc:
            profile.remove(worst)
        profiles = [list(i) for i in zip(* profiles_tranc)]
        result.clear()
        last -= 1

    return relative_majority(profiles, profiles_weight)


print "Winner (relative majority): {}".format(relative_majority(profiles, profiles_weight))
print "Winner (Condorcet): {}".format(condorcet(profiles, profiles_weight))
print "Winner (method of alternative votes): {}".format(alternative_votes_method(profiles, profiles_weight))
