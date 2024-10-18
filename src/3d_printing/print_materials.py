import random

class MaterialSelector:
    def __init__(self):
        self.available_materials = ['lunar regolith', 'plastic', 'metal', 'composite']

    def select_materials(self):
        """
        Simulates the selection of materials for 3D printing.
        
        :return: Dictionary of selected materials and their quantities
        """
        selected_materials = {
            material: random.randint(1, 10) for material in self.available_materials
        }
        return selected_materials
