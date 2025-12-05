from collections import deque

# Простий словник як граф - ключ це світ, значення це сусідні світи
worlds_map = {
    "Terra": ["Mars", "Cadia"],
    "Mars": ["Terra", "Armageddon"],
    "Cadia": ["Terra", "Fenris"],
    "Armageddon": ["Mars", "Valhalla"],
    "Fenris": ["Cadia", "Valhalla"],
    "Valhalla": ["Armageddon", "Fenris"]
}

def dfs(start, end, visited=None):
    # DFS - йдемо в глибину, перевіряємо першого сусіда до кінця
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    if start == end:
        return [start]
    
    for neighbor in worlds_map[start]:
        if neighbor not in visited:
            path = dfs(neighbor, end, visited)
            if path:
                return [start] + path
    
    return None

def bfs(start, end):
    # BFS - йдемо шарами, спочатку сусіди, потім сусіди сусідів
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path
        
        for neighbor in worlds_map[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

if __name__ == "__main__":
    start = "Terra"
    end = "Valhalla"
    
    dfs_result = dfs(start, end)
    bfs_result = bfs(start, end)
    
    print(f"Пошук маршруту від {start} до {end}:\n")
    print(f"DFS: {' -> '.join(dfs_result)} ({len(dfs_result)} світів)")
    print(f"BFS: {' -> '.join(bfs_result)} ({len(bfs_result)} світів)")
