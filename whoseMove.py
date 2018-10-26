def whoseMove(lastPlayer, win):
    if not win:
        if lastPlayer == "black":
            return "white"
        else:
            return "black"
    return lastPlayer
