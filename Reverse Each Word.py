from sys import stdin


def reverseEachWord(string) :
    words=string.split(" ")
    newwords=[word[::-1] for word in words]
    newstring=" ".join(newwords)
    return newstring
	# Your code goes here


























	



#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
