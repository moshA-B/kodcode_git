from shapes import Shape

class Triangle(Shape):
    def __init__(self, shape_id, side1, side2, side3, shape_type = "triangle", **kwargs):
        super().__init__(shape_id, shape_type)
        
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        s = ((self.side1 + self.side2 + self.side3) / 2)
        return  (s*(s - self.side1)*(s - self.side2)*(s - self.side3)) **0.5
    
    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def to_dict(self):
        return {"id": self.shape_id, "type" : self.shape_type, "side1": self.side1,"side2": self.side2, "side3": self.side3}
    
    # @classmethod
    # def input_data(cls, shape_id):
    #     side1 = validate_input("input side1")
    #     side2 = validate_input("input side2")
    #     side3 = validate_input("input side3")

    #    return cls(shape_id, side1, side2, side3)
    

