class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        robots = []
        for i in range(n):
            robots.append((positions[i], healths[i], directions[i], i))
        
        # sort by position
        robots.sort()
        
        stack = []  # store indices in robots list
        
        for i in range(n):
            pos, health, dirc, idx = robots[i]
            
            if dirc == 'R':
                stack.append(i)
            else:
                # fight with previous R robots
                while stack and robots[stack[-1]][2] == 'R' and health > 0:
                    top_idx = stack[-1]
                    top_pos, top_health, top_dir, top_original = robots[top_idx]
                    
                    if top_health == health:
                        stack.pop()
                        health = 0
                        break
                    elif top_health > health:
                        robots[top_idx] = (top_pos, top_health - 1, top_dir, top_original)
                        health = 0
                        break
                    else:
                        stack.pop()
                        health -= 1
                
                if health > 0:
                    robots[i] = (pos, health, dirc, idx)
                    stack.append(i)
        
        # collect survivors
        survivors = []
        for i in stack:
            survivors.append((robots[i][3], robots[i][1]))  # (original index, health)
        
        # sort by original index
        survivors.sort()
        
        return [h for _, h in survivors]