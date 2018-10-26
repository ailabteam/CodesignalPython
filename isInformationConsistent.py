def isInformationConsistent(evidences):
    ans = [0]*len(evidences[0])
    for r in evidences:
        for i,x in enumerate(r):
            if x != 0 and x + ans[i] == 0:
                return False
            elif ans[i] == 0:
                ans[i] = x
    return True