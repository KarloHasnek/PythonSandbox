
def longest_palindrom(s):
    n = len(s)
    longest = ''
    for i in range(n):
        for j in range(i+1, n+1):
            word = s[i:j]
            if word == word[::-1]:
                if len(word) > len(longest):
                    longest = word
    return longest


def main():
    s = input("Unesi proizvoljan niz za provjeru najduljeg palindroma: ")
    print(longest_palindrom(s))


main()
