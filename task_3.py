import heapq

# Граф де кожен маршрут має вагу (небезпека переходу)
worlds_with_weight = {
    "Terra": [("Mars", 1), ("Cadia", 3)],
    "Mars": [("Terra", 1), ("Armageddon", 2)],
    "Cadia": [("Terra", 3), ("Fenris", 2)],
    "Armageddon": [("Mars", 2), ("Valhalla", 4)],
    "Fenris": [("Cadia", 2), ("Valhalla", 1)],
    "Valhalla": [("Armageddon", 4), ("Fenris", 1)]
}

def dijkstra(start, end):
    # Дейкстра - знаходить найкоротший шлях з урахуванням ваг
    distances = {world: float('inf') for world in worlds_with_weight}
    distances[start] = 0
    parent = {world: None for world in worlds_with_weight}
    
    # Пріоритетна черга: (відстань, світ)
    queue = [(0, start)]
    
    while queue:
        current_dist, current = heapq.heappop(queue)
        
        # Якщо знайшли коротший шлях - прогайпаємо
        if current_dist > distances[current]:
            continue
        
        # Проходимо по сусідам
        for neighbor, weight in worlds_with_weight[current]:
            new_distance = current_dist + weight
            
            # Якщо шлях коротше - оновлюємо
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = current
                heapq.heappush(queue, (new_distance, neighbor))
    
    # Відновлюємо шлях від end до start
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    
    return path[::-1], distances[end]

if __name__ == "__main__":
    start = "Terra"
    end = "Valhalla"
    
    route, total_cost = dijkstra(start, end)
    
    print(f"Найбезпечніший маршрут від {start} до {end}:\n")
    print(f"Шлях: {' -> '.join(route)}")
    print(f"Сумарна небезпека: {total_cost}")
