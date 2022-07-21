
def compute_bets(n, m):
    arr = [n]
    for i in range(m - 1):
        arr.append(arr[i]*2)
    return arr

def test(initial_coins, max_losses, model):
    n = model(initial_coins, max_losses)
    bets = compute_bets(n, max_losses)
    print(f'total gambled: {sum(bets)}')
    print(f'your coins: {initial_coins}')
    assert round(sum(bets)) == initial_coins

model = lambda c, m: c/(1 + sum([2*i for i in range(1, m)]))
model2 = lambda c, m: c / sum(map(lambda i: 2**i, range(m)))

def simple_brute_force():
    min_coins = 1000
    max_coins = 10000
    min_bets = 2
    max_bets = 400
    for i in range(min_coins, max_coins):
        for j in range(min_bets, max_bets):
            test(i, j, model2)




