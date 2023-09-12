pieces = [1,1,2,2,2,8]
total_piece = 16
piece_has = list(map(int, input().split())) 
piece_less = total_piece - sum(piece_has)

for piece, has in zip(pieces, piece_has):
    print(piece - has, end = " ")