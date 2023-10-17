import pygame
import random as rd


class MazeNode:
    
    def __init__(self, i, j, next_node=None):
        
        self.status = 0 # 0 means not part of the maze
        self.i, self.j = i, j
        self.next_node = next_node
        
    def getNext(self):
        return self.next_node
    
    def setNext(self, n):
        self.next_node = n
        
    def getStatus(self):
        return self.status
    
    def connectToMaze(self):
        self.status = 1
        
    def disconnectFromMaze(self):
        self.status = 0


class Maze:
    
    def __init__(self, width=30, height=30, blockSize=30):
        
        self.w = width
        self.h = height
        self.bs = blockSize
        
        self.emptyCells = []
        self.mazeGrid = []
        
        # Maze initialization
        self._populateMazeGrid()
        
        # Starter maze
        i, j = rd.randint(0, self.h-1), rd.randint(0, self.w-1)
        self.mazeGrid[i][j].connectToMaze()
        
        # Maze colors
        self.colors = {'wall': (141, 121, 94), 'road': (229, 216, 200)}

    
    def _populateMazeGrid(self):
        
        for i in range(self.h):
            self.mazeGrid.append([])
            for j in range(self.w):
                self.mazeGrid[i].append(MazeNode(i, j))
                
        
    def _generateEmptyCellsList(self):
        
        self.emptyCells.clear()
        
        for i in range(self.h):
            for j in range(self.w):
                
                if not self.mazeGrid[i][j].getStatus():
                    self.emptyCells.append((i, j))
                
    
    def _singleRandomWalk(self, i, j):
        
        l = []
        if i + 1 < self.h: l.append((i + 1, j))
        if 0 <= i - 1: l.append((i - 1, j))
        if j + 1 < self.w: l.append((i, j + 1))
        if 0 <= j - 1: l.append((i, j - 1))
        
        return rd.choice(l)
    
    
    def _randomEmptyCell(self):
        return rd.choice(self.emptyCells)
    
    
    def generateMaze(self):
           
        while True:
            
            path = []
            self._generateEmptyCellsList()
            
            if len(self.emptyCells) == 0:
                break
            
            i, j = self._randomEmptyCell()
            path.append((i, j))
            
            while True:
                
                ni, nj = self._singleRandomWalk(i, j)
                if (ni, nj) in path:
                    break
                
                elif self.mazeGrid[ni][nj].getStatus() == 1:
                    
                    path.append((ni, nj))
                    
                    path_i = 0
                    while path_i < len(path)-1:
                        i, j = path[path_i]
                        ni, nj = path[path_i+1]
                        self.mazeGrid[i][j].setNext((ni, nj))
                        self.mazeGrid[i][j].connectToMaze()
                        path_i += 1
                    
                    break
                    
                else:
                    path.append((ni, nj))
                    i, j = ni, nj
        
    
    def drawMaze(self):
        
        self.generateMaze()
        
        pygame.init()
        screen = pygame.display.set_mode((self.w * self.bs, self.h * self.bs))
        
        screen.fill((self.colors['wall']))
        
        for i in range(self.h):
            for j in range(self.w):
                
                pygame.draw.rect(screen, self.colors['road'], (i * self.bs + 10, j * self.bs + 10, 10, 10)) # Make dynamic

                
                if self.mazeGrid[i][j].getNext() != None:
                    ni, nj = self.mazeGrid[i][j].getNext()
                    
                    if i < ni:
                        pygame.draw.rect(screen, self.colors['road'], (j * self.bs + 10, i * self.bs + 20, 10, 20))
                    if i > ni:
                        pygame.draw.rect(screen, self.colors['road'], (nj * self.bs + 10, ni * self.bs + 20, 10, 20))        
                    if j < nj:
                        pygame.draw.rect(screen, self.colors['road'], (j * self.bs + 20, i * self.bs + 10, 20, 10))
                    if j > nj:
                        pygame.draw.rect(screen, self.colors['road'], (nj * self.bs + 20, ni * self.bs + 10, 20, 10))
                        
                # pygame.draw.rect(screen, (141, 184, 195), (i * self.bs + 10, j * self.bs + 10, 10, 10)) # Make dynamic
                    
        pygame.display.flip()
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.generateMaze() # Make generate new when SPACE pressed
                        
        # Draw entrance and exit
                    
            
                    

                    
            
                
                

                  
            
maze = Maze()
# maze.generateMaze()       
maze.drawMaze()  
            
            
        
    