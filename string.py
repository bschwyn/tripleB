
# given a string of letters, find the longest substring w/ no repeated characters

# sequence of 2 byte values 65000, [

#chris interview feedback

#my background & experience
#remember to talk about git, docker, elasticsearch, splunk, virtual machines, aws cloud services, sql, linux vs windows

#technical problem
# talk about earlier on about switching

#was there ever a time when I said we should do something and management said no you can't.

#linked-list vs. array seemed [1, 3,1 2,3]


#personal problem


def norepeats(s):
    # say s = abcdefghaabcdefghijkl, abcdefghcadefg
    p1 = 0
    p2 = 0
    n = len(s)
    len_substring = 0
    current_len = 0

    used = []


    while p2 < n:
        if s[p2] not in used:
            current_substring = (p1, p2)
            p2 +=1
            current_len +=1
            used.append(s[p2])
        else:
            if current_len > len_substring:
                # save string indices
                longest_substring = current_substring
            len_substring = current_len

            p1 +=1

    return longest_substring

def noreapts(s):
    pass
    #find longest string w/ no repeated character from a given starting point
    #for each starting point in string, find the longest substring from each starting point