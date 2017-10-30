# Lab 4
_**DECISION-MAKING BY VOTING METHODS**_

Правило (метод) відносної більшості.
```
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
```
Правило Кондорсе.
```
def condorcet(profiles, profiles_weight):
    profiles_tranc = zip(* profiles)
    results = defaultdict(int)
    for iter in range(len(profiles_weight)):
        for c1, c2 in itertools.combinations(profiles_tranc[iter], 2):
            assert (c1 != c2)
            mini, maxi, res = (c1, c2, profiles_weight[iter]) if c1 < c2 \
                    else (c2, c1, -profiles_weight[iter])
            results[mini, maxi] += res
    for c in {c for profile in profiles_tranc for c in profile}:
        if (all((res > 0 if c == mini else res < 0) \
                for (mini, maxi), res in results.items() if c in [mini, maxi])):
            return c
    return "can't be find"
```
Метод альтернативних голосів.
```
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
```