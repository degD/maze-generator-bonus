        for i in range(self.h):
            for j in range(self.w):
                
                pygame.draw.rect(screen, self.colors['wall'], (i + 10 * self.bs, j * self.bs, self.bs, self.bs))
                pygame.draw.rect(screen, self.colors['road'], ((i + 10) * self.bs, (j + 10) * self.bs, 10, 10)) # Make dynamic
                
                # FIX DRAW SYSTEM
                if self.mazeGrid[i][j].getNext():
                    
                    ni, nj = self.mazeGrid[i][j].getNext()

                    if j < nj: # go right
                        pygame.draw.rect(screen, self.colors['road'], ((i + 10) * self.bs, (j + 10) * self.bs, 40, 10)) # Make dynamic
                    if j > nj: # go left
                        pygame.draw.rect(screen, self.colors['road'], ((ni + 10) * self.bs, (nj + 10) * self.bs, 40, 10)) # Make dynamic    
                    if i < ni: # go down
                        pygame.draw.rect(screen, self.colors['road'], ((i + 10)* self.bs, (j + 10) * self.bs, 10, 40)) # Make dynamic  
                    if i > ni: # go up
                        pygame.draw.rect(screen, self.colors['road'], ((ni + 10) * self.bs, (nj + 10) * self.bs, 10, 40)) # Make dynamic 