def calculate_distance(name, good_string):
    total_distance = 0
    prev_good_char = good_string[0]

    for char in name:
        min_distance = float('inf')
        nearest_char = None

        for good_char in good_string:
            distance = abs(ord(char) - ord(good_char))
            if distance < min_distance:
                min_distance = distance
                nearest_char = good_char
            elif distance == min_distance:  # Check if equidistant
                if abs(ord(good_char) - ord(prev_good_char)) < abs(ord(nearest_char) - ord(prev_good_char)):
                    nearest_char = good_char

        total_distance += min_distance
        prev_good_char = nearest_char

    return total_distance

# Get input
good_string = input()
name = input()

# Calculate and print the distance
distance = calculate_distance(name, good_string)
print(distance)
