class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to keep track of seen numbers for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # Calculate sub-box index (0 to 8)
                box_idx = (i // 3) * 3 + j // 3
                
                # Check for duplicates in the current row, column, or sub-box
                if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                    return False
                
                # Add the value to our tracking sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)
                
        return True