import pygame 
# Define colors 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
# Initialize
pygame.init()
# Set the size of the screen 
size = (800, 800) 
screen = pygame.display.set_mode(size, pygame.SRCALPHA)
# Create the chessboard 
board = [[0]*8 for i in range(8)] 
# Set up the pieces 
board[0][0] = 4 
board[0][1] = 2 
board[0][2] = 3 
board[0][3] = 5 
board[0][4] = 6 
board[0][5] = 3 
board[0][6] = 2 
board[0][7] = 4 
board[1][0] = 1 
board[1][1] = 1 
board[1][2] = 1 
board[1][3] = 1 
board[1][4] = 1 
board[1][5] = 1 
board[1][6] = 1 
board[1][7] = 1 
board[6][0] = -1 
board[6][1] = -1 
board[6][2] = -1 
board[6][3] = -1 
board[6][4] = -1 
board[6][5] = -1 
board[6][6] = -1 
board[6][7] = -1 
board[7][0] = -4 
board[7][1] = -2 
board[7][2] = -3 
board[7][3] = -5 
board[7][4] = -6 
board[7][5] = -3 
board[7][6] = -2 
board[7][7] = -4 
# Set up the font 
font = pygame.font.SysFont('Arial', 30) 
# Main loop 
while True: 
    # Handle events 
    pygame.draw.rect(screen, (205, 134, 6), ((0,0), size), width=0)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos() 
            row = pos[1] // 100 
            col = pos[0] // 100
    for x in range(8):
        for y in range(8):
            if board[y][x] < 0:
                pieceColor = (255,255,255)
            elif board[y][x] > 0:
                pieceColor = (0,0,0)
            else:
                pieceColor = (205, 134, 6)
            piece = font.render(str(board[y][x]), True, pieceColor)
            screen.blit(piece, (x*100+25, y*100+25))
    pygame.display.update()
