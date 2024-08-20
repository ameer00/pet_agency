import threading
import hyperdiv as hd


@hd.global_state
class ChartState(hd.BaseState):
    coordinates = hd.Prop(
        hd.List(hd.Tuple(hd.Float, hd.Float)),
        []
    )
    def get_coordinates(self):
        # sort tuples by first element 
        sorted_coordinates = sorted(list(self.coordinates),key=lambda x: x[0])
        return dict(data=sorted_coordinates)
    
    def add_coordinates(self, x, y):
        self.coordinates = self.coordinates + ( (x, y), ) 

    def reset_coordinates(self):
        self.coordinates = []
