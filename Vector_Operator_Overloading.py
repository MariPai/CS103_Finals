class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Adding only Vector instances
        if not isinstance(other, Vector):
            raise TypeError("Error: Only Vector instances can be added.")
        
        # Vector addition
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Test block
if __name__ == "__main__":
    v1 = Vector(5, 12)
    v2 = Vector(13, 23)
    
    # This will successfully add v1 and v2
    try:
        sum_vector = v1 + v2
        print("Sum:", sum_vector)
    except TypeError as e:
        print(e)

    # This will raise the TypeError because we're adding a non-vector type
    try:
        invalid_add = v1 + "not a vector"
        print("Sum:", invalid_add)
    except TypeError as e:
        print(e)
