from itertools import permutations

def numberMinimization(n, d):
    n = int(n)
    seen = set()
    stack = [n]
    ct = 0
    while stack:
        ct += 1
        node = stack.pop()
        for nei in get(node, d):
            if nei not in seen:
                seen.add(nei)
                stack.append(nei)
        if ct > 10000: return min(seen)
    return min(seen)

def get(n, d):
    for cand in permutations(str(n)):
        x = int("".join(cand))
        yield x
        if x % d: continue
        yield int(x/d)