import hyperdiv as hd


@hd.global_state
class TaskState(hd.BaseState):
    """
    The global task state. It exposes properties and methods for
    reading and writing that state.
    """

    # Tasks are held in a prop that is a list of (string, int)
    # tuples, where the  first string is the name of the task, 
    # second field is an int that indicates how long it took to 
    # complete the task in seconds
    tasks = hd.Prop(
        hd.List(hd.Tuple(hd.PureString, hd.Int)),
        (
            ("Wash dishes", 300),
            ("Clean the room", 400),
            ("Walk the dog", 500),
        ),
    )

    def add_task(self, name, duration):
        if name not in (task for task, _duration in self.tasks):
            self.tasks = ((name, duration),) + self.tasks