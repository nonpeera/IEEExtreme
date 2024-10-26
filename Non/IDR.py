def permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for e in permutations(s[:-1]):
            for i in range(len(e)+1):
                perms.append(e[:i] + s[-1] + e[i:])
        return perms
for i in permutations("123"):
    s1 = ""
    s2 = ""
    if i[0:(len(i)+1)//2] == s1.join(sorted(i[0:(len(i)+1)//2])) and i[(len(i)+1)//2-1:len(i)] == s1.join(sorted(i[(len(i)+1)//2-1:len(i)])[::-1]):
        print(i)