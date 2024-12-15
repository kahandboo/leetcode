import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]
        total_cost = 0
        
        while len(visited) < n:
            cost, current = heapq.heappop(min_heap)
            
            if current in visited:
                continue
            
            visited.add(current)
            total_cost += cost
            
            for next_point in range(n):
                if next_point not in visited:
                    manhattan_distance = abs(points[current][0] - points[next_point][0]) + abs(points[current][1] - points[next_point][1])
                    heapq.heappush(min_heap, (manhattan_distance, next_point))
        
        return total_cost
