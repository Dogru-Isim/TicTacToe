import random
import sys

print('\n'*100)
print('Welcome to TicTacToe! \n If you stuck, you can type "guide" or "g" anytime you want \n')
try:
	player1 = input('Player1: Pick one: "X" or "O"): ')
	player2 = ""
except:
	print('\nProgram has ended')
	sys.exit()

def player_input():
    global player1
    global player2
    
    while True:
        if player1.upper() == 'X':
            player2 = 'O'
            print('\n' * 100)
            print(f"""
Player1 is {player1}
Player2 is {player2}
            """)
            break
            
        elif player1.upper() == 'O':
            player2 = 'X'
            print('\n' * 100)
            print(f"""
Player1 is {player1}
Player2 is {player2}
            """)
            break
            
        elif player1.lower() == 'g' or player1.lower() == 'guide':
            print("\n SIKE You really thought you could get the game that easily didn't you? This game wasn't easy for me so why to you? \n")
            player1 = input('Player1: What do you wanna be?("X" or "O"): ')
            
        else:
            print('\n' * 100)
            player1 = input('\n Please type "X" or "O": ')


def display_board(board):
    hashtag, num1, num2, num3, num4, num5, num6, num7, num8, num9 = board
    print('\n'*100)
    print(f"""
                                                                                             |          |
                                                                                       {num1}     |    {num2}     |     {num3}
                                                                                             |          |          
                                                                                   ----------|----------|----------
                                                                                             |          |          
                                                                                       {num4}     |    {num5}     |     {num6}
                                                                                             |          |          
                                                                                   ----------|----------|----------          
                                                                                             |          |          
                                                                                       {num7}     |    {num8}     |     {num9}
                                                                                             |          |
                  """)
    print('\n'*18)

def place_marker(board, marker, position):
    board[int(position)] = marker

def win_check(board, mark):
    win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    condition = []
    c = 0
    
    condition_checker = 0
    for i in board:
        c += 1
        if i == mark:
            condition.append(c-1)
            for list in win_conditions:
                for num in list:
                    if num in condition:
                        condition_checker += 1
                    else:
                        condition_checker = 0
                        break
                if condition_checker == 3:
                    return True

def choose_first():
    stick = random.randint(1,2)
    if stick == 1:
        print('X is first')
        
    if stick == 2:
        print('O is first')

    return stick

def space_check(board, position):
    if board[int(position)] == 'X' or board[int(position)] == 'O':
        return False
    else:
        return True

def full_board_check(board):
    if board.count(' ') == 0:
        return True
    else:
        return False
        
def player_choice(board):
    while True:
        try:
            position = input('\nEnter your your area number: ')
            if position == 'g' or position == 'guide':
                print('\n SIKE no guide for you \n')
            
            elif int(position) in range(1,10):
                if space_check(board, position):
                    return int(position)
                    
        except ValueError:
            continue

def replay():
    response = input('\nDo you want to play again?(Yes or No): ')
    while True:
        try:
            if response.lower() == 'yes':
                return True
                
            elif response.lower() == 'no':
                return False
                
            else:
                response = input("\nPlease type in 'yes' or 'no': ")
        except ValueError:
            response = input("\nPlease type in 'yes' or 'no': ")

def main():
	board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	player_input()
	first = choose_first()

	while True:
		try:
			display_board(board)

			if first == 1:
				print('X goes,')

				place_marker(board, 'X', player_choice(board))
				display_board(board)

				if win_check(board, 'X'):
					print('\nCongrats X, you win!!\n')
					break
		        
				if full_board_check(board):
					print('\nTie\n')
					break
		        
				print('O goes,')
		        
				place_marker(board, 'O', player_choice(board))
				display_board(board)
		        
				if win_check(board, 'O'):
					print('\nCongrats O, you win!!\n')
					break

			else:        
				print('O goes,')
		        
				place_marker(board, 'O', player_choice(board))
				display_board(board)

				if win_check(board, 'O'):
					print('\nCongrats O, you win!!\n')
					break
		            
				if full_board_check(board):
					print('\nTie\n')
					break
		        
				print('X goes,')
		        
				place_marker(board, 'X', player_choice(board))
				display_board(board)

				if win_check(board, 'X'):
					print('\nCongrats X, you win!!\n')
					break
		            
		except KeyboardInterrupt:
			print('\nGame ended.\n')
			break
			
if __name__ == '__main__':
	try:
		main()
		while True:
			try:
				if replay():
					main()
				else:
					print('\n'*100 + 'ok\n')
					break
			except KeyboardInterrupt:
				print('\n \nUser has ended the program\n')
				break
	except KeyboardInterrupt:
		print('\nProgram has ended')
