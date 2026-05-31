from shapes import Shape
from math import pi


class Circle(Shape):
    def __init__(self, shape_id, radius,shape_type = "circle", **kwargs):
        super().__init__(shape_id,shape_type)
        
        self.radius = float(radius)

    def get_area(self):
        return pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2*pi *self.radius
    
    def to_dict(self):
        return {"id": self.shape_id, "type" : self.shape_type, "radius": self.radius} 
    
    # @classmethod
    # def input_data(cls, shape_id):
    #     radius = validate_input("input radius")
    #     return cls(shape_id, radius)
    

