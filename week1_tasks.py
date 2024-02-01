# TASK 1
def input_weights_and_names():
    weights = []
    names = []

    for i in range(1, 31):
        name = input(f"Enter name for pupil {i}: ")
        weight = float(input(f"Enter weight for {name} (in kg): "))

        # Validate weight
        while weight <= 0:
            print("Invalid weight. Weight must be greater than 0.")
            weight = float(input(f"Enter valid weight for {name} (in kg): "))

        names.append(name)
        weights.append(weight)

    return names, weights

# TASK 2
def calculate_weight_difference(initial_weights, final_weights):
    differences = [final - initial for initial, final in zip(initial_weights, final_weights)]
    return differences

# TASK 3
def check_and_output_difference(names, differences):
    for name, difference in zip(names, differences):
        if abs(difference) > 2.5:
            if difference > 0:
                print(f"{name}: Weight increased by {difference} kilograms.")
            else:
                print(f"{name}: Weight decreased by {abs(difference)} kilograms.")

def main():
    # TASK 1
    print("TASK 1: Enter weights and names for 30 pupils.")
    names, initial_weights = input_weights_and_names()

    # TASK 2
    print("\nTASK 2: Enter final weights for the same 30 pupils.")
    final_weights = input_weights_and_names()[1]

    # TASK 3
    print("\nTASK 3: Differences in weight greater than 2.5 kg.")
    differences = calculate_weight_difference(initial_weights, final_weights)
    check_and_output_difference(names, differences)

if __name__ == "__main__":
    main()



