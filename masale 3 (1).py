def px(n):
    size = 2 * n + 1
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    x, y = n, n
    grid[x][y] = '*'
    step = 1  
    direction = 0
    for i in range(1, n + 1):
        for _ in range(2):  
            for _ in range(step):
                if direction == 0: 
                    y += 1
                elif direction == 1:  
                    x -= 1
                elif direction == 2:  
                    y -= 1
                elif direction == 3:  
                    x += 1

                grid[x][y] = '*'
            direction = (direction + 1) % 4  
        step += 1  
    for row in grid:
        print(' '.join('*' if cell == '*' else '-' for cell in row))
n = int(input("Enter n: "))
px(n)