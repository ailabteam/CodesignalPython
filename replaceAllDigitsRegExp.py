def replaceAllDigitsRegExp(inputString):
    return  "".join(['#' if char.isdigit() else char for char in inputString])
