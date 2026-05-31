from shapes import Shape

class Hexagon(Shape):
    def __init__(self, shape_id, side, shape_type="hexagon", **kwargs):
        super().__init__(shape_id,shape_type)
        

        self.side = side

    def get_area(self):
        return (3 *  3 ** 0.5/2) * self.side**2
    
    def get_perimeter(self):
        return self.side * 6
    
    def to_dict(self):
        return {"id": self.shape_id, "type" : self.shape_type, "side": self.side} 
    
    # @classmethod
    # def input_data(cls, shape_id):
    #     side = validate_input("input side")
    #     return cls(shape_id, side)
    

