from hexagon import Hexagon
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from circle import Circle
import os
import json


class ShapeManager:

    def __init__(self, available_shapes):
        self.available_shapes = available_shapes
        self.shapes = []
        self.shape_id = 0
        self.load_from_json(self.available_shapes)

    def create_shape(self, shape,**kwargs):
        self.shape_id += 1
        self.shapes.append(shape(self.shape_id, **kwargs))
        self.save_to_json()

    def get_all_shapes(self):
        shape_list = [shape.to_dict() for shape in self.shapes]
        return shape_list

    def update_shape(self, shape_id, new_data):
        for shape in self.shapes:
            if shape_id == shape.shape_id:
                for k, v in new_data.items():
                    setattr(shape, k, v)
                self.save_to_json()
                return

    def delete_shape(self, shape_id):
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                self.shapes.remove(shape)
                break
        self.save_to_json()
        return

    def save_to_json(self):

        with open("shapes.json", "w") as f:
            shape_list = [shape.to_dict() for shape in self.shapes]
            json.dump(shape_list, f, indent=4)

        return

    def load_from_json(self, available_shapes):
        if not os.path.exists("shapes.json"):
            return
        
        with open("shapes.json", "r") as f:
            try:
                data = json.load(f)
            except Exception:
                return

            max_id = 0
            for shape in data:
                shape_type = shape.pop("type")
                shape_id = shape.pop("id")

                instance = available_shapes[shape_type](shape_id, **shape)
                self.shapes.append(instance)

                if shape_id > max_id:
                    max_id = shape_id
            
            self.shape_id = max_id
        return


