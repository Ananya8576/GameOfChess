import sys
 
### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.
 
# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self,pos,rows,cols,color):
        self.pos=pos
        self.cols=cols
        self.rows=rows
        self.color=color
    
    #get the col (num)
    def get_c(self):
        return self.pos[1]
    
    #get the row (num)
    def get_r(self):
        return self.pos[0]
 
#finding kill-moves and moves particluar to each piece  
#28th Oct: wrong movement for pawn 
#29th Oct debug: separate enemy and free space movements, combining doesn't work for PAWN
 
class Rook(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
 
    def moves(self,state): #regular movement to empty space
        rook_moves=[]
        r,c=self.pos
        for i in range(r-1,-1,-1):
            if c<self.cols and c>=0:
                if (i,c) in state.own_piece or (i,c) in state.enemy_piece:
                    break
                rook_moves.append((i,c))
        for j in range(r+1,self.rows):
            if c<self.cols and c>=0:
                if (j,c) in state.own_piece or (j,c) in state.enemy_piece:
                    break
                rook_moves.append((j,c))
        for k in range(c+1,self.cols):
            if r<self.rows and r>=0:
                if (r,k) in state.own_piece or (r,k) in state.enemy_piece:
                    break
                rook_moves.append((r,k))
        for l in range(c-1,-1,-1):
            if r<self.rows and r>=0:
                if (r,l) in state.own_piece or (r,l) in state.enemy_piece:
                    break
                rook_moves.append((r,l))
        return rook_moves
 
    def kill_moves(self,state): #move only when enemy piece encountered
        rook_kill_moves=[]
        r,c=self.pos
        if self.color=='White':
            for i in range(r-1,-1,-1):
                if c<self.cols and c>=0:
                    if (i,c) in state.enemy_piece:
                        rook_kill_moves.append((i,c))
                        break
                    elif (i,c) in state.own_piece:
                        break
            for j in range(r+1,self.rows):
                if c<self.cols and c>=0:
                    if (j,c) in state.enemy_piece:
                        rook_kill_moves.append((j,c))
                        break
                    elif (j,c) in state.own_piece:
                        break
            for k in range(c+1,self.cols):
                if r<self.rows and r>=0:
                    if (r,k) in state.enemy_piece:
                        rook_kill_moves.append((r,k))
                        break
                    elif (r,k) in state.own_piece:
                        break
            for l in range(c-1,-1,-1):
                if r<self.rows and r>=0:
                    if (r,l) in state.enemy_piece:
                        rook_kill_moves.append((r,l))
                        break
                    elif (r,l) in state.own_piece:
                        break
        if self.color=='Black':
            for i in range(r-1,-1,-1):
                if c<self.cols and c>=0:
                    if (i,c) in state.enemy_piece:
                        break
                    elif (i,c) in state.own_piece:
                        rook_kill_moves.append((i,c))
                        break
            for j in range(r+1,self.rows):
                if c<self.cols and c>=0:
                    if (j,c) in state.enemy_piece:
                        break
                    elif (j,c) in state.own_piece:
                        rook_kill_moves.append((j,c))
                        break
            for k in range(c+1,self.cols):
                if r<self.rows and r>=0:
                    if (r,k) in state.enemy_piece:
                        break
                    elif (r,k) in state.own_piece:
                        rook_kill_moves.append((r,k))
                        break
            for l in range(c-1,-1,-1):
                if r<self.rows and r>=0:
                    if (r,l) in state.enemy_piece:
                        break
                    elif (r,l) in state.own_piece:
                        rook_kill_moves.append((r,l))
                        break
        return rook_kill_moves
 
    def get_name(self):
        return "Rook"       
 
class Bishop(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
  
    def moves(self,state):
        r,c=self.pos
        bishop_moves=[]
        diag1 = zip(range(r+1,self.rows), range(c-1,-1,-1))
        diag2 = zip(range(r+1,self.rows), range(c+1,self.cols)) 
        diag3 = zip(range(r-1,-1,-1), range(c-1,-1,-1))
        diag4 = zip(range(r-1,-1,-1), range(c+1,self.cols))
        for r1,c1 in diag1:
            if r1<self.rows and r1>=0 and c1<self.cols and c1>=0:
                if (r1,c1) in state.own_piece or (r1,c1) in state.enemy_piece:
                    break
                bishop_moves.append((r1,c1))
        for r2,c2 in diag2:
            if r2<self.rows and r2>=0 and c2<self.cols and c2>=0:
                if (r2,c2) in state.own_piece or (r2,c2) in state.enemy_piece:
                    break
                bishop_moves.append((r2,c2))
        for r3,c3 in diag3:
            if r3<self.rows and r3>=0 and c3<self.cols and c3>=0:
                if (r3,c3) in state.own_piece or (r3,c3) in state.enemy_piece:
                    break
                bishop_moves.append((r3,c3))
        for r4,c4 in diag4:
            if r4<self.rows and r4>=0 and c4<self.cols and c4>=0:
                if (r4,c4) in state.own_piece or (r4,c4) in state.enemy_piece:
                    break
                bishop_moves.append((r4,c4))
        return bishop_moves
 
    def kill_moves(self,state):
        r,c=self.pos
        bishop_kill_moves=[]
        diag1 = zip(range(r+1,self.rows), range(c-1,-1,-1))
        diag2 = zip(range(r+1,self.rows), range(c+1,self.cols)) 
        diag3 = zip(range(r-1,-1,-1), range(c-1,-1,-1))
        diag4 = zip(range(r-1,-1,-1), range(c+1,self.cols))
        if self.color=='White':
            for r1,c1 in diag1:
                if r1<self.rows and r1>=0 and c1<self.cols and c1>=0:
                    if (r1,c1) in state.enemy_piece:
                        bishop_kill_moves.append((r1,c1))
                        break
                    elif (r1,c1) in state.own_piece:
                        break
            for r2,c2 in diag2:
                if r2<self.rows and r2>=0 and c2<self.cols and c2>=0:
                    if (r2,c2) in state.enemy_piece:
                        bishop_kill_moves.append((r2,c2))
                        break
                    elif (r2,c2) in state.own_piece:
                        break
            for r3,c3 in diag3:
                if r3<self.rows and r3>=0 and c3<self.cols and c3>=0:
                    if (r3,c3) in state.enemy_piece:
                        bishop_kill_moves.append((r3,c3))
                        break
                    elif (r3,c3) in state.own_piece:
                        break
            for r4,c4 in diag4:
                if r4<self.rows and r4>=0 and c4<self.cols and c4>=0: 
                    if (r4,c4) in state.enemy_piece:
                        bishop_kill_moves.append((r4,c4))
                        break
                    elif (r4,c4) in state.own_piece:
                        break
        if self.color=='Black':
            for r1,c1 in diag1:
                if r1<self.rows and r1>=0 and c1<self.cols and c1>=0:
                    if (r1,c1) in state.own_piece:
                        bishop_kill_moves.append((r1,c1))
                        break
                    elif (r1,c1) in state.enemy_piece:
                        break
            for r2,c2 in diag2:
                if r2<self.rows and r2>=0 and c2<self.cols and c2>=0:
                    if (r2,c2) in state.own_piece:
                        bishop_kill_moves.append((r2,c2))
                        break
                    elif (r2,c2) in state.enemy_piece:
                        break
            for r3,c3 in diag3:
                if r3<self.rows and r3>=0 and c3<self.cols and c3>=0:
                    if (r3,c3) in state.own_piece:
                        bishop_kill_moves.append((r3,c3))
                        break
                    elif (r3,c3) in state.enemy_piece:
                        break
            for r4,c4 in diag4:
                if r4<self.rows and r4>=0 and c4<self.cols and c4>=0:
                    if (r4,c4) in state.own_piece:
                        bishop_kill_moves.append((r4,c4))
                        break
                    elif (r4,c4) in state.enemy_piece:
                        break
        return bishop_kill_moves
 
    def get_name(self):
        return "Bishop"
 
class Queen(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
 
    def moves(self,state):
        queen_moves=[]
        piece1=Rook(self.pos,self.rows, self.cols,self.color)
        piece2=Bishop(self.pos, self.rows, self.cols,self.color)
        queen_moves.extend(piece1.moves(state))
        queen_moves.extend(piece2.moves(state))
        return queen_moves
 
    def kill_moves(self,state):
        queen_kill_moves=[]
        piece1=Rook(self.pos,self.rows, self.cols,self.color)
        piece2=Bishop(self.pos, self.rows, self.cols,self.color)
        queen_kill_moves.extend(piece1.kill_moves(state))
        queen_kill_moves.extend(piece2.kill_moves(state))
        return queen_kill_moves
 
    def get_name(self):
        return "Queen"
    
class Knight(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
 
    def moves(self,state): #fixed 8 moves around piece
        op1=[-2,1,-1,2,2,1,-1,-2] #for row movement
        op2=[1,2,2,1,-1,-2,-2,-1] #for col movement
        knight_moves=[]
        r,c=self.pos
        for index in range(0,8):
            if r+op1[index]< self.rows and r+op1[index]>=0 and c+op2[index]<self.cols and c+op2[index]>=0:
                if (r+op1[index],c+op2[index]) not in state.own_piece and (r+op1[index],c+op2[index]) not in state.enemy_piece and (r+op1[index],c+op2[index]) in state.empty:
                    knight_moves.append((r+op1[index],c+op2[index]))
        return knight_moves
 
    def kill_moves(self,state): #fixed 8 moves around piece
        op1=[-2,1,-1,2,2,1,-1,-2] #for row movement
        op2=[1,2,2,1,-1,-2,-2,-1] #for col movement
        knight_kill_moves=[]
        r,c=self.pos
        if self.color=='White':
            for index in range(0,8):
                if r+(op1[index])< self.rows and r+(op1[index])>=0 and c+(op2[index])<self.cols and c+(op2[index])>=0:
                    if (r+op1[index],c+op2[index]) in state.enemy_piece:
                        knight_kill_moves.append((r+op1[index],c+op2[index]))
        if self.color=='Black':
            for index in range(0,8):
                if r+op1[index]< self.rows and r+op1[index]>=0 and c+op2[index]<self.cols and c+op2[index]>=0:
                    if (r+op1[index],c+op2[index]) in state.own_piece:
                        knight_kill_moves.append((r+op1[index],c+op2[index]))
        return knight_kill_moves
 
    def get_name(self):
        return "Knight"
 
class King(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
 
    def moves(self,state):
        king_moves=[]
        r,c=self.pos
        for i in range(-1,2):
            for j in range(-1,2):
                if r+i<self.rows and c+j<self.cols and r+i>=0 and c+j>=0:
                    if (r+i,c+j)!=(r,c) and (r+i,c+j) not in state.enemy_piece and (r+i,c+j) not in state.own_piece and (r+i,c+j) in state.empty:
                        king_moves.append((r+i,c+j))
        return king_moves
 
    def kill_moves(self,state):
        king_kill_moves=[]
        r,c=self.pos
        if self.color=='White':
            for i in range(-1,2):
                for j in range(-1,2):
                    if r+i<self.rows and c+j<self.cols and r+i>=0 and c+j>=0:
                        if (r+i,c+j)!=(r,c) and (r+i,c+j) in state.enemy_piece:
                            king_kill_moves.append((r+i,c+j))
        if self.color=='Black':
            for i in range(-1,2):
                for j in range(-1,2):
                    if r+i<self.rows and c+j<self.cols and r+i>=0 and c+j>=0:
                        if (r+i,c+j)!=(r,c) and (r+i,c+j) in state.own_piece:
                            king_kill_moves.append((r+i,c+j))
        return king_kill_moves
 
    def get_name(self):
        return "King"
 
class Ferz(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
 
    def moves(self,state):
        ops=[-1,1]
        ferz_moves=[]
        r,c=self.pos
        for i in ops:
            for j in ops:
                if r+i<self.rows and r+i>=0 and c+j<self.cols and c+j>=0:
                    if (r+i,c+j) not in state.enemy_piece and (r+i,c+j) not in state.own_piece and (r+i,c+j) in state.empty:
                        ferz_moves.append((r+i,c+j))
        return ferz_moves
 
    def kill_moves(self,state):
        ops=[-1,1]
        ferz_kill_moves=[]
        r,c=self.pos
        if self.color=='White':
            for i in ops:
                for j in ops:
                    if r+i<self.rows and r+i>=0 and c+j<self.cols and c+j>=0 and (r+i,c+j) in state.enemy_piece:
                        ferz_kill_moves.append((r+i,c+j))
        else:
            for i in ops:
                for j in ops:
                    if r+i<self.rows and r+i>=0 and c+j<self.cols and c+j>=0 and (r+i,c+j) in state.own_piece:
                        ferz_kill_moves.append((r+i,c+j))
        return ferz_kill_moves
 
    def get_name(self):
        return "Ferz"
 
class Princess(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
 
    def moves(self,state):
        princess_moves=[]
        piece1=Bishop(self.pos,self.rows, self.cols,self.color)
        piece2=Knight(self.pos, self.rows, self.cols,self.color)
        princess_moves.extend(piece1.moves(state))
        princess_moves.extend(piece2.moves(state))
        return princess_moves
    
    def kill_moves(self,state):
        princess_kill_moves=[]
        piece1=Bishop(self.pos,self.rows, self.cols,self.color)
        piece2=Knight(self.pos, self.rows, self.cols,self.color)
        princess_kill_moves.extend(piece1.kill_moves(state))
        princess_kill_moves.extend(piece2.kill_moves(state))
        return princess_kill_moves
 
    def get_name(self):
        return "Princess"
    
class Empress(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
 
    def moves(self,state):
        empress_moves=[]
        piece1=Rook(self.pos,self.rows, self.cols,self.color)
        piece2=Knight(self.pos, self.rows, self.cols,self.color)
        empress_moves.extend(piece1.moves(state))
        empress_moves.extend(piece2.moves(state))
        return empress_moves
 
    def kill_moves(self,state):
        empress_kill_moves=[]
        piece1=Rook(self.pos,self.rows, self.cols,self.color)
        piece2=Knight(self.pos, self.rows, self.cols,self.color)
        empress_kill_moves.extend(piece1.kill_moves(state))
        empress_kill_moves.extend(piece2.kill_moves(state))
        return empress_kill_moves
 
    def get_name(self):
        return "Empress"
 
class Pawn(Piece):
    def __init__(self,pos,rows,cols,color):
        super().__init__(pos,rows,cols,color)
 
    def moves(self,state):
        pawn_moves=[]
        r,c=self.pos
        if r+1<self.rows and r+1>=0 and c>=0 and c<self.cols:
            if self.color=='White':
                if (r+1,c) not in state.own_piece and (r+1,c) not in state.enemy_piece and (r+1,c) in state.empty:
                    pawn_moves.append((r+1,c))
            else:
                if (r-1,c) not in state.own_piece and (r-1,c) not in state.enemy_piece and (r-1,c) in state.empty:
                    pawn_moves.append((r-1,c))
        return pawn_moves
 
    def kill_moves(self,state):
        pawn_kill_moves=[]
        r,c=self.pos
        ops=[1,-1]
        if self.color=='White':
            for i in ops:
                if r+1<self.rows and r+1>=0 and c+i>=0 and c+i<self.cols:
                    if (r+1,c+i) in state.enemy_piece: #and enemy present based on color
                        pawn_kill_moves.append((r+1,c+i))
        if self.color=='Black':
            for i in ops:
                if r-1<self.rows and r-1>=0 and c+i>=0 and c+i<self.cols:
                    if (r-1,c+i) in state.own_piece: #and enemy present based on color
                        pawn_kill_moves.append((r-1,c+i))
        return pawn_kill_moves
 
    def get_name(self):
        return "Pawn"
 
############################################################################
######## Board
#############################################################################
class Board:
    def __init__(self,r,c):
        self.r=r
        self.c=c
 
#############################################################################
######## State
#############################################################################
 
#h values example: https://www.chess.com/blog/HasanElias/exact-relative-value-of-chess-pieces-and-fairy-chess-pieces
#optimising algo for minmax:https://www.youtube.com/watch?v=-ivz8yJ4l4E
#improving h:https://chess.stackexchange.com/questions/14434/how-to-determine-the-value-of-a-piece-from-scratch
#https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

heuristics={'Pawn':10,'Ferz':20,'Knight':30,'Bishop':40,'Rook':50,'Princess':60,'Empress':80,'Queen':90,'King':900}
 
class State:
    def __init__(self,rows,cols,gameboard):
        self.rows=rows
        self.cols=cols
        self.gameboard=gameboard
        self.white_pieces=[] #listing of white pieces that are on the board
        self.black_pieces=[] #listing of black that are on the board
        self.own_piece=[] #positions of own pieces
        self.enemy_piece=[] #positions of enemy pieces
        self.empty=[]
        
        #need list of all pieces for debugging in example board on google collab 
        occupied=list(gameboard.keys()) #non-empty spaces on board
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in occupied:
                    self.empty.append((r,c)) #empty blocks for movement
 
        for pos,tup in list(gameboard.items()):
            name_piece=tup[0]
            color_piece=tup[1]
            if color_piece=='Black': #all enemy pieces on board (BLACK)
                if name_piece=='King':
                    self.black_pieces.append(King(pos,rows,cols,'Black'))
                elif name_piece=='Queen':
                    self.black_pieces.append(Queen(pos,rows,cols,'Black'))
                elif name_piece=='Empress':
                    self.black_pieces.append(Empress(pos,rows,cols,'Black'))
                elif name_piece=='Princess':
                    self.black_pieces.append(Princess(pos,rows,cols,'Black'))
                elif name_piece=='Rook':
                    self.black_pieces.append(Rook(pos,rows,cols,'Black'))
                elif name_piece=='Bishop':
                    self.black_pieces.append(Bishop(pos,rows,cols,'Black'))
                elif name_piece=='Knight':
                    self.black_pieces.append(Knight(pos,rows,cols,'Black'))
                elif name_piece=='Ferz':
                    self.black_pieces.append(Ferz(pos,rows,cols,'Black'))
                else:
                    self.black_pieces.append(Pawn(pos,rows,cols,'Black'))
            else: #all own pieces on board (WHITE)
                if name_piece=='King':
                    self.white_pieces.append(King(pos,rows,cols,'White'))
                elif name_piece=='Queen':
                    self.white_pieces.append(Queen(pos,rows,cols,'White'))
                elif name_piece=='Empress':
                    self.white_pieces.append(Empress(pos,rows,cols,'White'))
                elif name_piece=='Princess':
                    self.white_pieces.append(Princess(pos,rows,cols,'White'))
                elif name_piece=='Rook':
                    self.white_pieces.append(Rook(pos,rows,cols,'White'))
                elif name_piece=='Bishop':
                    self.white_pieces.append(Bishop(pos,rows,cols,'White'))
                elif name_piece=='Knight':
                    self.white_pieces.append(Knight(pos,rows,cols,'White'))
                elif name_piece=='Ferz':
                    self.white_pieces.append(Ferz(pos,rows,cols,'White'))
                else:
                    self.white_pieces.append(Pawn(pos,rows,cols,'White'))
 
    def assign_pieces(self):
        for p in self.black_pieces: #assign entire piece to dictionary so easy to call positions
            self.gameboard[p.pos]=p
            self.enemy_piece.append(p.pos)
        for p2 in self.white_pieces:
            self.gameboard[p2.pos]=p2
            self.own_piece.append(p2.pos)
 
    def heuristic(self,name,color):
        if color=='White':
            return heuristics[name] #own 
        else:
            return heuristics[name]*(-1) #enemy 
        
    def utility(self):
        utility_white=0
        utility_black=0
        for key,piece in self.gameboard.items():
            val1=piece.get_name()
            val2=piece.color
            if key in self.own_piece and val2=='White':
                utility_white+=self.heuristic(val1,val2)
            elif key in self.enemy_piece and val2=='Black':
                utility_black+=self.heuristic(val1,val2)
        return utility_white+utility_black
 
    def next_board(self):
        next={}
        for key in self.gameboard.keys():
            p=self.gameboard[key]
            next[key]=(p.get_name(),p.color)
        return next
 
    def try_action(self,from_pos,to_pos,self_turn): #trying an action for each piece on dummy board
        initial_piece=self.gameboard[from_pos] #initial piece
        initial_piece.pos=to_pos #final position
 
        if self_turn==True:
            self.own_piece.remove(from_pos)
            self.own_piece.append(to_pos)
            if to_pos in self.enemy_piece: #killed piece
                self.enemy_piece.remove(to_pos)
                self.black_pieces.remove(self.gameboard[to_pos])
        else:
            self.enemy_piece.remove(from_pos)
            self.enemy_piece.append(to_pos)
            if to_pos in self.own_piece:
                self.own_piece.remove(to_pos)
                self.white_pieces.remove(self.gameboard[to_pos])
        
        self.gameboard.pop(from_pos)
        self.gameboard[to_pos] = initial_piece
        self.empty.append(from_pos)
 
def all_actions(state,piece): #all possible actions at each piece
    movement=piece.kill_moves(state)
    movement.extend(piece.moves(state))
    return set(movement)
 
def check(state,self_turn): #only need to check for white king under check/checkmate
    for (i,j) in state.gameboard.keys():
        p1=state.gameboard[(i,j)]
        if p1.get_name() == "King":
            for (i2,j2) in state.gameboard.keys():
                p2 = state.gameboard[(i2,j2)]
                if p2.color != p1.color:
                    lst = all_actions(state,p2)
                    if p1.pos in lst: #condition 1:under check
                        if p1.color == "White" and self_turn==True:
                            return True
        return False
 
def terminal(state): #if one king killed then game stops
    count=0
    for p in state.gameboard.values():
        if p != None and p.get_name()=='King': #condition 2: king capture
            count+=1
    if count!=2:
        return True 
    return False
 
negative_inf=-float('inf')
positive_inf=float('inf')
 
#Implement your minimax with alpha-beta pruning algorithm here.
def ab(gameboard,state):
    state.gameboard=gameboard
    self_turn=True
    depth=2 #returning based on black moves so need to use depth<5
    alpha=negative_inf
    beta=positive_inf
 
    _,position = minimax(state,self_turn, depth, alpha, beta)
    return position
 
def minimax(state,self_turn, depth, alpha, beta):
    if depth == 0 or terminal(state): #condition 2: king capture
        return state.utility(),None
 
    if check(state,self_turn)==True: #not needed,stop based on alpha beta
        return positive_inf, None 
 
    selected=None
    if self_turn==True: #max player
        value = negative_inf
        for node in state.white_pieces:
            possible_moves=all_actions(state,node)
            for action in possible_moves:
                from_pos=node.pos
                to_pos=action
                
                dummy_board=state.next_board() #copy of board
                dummy_state=State(7,7,dummy_board)
                dummy_state.assign_pieces()
                dummy_state.try_action(from_pos,to_pos,self_turn)
 
                val,_=minimax(dummy_state,False,depth-1, alpha, beta)
 
                if val>value:
                    value,selected=val,(from_pos,to_pos)
                    alpha=max(alpha,value)
                if value>=beta:
                    break
                if alpha>=beta:
                    break
            if alpha>=beta:
                break
        return value, selected
    
    else: #min player
        value=positive_inf
        for node in state.black_pieces:
            possible_moves=all_actions(state,node)
            for action in possible_moves:
                from_pos=node.pos
                to_pos=action
                
                dummy_board=state.next_board() #copy of board
                dummy_state=State(7,7,dummy_board)
                dummy_state.assign_pieces()
                dummy_state.try_action(from_pos,to_pos,self_turn)
                
                val,_=minimax(dummy_state,True,depth-1, alpha, beta)
                
                if val<value:
                    value,selected=val,(from_pos,to_pos)
                    beta=min(beta,value)
                if value<=alpha:
                    break
                if beta<=alpha:
                    break
            if beta<=alpha:
                break
        return value, selected
  
 
def convert_to_char(pos):
    return (chr(pos[1] + 97), int(pos[0]))
 
def convert_to_num(pos):
    return (int(pos[1]),ord(pos[0])-97)

 
#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")
 
    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline())) # Integer
    cols = int(get_par(handle.readline())) # Integer
    gameboard = {}
    
    enemy_piece_nums = get_par(handle.readline()).split()
    num_enemy_pieces = 0 # Read Enemy Pieces Positions
    for num in enemy_piece_nums:
        num_enemy_pieces += int(num)
 
    handle.readline()  # Ignore header
    for i in range(num_enemy_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "Black")    
 
    own_piece_nums = get_par(handle.readline()).split()
    num_own_pieces = 0 # Read Own Pieces Positions
    for num in own_piece_nums:
        num_own_pieces += int(num)
 
    handle.readline()  # Ignore header
    for i in range(num_own_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "White")    
 
    return rows, cols, gameboard
 
def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]
 
def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)
 
# You may call this function if you need to set up the board
def setUpBoard():
    config = sys.argv[1]
    rows, cols, gameboard = parse(config)
    #return gameboard
 
### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook, Princess, Empress, Ferz, Pawn (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)
 
# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new ending position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))
 
def studentAgent(gameboard):
    #gameboard uses (char,num) form on codepost, local case not there so test accordingly
    new={}
    for key,tup in list(gameboard.items()): #codepost
        new[convert_to_num(key)]=tup
    state=State(7,7,new)
    state.assign_pieces()
    move = ab(new,state)
 
    #state=State(7,7,gameboard) #local
    #state.assign_pieces() #local
    #move=ab(gameboard,state) #local
 
    final=(convert_to_char(move[0]),convert_to_char(move[1]))
    return final #Format to be returned (('a', 0), ('b', 3))
 
#gameboard=setUpBoard()
#print(studentAgent(gameboard))