from shapes import Shape

class Rectangle(Shape):
    def __init__(self, shape_id, width, height, shape_type="rectangle", **kwargs):
        super().__init__(shape_id, shape_type)
        
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (self.height + self.width) * 2
    
    def to_dict(self):
        return {"id": self.shape_id, "type" : self.shape_type, "width": self.width, "height": self.height}

    # @classmethod
    # def input_data(cls, shape_id):
    #     width = validate_input("input width")
    #     height = validate_input("input height")
    #     return cls(shape_id, width, height) 
    

