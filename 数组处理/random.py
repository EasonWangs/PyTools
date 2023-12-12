import hashlib


def get_winners(min_n, max_n, num_win, key):
    res = key
    print(type(res),res)

    winners = set()
    while len(winners) < num_win:
        res = hashlib.sha256(res).hexdigest()
        print(type(res), res)
        res = int(res, 16)
        print(type(res), res)
        delat = (max_n-min_n+1)
        winners.add( res % delat + min_n)
    print(winners)
    return winners

get_winners(1,900,1,b'000000000000000000093aab34c7ed58261ae9dd96f082e7487928bc21f53faa')