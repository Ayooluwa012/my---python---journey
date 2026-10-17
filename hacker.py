import time
import random
import os

def slow_print(text, delay=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

os.system("cls" if os.name == "nt" else "clear")

print("=" * 45)
slow_print("   INITIALIZING SECRET SYSTEM...", 0.05)
print("=" * 45)

time.sleep(1)

messages = [
    "[+] Connecting to secure server...",
    "[+] Bypassing firewall...",
    "[+] Decrypting encrypted files...",
    "[+] Scanning network...",
    "[+] Accessing classified database...",
    "[+] Downloading secret files..."
]

for message in messages:
    slow_print(message)
    time.sleep(random.uniform(0.5, 1.2))
    print(f"    Progress: {random.randint(70, 99)}%")

print()

for i in range(30):
    print("".join(random.choice("01ABCDEF") for _ in range(45)))
    time.sleep(0.06)

print()
slow_print("!!! SYSTEM ACCESS GRANTED !!!", 0.08)
slow_print("WELCOME, AGENT AYOOLUWA.", 0.08)
slow_print("YOUR NEXT MISSION AWAITS...", 0.08)

print("\n" + "=" * 45)