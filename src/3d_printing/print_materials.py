# print_materials.py

class PrintMaterial:
    def __init__(self, name, density, melting_point, tensile_strength, cost, compatibility, environmental_impact, availability):
        self.name = name
        self.density = density  # in g/cm^3
        self.melting_point = melting_point  # in °C
        self.tensile_strength = tensile_strength  # in MPa
        self.cost = cost  # in $/kg
        self.compatibility = compatibility  # List of compatible printing technologies
        self.environmental_impact = environmental_impact  # Scale of 1-10 (1 being low impact)
        self.availability = availability  # Availability score (1-10)

    def __repr__(self):
        return (f"{self.name}: Density={self.density} g/cm³, Melting Point={self.melting_point}°C, "
                f"Tensile Strength={self.tensile_strength} MPa, Cost=${self.cost}/kg, "
                f"Compatibility={self.compatibility}, Environmental Impact={self.environmental_impact}, "
                f"Availability={self.availability}")

class MaterialManager:
    def __init__(self):
        self.materials = []

    def add_material(self, material):
        self.materials.append(material)

    def get_materials(self):
        return self.materials

    def select_material(self, min_strength=None, max_cost=None, min_availability=None, max_impact=None):
        selected_materials = []
        for material in self.materials:
            if (min_strength is None or material.tensile_strength >= min_strength) and \
               (max_cost is None or material.cost <= max_cost) and \
               (min_availability is None or material.availability >= min_availability) and \
               (max_impact is None or material.environmental_impact <= max_impact):
                selected_materials.append(material)
        return selected_materials

    def display_materials(self):
        for material in self.materials:
            print(material)

# Example usage
if __name__ == "__main__":
    # Create a MaterialManager instance
    manager = MaterialManager()

    # Add some materials with advanced features
    manager.add_material(PrintMaterial("PLA", 1.24, 180, 50, 20, ["FDM"], 3, 8))
    manager.add_material(PrintMaterial("ABS", 1.04, 220, 40, 25, ["FDM"], 5, 7))
    manager.add_material(PrintMaterial("PETG", 1.27, 230, 50, 30, ["FDM", "SLS"], 4, 9))
    manager.add_material(PrintMaterial("Nylon", 1.15, 260, 70, 35, ["FDM", "SLS"], 6, 6))

    # Display all materials
    print("Available Materials:")
    manager.display_materials()

    # Select materials based on advanced criteria
    print("\nSelected Materials (Strength >= 50 MPa, Cost <= $30/kg, Availability >= 7, Impact <= 5):")
    selected = manager.select_material(min_strength=50, max_cost=30, min_availability=7, max_impact=5)
    for mat in selected:
        print(mat)
