from shapes import Shape

class Square(Shape):
    def __init__(self, shape_id, side, shape_type="square", **kwargs):
        super().__init__(shape_id, shape_type)
        
        self.side = side
        
    def get_area(self):
        return self.side * self.side
    
    def get_perimeter(self):
        return self.side * 4
    
    def to_dict(self):
        return {"id": self.shape_id, "type" : self.shape_type, "side": self.side} 
    
    # @classmethod
    # def input_data(cls, shape_id):
    #     side = validate_input("input side")
    #     return cls(shape_id, side)
    



