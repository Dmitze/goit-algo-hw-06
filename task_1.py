import networkx as nx
import matplotlib.pyplot as plt

class WarhammerMap:
    def __init__(self):
        self.graph = nx.Graph()
        self._add_worlds()
    
    def _add_worlds(self):
        # Додаємо 6 світів
        worlds = ["Terra", "Mars", "Cadia", "Fenris", "Armageddon", "Valhalla"]
        self.graph.add_nodes_from(worlds)
        
        # Додаємо маршрути (кількість зв'язків)
        connections = [
            ("Terra", "Mars"),
            ("Terra", "Cadia"),
            ("Mars", "Armageddon"),
            ("Cadia", "Fenris"),
            ("Armageddon", "Valhalla"),
            ("Fenris", "Valhalla")
        ]
        self.graph.add_edges_from(connections)
    
    def print_info(self):
        # Виводимо базову інформацію про граф
        print(f"Світів всього: {self.graph.number_of_nodes()}")
        print(f"Маршрутів всього: {self.graph.number_of_edges()}")
        
        # Показуємо скільки маршрутів від кожного світу
        for node in self.graph.nodes():
            count = self.graph.degree(node)
            print(f"{node}: {count} маршрутів")
    
    def draw(self):
        # Рисуємо граф на екран
        pos = nx.spring_layout(self.graph, seed=42)
        
        nx.draw_networkx_nodes(self.graph, pos, node_color="lightblue", node_size=1000)
        nx.draw_networkx_edges(self.graph, pos, width=2)
        nx.draw_networkx_labels(self.graph, pos)
        
        plt.title("Карта варп-маршрутів")
        plt.axis('off')
        plt.savefig("Figure.png", dpi=100, bbox_inches='tight')
        plt.show()

if __name__ == "__main__":
    galaxy = WarhammerMap()
    galaxy.print_info()
    galaxy.draw()
