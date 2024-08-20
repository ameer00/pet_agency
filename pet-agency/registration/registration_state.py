import hyperdiv as hd


@hd.global_state
class RegistrationState(hd.BaseState):
    """
    The global registration state. It exposes properties and methods for
    reading and writing that state.
    """

    # Registrations are held in a prop that is a list of (string, string, bool)
    # tuples, where the  first string is the name of the pet, 
    # second string is the type of the pet (cat/dog) and the third indicates
    # if the pet is available for adoption or no 
    registrations = hd.Prop(
        hd.List(hd.Tuple(hd.PureString, hd.PureString, hd.Bool)),
        (
            ("Snoopy", "dog",  True),
            ("Sasha", "cat",  False),
            ("Billy", "dog", True),
        ),
    )

    def get_all_registrations(self):
        return self.registrations

    def toggle_registration(self, registration):
        self.registrations = tuple(
            (name, pet_type, (adopted if name != registration else not adopted)) for name, pet_type, adopted in self.registrations
        )

    def remove_registration(self, registration):
        self.registrations = tuple((name, pet_type, adopted) for name, pet_type, adopted in self.registrations if name != registration)

    @property
    def pets_left(self):
        return len([(name, pet_type,  adopted) for name, pet_type, adopted in self.registrations if not adopted])

    def clear_completed(self):
        self.registrations = tuple((name, pet_type, adopted) for name, pet_type, adopted in self.registrations if not adopted)

    @property
    def has_completed(self):
        return len([(name, pet_type, adopted) for name, pet_type, adopted in self.registrations if adopted]) > 0


    def add_registration(self, name, pet_type):
        if name not in (registration for registration, _pet_type, _adopted in self.registrations):
            self.registrations = ((name, pet_type, False),) + self.registrations

    @property
    def completed_registrations(self):
        return tuple((name, pet_type, adopted) for name, pet_type, adopted in self.registrations if adopted)

    @property
    def active_registrations(self):
        return tuple((name, pet_type, adopted) for name, pet_type, adopted in self.registrations if not adopted)


