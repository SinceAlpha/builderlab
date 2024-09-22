# Input positions from the user
nozzle_x_position = float(input("Enter the nozzle X position: "))
nozzle_y_position = float(input("Enter the nozzle Y position: "))
probe_x_position = float(input("Enter the probe X position: "))
probe_y_position = float(input("Enter the probe Y position: "))

# Calculate offsets
x_offset = nozzle_x_position - probe_x_position
y_offset = nozzle_y_position - probe_y_position

# Output the calculated offsets
print(f"X Offset: {x_offset}")
print(f"Y Offset: {y_offset}")

print("\nUpdate your printer.cfg with these values, remove tape/marks from the bed, and issue a RESTART command.")
