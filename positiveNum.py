def exactly_two_positive(a, b, c):
    positive_count = sum(x > 0 for x in (a, b, c))
    return positive_count == 2