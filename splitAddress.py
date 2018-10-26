def splitAddress(address):
    t = address.split("/")
    res = []
    for i in range(len(t)):
        tmp = t[i].split(":")
        tmp = tmp[0].split(".com")
            
        if tmp[0] != "":
            res.append(tmp[0])
    return res
