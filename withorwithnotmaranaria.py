# Welcome Branch
# Libraries Imported Here
import sys
import time

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

print(f"\n{MAGENTA}Welcome Branch - Developer Cole{RESET}")
print(f"\n{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1

    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()
    time.sleep(.5)

    if ellipsis == 4:
        ellipsis = 0

    if x == 20:
        print(f"\n{GREEN}Operating System Booted Up - Retina Access Granted{RESET}")


