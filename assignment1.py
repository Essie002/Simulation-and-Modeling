import random  

# Function to simulate rolling a dice 1000 times and count frequencies
def simulate_dice_rolls():
    frequency1 = frequency2 = frequency3 = frequency4 = frequency5 = frequency6 = 0  # Initializing frequencies for each face
    for _ in range(1000):  # Looping 1000 times for 1000 dice rolls
        x = random.random()  # Generating a random float between 0 and 1
        if 0 <= x < 1/6:  # Checking which range the random number falls into
            frequency1 += 1
        elif 1/6 <= x < 2/6:
            frequency2 += 1
        elif 2/6 <= x < 3/6:
            frequency3 += 1
        elif 3/6 <= x < 4/6:
            frequency4 += 1
        elif 4/6 <= x < 5/6:
            frequency5 += 1
        else:
            frequency6 += 1
    return [frequency1, frequency2, frequency3, frequency4, frequency5, frequency6]  # Returning frequencies for each face

# Function to display the table of frequencies and percentages
def display_table(frequencies):
    print("Face  | Frequency | Percentage")  # Printing the table headers
    print("-" * 28)  # Printing a separator line
    total_rolls = sum(frequencies)  # Calculating the total number of rolls
    for face, frequency in enumerate(frequencies, start=1):  # Looping through each face and its frequency
        percentage = (frequency / total_rolls) * 100  # Calculating the percentage
        print(f" {face}    |    {frequency}    |    {percentage:.1f}%")  # Printing the face, frequency, and percentage
    print("-" * 28)  # Printing a separator line
    print(f"Total  |    {total_rolls}    |    100.0%")  # Printing the total number of rolls and 100%

# Main function to run the simulation and display the table
def main():
    frequencies = simulate_dice_rolls()  # Simulating dice rolls and getting frequencies
    display_table(frequencies)  # Displaying the table of frequencies and percentages

if __name__ == "__main__":
    main()  # Calling the main function when the script is executed directly

#