class RecyclingSystem:
    def __init__(self):
        self.recycling_efficiency = 0.75  # 75% efficiency in recycling

    def recycle_materials(self, materials):
        """
        Simulates the recycling of materials, particularly lunar regolith.
        
        :param materials: Dictionary of materials selected for recycling
        :return: Dictionary of recycled materials
        """
        recycled_materials = {}
        for material, quantity in materials.items():
            recycled_quantity = quantity * self.recycling_efficiency
            recycled_materials[material] = recycled_quantity
        return recycled_materials
