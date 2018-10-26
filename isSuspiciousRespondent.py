def isSuspiciousRespondent(ans1, ans2, ans3):
    if ans1 and ans2 and ans3:
        return True
    elif not ans1 and not ans2 and not ans3:
        return True
    
    return False
