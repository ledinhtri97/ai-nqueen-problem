q = []

def main():
	N = int(input("Input NxN chess: N = "))

	if(BFS(N,[])):
		print("found result")
	else:
		print("no result!")

def isSafe(boa, clm):
	for i in range(len(boa)):
		if((boa[i]==clm)| (abs(clm-boa[i])==(len(boa)-i))):
			return False
	return True

def BFS(N, boa):
	if(len(boa) == 0):
		for i in range(N):
			q.append([i])
	while (len(q) != 0):
		top = q.pop(0)
		if(len(top) == N):
			chess = [['-' for i in range(N)] for j in range(N)]
			for x in range(N):
				chess[x][top[x]] = 'Q'
			print("\n".join(" ".join(row) for row in zip(*chess)))
			return True
		for i in range(N):
			if(isSafe(top, i)):
				temp = [top[i] for i in range(len(top))]
				temp.append(i)
				q.append(temp)
	return False

main()