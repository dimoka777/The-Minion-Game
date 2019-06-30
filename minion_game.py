"""
Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring
A player gets +1 point for each occurrence of the substring in the string .
"""
string = input()

vowels = 'aeiou'.upper()
strl = len(string)
kevin = sum(strl-i for i in range(strl) if string[i] in vowels)
stuart = strl*(strl + 1)/2 - kevin

if kevin == stuart:
    print('Draw')
elif kevin > stuart:
    print('Kevin %d' % kevin)
else:
    print('Stuart %d' % stuart)
