import Tile_Classes as tc
import heapq

##############################################################
# This script is used to calculate a path between two points #
##############################################################


# Start with the starting cell in the open list, and nothing in the closed list.

# Remove the cell with the lowest


# G == Cost to move to this cell
# H == Estimation of cost to move to ending cell (ie, calculate distance if no walls are present)
# F == The sum of the two above values

class AStar:

    def __init__(self, area,_start, _end):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = area
        self.grid_height = len(area)
        self.grid_width = len(area[0])
        self.start = _start
        self.end = _end

    def get_heuristic(self, cell):        
        return abs(cell.pos[0] - self.end.pos[0]) + abs(cell.pos[1] - self.end.pos[1])        
    

    def get_cell(self, x, y):
        for row in self.cells:
            for cell in row:
                if cell.pos == (x,y):
                    return cell

    def get_adjacent_cells(self, cell):
        cells = []
        if cell.pos[0] < self.grid_width -1:
            cells.append(self.get_cell(cell.pos[0] +1 , cell.pos[1]))
        if cell.pos[1] > 0:
            cells.append(self.get_cell(cell.pos[0], cell.pos[1] - 1))
        if cell.pos[0] > 0:
            cells.append(self.get_cell(cell.pos[0] - 1, cell.pos[1]))
        if cell.pos[1] < self.grid_height -1:
            cells.append(self.get_cell(cell.pos[0], cell.pos[1] + 1))
        return cells

    def finalise_path(self):
        cell = self.end
        path_list = []
        path_list.append(self.end.pos)
        while cell.parent is not self.start:
            cell = cell.parent
            path_list.append(cell.pos)
            print ('path: cell: %d,%d' % (cell.pos[0], cell.pos[1]))
        return path_list

    def update_cell(self, adj, cell):
        adj.g = cell.g + 1
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g


    def process(self):
        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))

        while len(self.opened):
            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)
            # add cell to closed list so we don't process it twice
            self.closed.add(cell.pos)
            # if ending cell, display found path
            if cell.pos is self.end.pos:
                
                return self.finalise_path()
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.walkable and adj_cell.pos not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found for this adj
                        # cell.
                        if adj_cell.g > cell.g + 1:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))



