def qsort(values=[]):
    if len(values) <= 1:
        return values

    pivot = values[len(values)/2]
    lower,equal,upper = [], [], []
    for i in values:
        if i < pivot:
            lower.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            upper.append(i)
    return qsort(lower) + equal + qsort(upper)

unsorted = [23,2,42,4,23,42,34,2,42,42,342,35,4,7,58,789788,6,4,3,3453,6,46,7]
sortedl = qsort(unsorted)
print '[%s]' % ', '.join(map(str, sortedl))
