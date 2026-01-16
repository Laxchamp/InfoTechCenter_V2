# Welcome Branch
# This program simulates a colorful OS-style boot screen

# Libraries Imported Here
import sys      # Lets us control terminal output
import time     # Lets us add delays for animation timing
import os       # Used to enable ANSI color support on Windows

# Enable ANSI escape codes on Windows terminals
# (Does nothing on Mac/Linux, safe to include)
os.system("")

# ANSI color codes for terminal text coloring
RESET   = "\033[0m"   # Resets text back to normal color
GREEN   = "\033[92m"  # Bright green text
CYAN    = "\033[96m"  # Bright cyan text
YELLOW  = "\033[93m"  # Bright yellow text
MAGENTA = "\033[95m"  # Bright magenta text

# Print the title lines in color
print(f"\n{MAGENTA}Welcome Branch - Developer Cole{RESET}")
print(f"\n{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

# x controls how long the boot loop runs
x = 0

# ellipsis controls how many dots appear after "Booting"
ellipsis = 0

# Main boot animation loop
# Runs until x reaches 20 cycles
while x != 20:
    x += 1  # Increase loop counter each cycle

    # Build the boot message with a growing number of dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1  # Increase dot count each loop

    # Write the message on the same line (\r returns cursor to line start)
    # \033[K clears the rest of the line
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Forces the text to appear immediately

    # Pause to create animation timing
    time.sleep(.5)

    # Reset dots after 3 so it cycles "...", then starts over
    if ellipsis == 4:
        ellipsis = 0

    # When loop finishes, print the success message
    if x == 20:
        print(f"\n{GREEN}Operating System Booted Up - Retina Access Granted{RESET}")


