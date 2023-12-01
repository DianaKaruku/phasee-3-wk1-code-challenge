def solve(word):
    def consonant_value(substr):
        return sum(ord(char) - ord('a') + 1 for char in substr)

    vowels = "aeiou"
    consonant_substrings = [s for s in word if s not in vowels]
    values = [consonant_value(substr) for substr in ''.join(consonant_substrings).split('a')]

    return max(values)