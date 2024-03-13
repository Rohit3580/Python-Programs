"""Count the number of strings where the string length is 2 or more and the first
 and last character are same from a given list of strings"""


def check(lst):
    icnt = 0
    for i in lst:
        if len(i) > 2 and i[0] == i[-1]:
            icnt = icnt+1

    print(icnt)



word = ['acw', 'ac','121','ada','az','222']
check(word)