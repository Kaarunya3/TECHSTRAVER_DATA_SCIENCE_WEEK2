import pygame

# Grid size and colors
WIDTH, HEIGHT = 540, 540
CELL_SIZE = WIDTH // 9
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLUE = (0, 0, 255)  # Highlighting color

pygame.init()  # Initialize pygame before using font modules
FONT = pygame.font.SysFont("Arial", 40)

# Board (replace with your API data if applicable)
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 5, 0, 0, 6, 3, 0, 8, 7],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [8, 0, 0, 7, 0, 0, 0, 0, 4],
    [2, 9, 0, 8, 0, 0, 7, 1, 0],
    [0, 7, 4, 0, 0, 0, 0, 5, 8],
]


def draw_grid(win):
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(win, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(win, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)


def display_board(win, board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            value = board[row][col]
            if value != 0:
                text = FONT.render(str(value), True, BLACK)
                win.blit(text, (col * CELL_SIZE + (CELL_SIZE - text.get_width()) // 2, row * CELL_SIZE + (CELL_SIZE - text.get_height()) // 2))


def is_valid(board, row, col, num):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0

    return False


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None


def highlight_cell(win, pos):
    row, col = pos
    pygame.draw.rect(win, BLUE, (col * CELL_SIZE + 5, row * CELL_SIZE + 5, CELL_SIZE - 10, CELL_SIZE - 10))


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver")
    run = True
    selected = None
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected = (pos[0] // CELL_SIZE, pos[1] // CELL_SIZE)
            if event.type == pygame.KEYDOWN:
                if selected and event.key != pygame.K_BACKSPACE:
                    if 0 <= event.key - 48 <= 9:  # Check for number keys (0-9)
                        board[selected[0]][selected[1]] = event.key - 48
                else:
                    if event.key == pygame.K_SPACE:
                        solve(board)

        win.fill(WHITE)
        draw_grid(win)
        display_board(win, board)
        if selected:
            highlight_cell(win, selected)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

