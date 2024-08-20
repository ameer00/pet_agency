import hyperdiv as hd
from registration_state import RegistrationState

def main():
    registrations = RegistrationState()

    # Add a new registration /  pet to the list of registrations 

    new_pet = "Jimmy"
    pet_type = "Cat"

    # pet is registered as available 
    registrations.add_registration(new_pet, pet_type)

    # toggle / changes the pet availability status 
    # we always access the registration of the pet using its name
    # suppose we want to make Jimmy adopted
    registrations.toggle_registration("Jimmy")

    # we can make Jimmy be available again by toggling it 
    registrations.toggle_registration("Jimmy") 

    # loop through/iterate through all the registrations
    # and print al of them

    # get the list of pets / registrations
    registration_items = registrations.get_all_registrations()

    if registration_items:
        for i, (registration, pet_type, adopted) in enumerate(registration_items):
            print(f"Registration {i}: {registration}, {pet_type}, {adopted}")
            last_item = i == len(registration_items) - 1
            if last_item:
                print("This was the last pet!!")
    else:
        print("No pet registrations found.")

if __name__ == "__main__":
    hd.run(main)



