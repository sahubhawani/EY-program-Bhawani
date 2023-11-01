"""
During a hiking trip, a group of friends decided to explore a cave. They encountered a series of tunnels with different lengths. Write a Python program that prompts the user to enter the length of a tunnel in meters. Depending on the length of the tunnel, the program should display a message describing the tunnel's classification:

Tunnels shorter than 100 meters are classified as "Short tunnels."
Tunnels between 100 and 500 meters are classified as "Medium tunnels."
Tunnels longer than 500 meters are classified as "Long tunnels."
"""

# take user input
tunnel_length = int(input("Please type the length of the tunnel is meter:"))

if tunnel_length <100:
    print("Short tunnel")

elif tunnel_length > 100 and tunnel_length < 500:
    print("Medium tunnel")

elif tunnel_length >500:
    print("Long tunnel")