#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on August 2020
# This program calculates the total cost of a pizza

import constants


def main():
    # This function calculates the total cost of a pizza

    # Input
    diameter = int(input("Enter the diameter of the desired pizza (inch): "))

    # Process
    sub_total = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total * constants.HST  # HST is set to 1.13

    # Output
    print("")
    print("The cost for a {0}in pizza is: ${1:,.2f}".format(diameter, total))


if __name__ == "__main__":
    main()
