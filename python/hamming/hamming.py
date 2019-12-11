def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The two compared strings must be the same length.")
    i = 0
    differences = 0
    while i < len(strand_a):
        if strand_a[i] != strand_b[i]:
            differences = differences + 1
        i = i + 1
    return differences
