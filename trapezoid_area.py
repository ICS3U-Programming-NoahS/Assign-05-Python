#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Dec 11th, 2023
# This program asks the user to enter
# the large side, small side and height of a trapezoid,
# as well as the units being used.
# It then calculates and displays the area of the trapezoid.


def calc_area(small_side, large_side, height):
    # Calculate area of trapezoid
    area = (small_side + large_side) / 2 * height

    # Return area to main
    return area


def main():
    while True:
        # greeting
        print("This program calculates the area of a trapezoid")
        print(
            "by asking you to enter the large side, small side and height of the trapezoid,"
        )
        print("as well as the units you are using.")

        # get small side, large side, height and unit from user
        small_side_str = input("Enter the length of the small side: ")
        large_side_str = input("Enter the length of the large side: ")
        height_str = input("Enter the height: ")
        unit = input("Enter the unit (e. g. cm, m, in): ")

        # Check if input is valid
        try:
            small_side_float = float(small_side_str)

            # If the small side is less or equal to 0
            if small_side_float <= 0:
                print("{} is not a valid side length.".format(small_side_float))

                # Repeats section of the loop
                continue

            try:
                large_side_float = float(large_side_str)

                # If the large side is less or equal to 0
                if large_side_float <= 0:
                    print("{} is not a valid side length.".format(large_side_float))

                    # Repeats section of the loop
                    continue

                try:
                    height_float = float(height_str)

                    # If the height is less or equal to 0
                    if height_float <= 0:
                        print("{} is not a valid height.".format(height_float))

                        # Repeats section of the loop
                        continue

                    # If the small side is longer than the large side
                    elif large_side_float < small_side_float:
                        print("The small side cannot be longer than the large side.")

                        # Repeats section of the loop
                        continue

                    else:
                        # Call function to get area
                        calculated_area = calc_area(
                            small_side_float, large_side_float, height_float
                        )

                        # Display area of trapezoid, with proper units
                        print(
                            "The area of the trapezoid is {:.2f} {}².".format(
                                calculated_area, unit
                            )
                        )

                        # Break after successful input
                        break
                except:
                    # height is not a float
                    print("{} is not a float.".format(height_str))

                    # Repeats section of the loop
                    continue
            except:
                # large side is not a float
                print("{} is not a float.".format(large_side_str))

                # Repeats section of the loop
                continue
        except:
            # small side is not a float
            print("{} is not a float.".format(small_side_str))

            # Repeats section of the loop
            continue


if __name__ == "__main__":
    main()
