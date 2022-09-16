import pygame

pygame.init()

#関数----------------------------------------------------------------------

#グリッドの描画
def draw_grid():
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (0,i*200), (600,i*200), width=5)
        pygame.draw.line(screen, BLACK, (i*200,0), (i*200,600), width=5)

#ボードの描画
def draw_board():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                pygame.draw.circle(screen, RED, (100+i*200,100+j*200), 90, width=5)

    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:
                pygame.draw.line(screen, BLUE, (i*200+20,j*200+20), (i*200+180,j*200+180), width=5)
                pygame.draw.line(screen, BLUE, (i*200+180,j*200+20), (i*200+20,j*200+180), width=5)
#勝利の確認
def check_winner():
    winner = ''
    gameover = False
    draw = 1
    for i in range(3):
        for j in range(3):
            #縦
            if board[i][0]+board[i][1]+board[i][2] == 3:
                winner = 'Maru Win!'
            if board[i][0]+board[i][1]+board[i][2] == -3:
                winner = 'Batu Win!'
            #横
            if board[0][j]+board[1][j]+board[2][j] == 3:
                winner = 'Maru Win!'
            if board[0][j]+board[1][j]+board[2][j] == -3:
                winner = 'Batu Win!'
            #斜め
            if board[0][0]+board[1][1]+board[2][2] == 3:
                winner = 'Maru Win!'
            if board[0][2]+board[1][1]+board[2][0] == 3:
                winner = 'Maru Win!'
            if board[0][0]+board[1][1]+board[2][2] == -3:
                winner = 'Batu Win!'
            if board[0][2]+board[1][1]+board[2][0] == -3:
                winner = 'Batu Win!'
            #空白があったら0になる
            draw *= board[i][j]
            
    #ドローの判定       
    if winner == '' and draw != 0:
        winner = '  DRAW!  '
            
    #勝者の描画
    if winner != '':
        if winner == 'Batu Win!':
            win_text = font.render(winner, True, BLUE, None)
            reset_text_img = font.render('Click to reset', True, BLUE, None)
        elif winner == 'Maru Win!':
            win_text = font.render(winner, True, RED, None)
            reset_text_img = font.render('Click to reset', True, RED, None)
        else:
            win_text = font.render(winner, True, GREEN, None)
            reset_text_img = font.render('Click to reset', True, GREEN, None)
        screen.blit(win_text, (140,200))
        screen.blit(reset_text_img, (90,300))
        gameover = True
        
    return gameover
#--------------------------------------------------------------------------

#ウィンドウの作成
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('○✕ゲーム')

#色
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,220,0)
BLUE = (0,0,255)

#フォントの設定
font = pygame.font.SysFont(None, 100,italic=True)

#ボード(0:空白 1:〇 -1:✕)
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

number = 1

#メインループ
run = True
while run:

    #背景
    screen.fill(WHITE)
    
    #マウスの位置取得
    mx,my = pygame.mouse.get_pos()
    x = mx//200
    y = my//200
    
    #グリッドの描画
    draw_grid()

    #ボードの描画
    draw_board()

    #勝利の確認
    game_over = check_winner()
          
    #イベントの取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board[x][y] == 0 and game_over == False:
                board[x][y] = number
                number *= -1
            if game_over:
                board = [[0,0,0],
                         [0,0,0],
                         [0,0,0]]
                number = 1
    #更新    
    pygame.display.update()
            
pygame.quit()
