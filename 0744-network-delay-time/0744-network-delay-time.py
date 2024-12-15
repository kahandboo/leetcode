import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        

        min_time = {i: float('inf') for i in range(1, n + 1)}
        min_time[k] = 0 


        priority_queue = [(0, k)]
        
        while priority_queue:
            current_time, current_node = heapq.heappop(priority_queue)
            
            if current_time > min_time[current_node]:
                continue
            
            for neighbor, travel_time in graph[current_node]:
                time = current_time + travel_time
                
                if time < min_time[neighbor]:
                    min_time[neighbor] = time
                    heapq.heappush(priority_queue, (time, neighbor))
        

        max_time = max(min_time.values())
        return max_time if max_time < float('inf') else -1