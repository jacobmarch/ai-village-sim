from models.person import Person
from models.location import Location
import random

def create_village():
    village = Location("Meadowbrook", "A quaint village nestled in a lush valley.")
    
    # Create some villagers
    villagers = Person.load_villagers()

    # Add villagers to the village
    for villager in villagers:
        village.add_occupant(villager)

    return village

def simulate_day(village):
    print(f"\nA new day begins in {village.name}...")
    events = []

    # Morning: Each person reviews their goals and plans their day
    for person in village.occupants:
        try:
            person.review_goals()
            events.append(f"{person.name} plans to: {person.daily_action}")
        except Exception as e:
            print(f"Error during goal review for {person.name}: {str(e)}")

    # Afternoon: Each person takes their planned action
    for person in village.occupants:
        try:
            events.append(f"{person.name} is {person.daily_action}")
            person.take_action(person.daily_action)
        except Exception as e:
            print(f"Error during action for {person.name}: {str(e)}")
 
    # Evening: Random interactions between villagers
    for _ in range(len(village.occupants) // 2):  # Each villager has a chance to interact
        try:
            person1, person2 = random.sample(village.occupants, 2)
            interaction = person1.interact_with(person2)
            events.append(f"{person1.name} and {person2.name} interact: {interaction}")
        except Exception as e:
            print(f"Error during interaction: {str(e)}")

    # Night: Each person learns from their experiences
    for person in village.occupants:
        try:
            experience = f"spent the day {person.daily_action}"
            person.learn_from_experience(experience)
        except Exception as e:
            print(f"Error during learning for {person.name}: {str(e)}")

    # Print all events for the day
    for event in events:
        print(event)

def run_simulation():
    village = create_village()
    print(f"Welcome to {village.name}!")
    print(f"Population: {len(village.occupants)}")
    print("Villagers:")
    for villager in village.occupants:
        print(f"- {villager}")
    
    day = 1
    while True:
        print(f"\n--- Day {day} ---")
        simulate_day(village)
        user_input = input("\nPress Enter to continue to the next day, or type 'exit' to end the simulation: ").strip().lower()
        if user_input == 'exit':
            break
        day += 1

    print("\nSimulation ended.")