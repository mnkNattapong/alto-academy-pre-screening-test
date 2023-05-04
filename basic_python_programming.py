def calculate_temperature_stats():
    # Ask the user to enter the temperature for each day of the week
    temperatures = []
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_of_week:
        while True:
            temp_str = input(f"Enter temperature for {day} (or leave blank if unknown): ")
            if temp_str == "":
                break
            try:
                temp = float(temp_str)
                temperatures.append(temp)
                break
            except ValueError:
                print("Invalid temperature, please enter a number or leave blank.")

    if not temperatures:
        print("No temperature data entered.")
        return

    # Calculate the average temperature for the week
    avg_temp = sum(temperatures) / len(temperatures)
    print(f"Average temperature for the week: {avg_temp:.2f}")

    # Print out the highest and lowest temperatures for the week
    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)
    print(f"Highest temperature for the week: {highest_temp:.2f}")
    print(f"Lowest temperature for the week: {lowest_temp:.2f}")

    # Sort the temperatures in ascending order
    sorted_temps = sorted(temperatures)
    print("Temperatures in ascending order:", sorted_temps)

    # Calculate the variance of the temperatures for the week
    variance = sum((temp - avg_temp) ** 2 for temp in temperatures) / len(temperatures)
    print(f"Variance of temperatures for the week: {variance:.2f}")

calculate_temperature_stats()
