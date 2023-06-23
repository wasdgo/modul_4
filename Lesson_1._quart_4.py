word = input()
pieceword = len(word) // 2
print(word[:pieceword] == word[:len(word)-pieceword-1:-1])