def difference(l1, l2):
    lijst = l1 + l2
    i = 0
    j = 0
    k = 0
    gemeenschappelijk = []
    lijst.sort()

    while i < len(lijst) - 1:
        if lijst[i] == lijst[i + 1]:
            gemeenschappelijk.append(lijst[i])
            lijst.pop(i)
            lijst.pop(i)
        else:
            i = i + 1
    difren = l2 + gemeenschappelijk
    Luit = lijst + difren
    Luit.sort()

    while k < len(difren) - 1:
        if difren[k] == difren[k + 1]:
            difren.pop(k)
            difren.pop(k)
        else:
            k = k + 1

    while j < len(Luit) - 1:
        if Luit[j] == Luit[j + 1]:
            Luit.pop(j)
            Luit.pop(j)
        else:
            j = j + 1

    return Luit