from simulation import run_simulation

if __name__ == "__main__":
    print("Welcome to the AI Village Simulation!")
    print("The simulation will continue until you type 'exit'.")
    print("Press Enter to simulate the next day, or type 'exit' to end the simulation.")
    user_input = input("Press Enter to start the simulation...")
    if user_input.lower() != 'exit':
        run_simulation()
    else:
        print("Simulation ended by user.")