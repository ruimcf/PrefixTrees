def naive(text, pattern):
    for i in range((len(text)-len(pattern))+1):
        for j in range(len(pattern)):
            if pattern[j] != text[i+j]:
                break;
            if(j == len(pattern)-1):
                print("Pattern found")

def KMP(text, pattern):
    pi = computePiArray(pattern)
    q = 0
    for i in range((len(text)-len(pattern))+1):
        while q > 0 and pattern[q+1] != text[i]:
            q = pi[q]
        if pattern[q+1] == text[i]:
            q = q + 1
        if q == len(pattern):
            print("Pattern found")
            q = pi[q]


def computePiArray(pattern):
    pi = []
    pi.append(0)
    for i in range(1, len(pattern)):
        pi.append(0)
        for j in range(1,i+1):
            if pattern[0:j] == pattern[i-j+1:i+1]:
                pi[i] = j
    return pi




if __name__ == "__main__":
    text = "Hello World"
    pattern = "l"
    computePiArray(pattern)
    KMP(text, pattern)
