import hyperdiv as hd
from .registration_state import RegistrationState


"""
This is the header of the page.
Returns:
    Nothing, just render the elements 
Parameters:
    None
"""
def header():
    """
    TODO: Add to the form:
        1. A text input form where users will type the name of the pet
            1.2 Placeholder for text input: "Pet name?"
        2. A radio group where users will choose between dog or cat type 
        3. An "add" button
        3.1 The "add button" should be a submit button for the form
        3.2 When the form is submitted, add the pet to the list of registrations 
    """    
    # class that stores the pet registrations
    registrations = RegistrationState()
    with hd.hbox(
        padding=1,
        gap=1,
        align="center",
        border_bottom="1px solid neutral-200",
    ):
        
        # Input form
        with hd.form(direction="horizontal") as form:

            # text input in the form to type the name of the pet 
            form.text_input(name="pet_name", placeholder="Pet name?")
            
            # add two radio buttons to the form to choose between cat and dog
            
            
            # add submit button

            # when form is submitted add information about pets to the registration 

            
"""
This is a building block of the rendered list of registrations. 
Returns:
    Returns nothing, just render the elements 
Parameters:
    registration (string): name of the pet in the registration 
    pet_type (string): type of the pet (dog or cat)
    adopted (bool): whether the pet was adopted or not
    last_item (bool): whether this is the last item in the list of registrations
"""
def registration_row(registration,  pet_type, adopted, last_item=False):
    """
    this is the element registration row and it represents each one of
    the pets added in the RegistrationState(). This is a building block of the 
    rendered list of registrations. 
    TODO: Add toggle button  that works as a toggle button:
         1. When button is clicked, it should be able to update/toggle the registration 
        of the pet in the registration list. 
         2. when the pet is adopted, the text of the button should be "Adopted" but
         if the pet is available, it should be "Available"


    style:
        2.1 If the pet was adopted, the button should be:
            2.1.1 Green green-50
            2.1.2 Have border 1px solid green-300
            2.1.3 Have a prefix icon called "check"
        2.2 Otherwise,if pet was not adopted 
            2.2.1 it should use default values for style
            2.2.2 have a prefix icon called of dot
    """
    registrations = RegistrationState()

    with hd.hbox(
        padding=1,
        gap=1,
        align="center",
        border_bottom=(None if last_item else "1px solid neutral-200"),
    ):
        
        with hd.box(width=10, align="center"):
            # TODO: add the registration toggle button
            pass

        hd.text(f"{registration} ({pet_type})", grow=1, font_color="neutral-800")



"""
Building block for when there are no registrations to render. 
Returns:
    Returns nothing, just render the elements 
"""
def nothing_here():
    with hd.box(padding=1.5, align="center", justify="center"):
        hd.text("There are no pets here.", font_color="neutral-500")



"""
Renders the list of registrations or the nothing_here component if there are no registrations
Returns:
    Returns nothing, just render the elements 
"""
def registrations_list():
    registrations = RegistrationState()
    
    registration_items = registrations.get_all_registrations()
    print(registration_items)

    if registration_items:
        with hd.box(vertical_scroll=True):
            for i, (registration, pet_type, adopted) in enumerate(registration_items):
                with hd.scope(registration):
                    registration_row(registration, pet_type, adopted, last_item=i == len(registration_items) - 1)
    else:
        nothing_here()


def footer():
    """
    The footer, rendering the count of pets left, the nav
    """

    registrations = RegistrationState()

    with hd.hbox(
        justify="space-between",
        align="center",
        padding=1,
        height=3,
        border_top="1px solid neutral-200",
    ):
        # Count
        hd.text(
            f"{registrations.pets_left} pet{'s' if registrations.pets_left != 1 else ''} for adoption",
            basis=0,
            grow=1,
        )


def main():
    app = hd.template(title="Pet Registration App", sidebar=False)
    app.body.align = "center"
    with app.body:
        with hd.box(
            background_color="neutral-50",
            border="1px solid neutral-200",
            width=40,
            border_radius="large",
            vertical_scroll=False,
        ):
            header()
            registrations_list()
            footer()
