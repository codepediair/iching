import os
import sys

class YiJing:
    def cast_hexagram(self):
        print("Casting coins... (擲筊占卜)")
        # پیاده‌سازی واقعی اینجا قرار می‌گیره

    def lookup_hexagram(self):
        number = input("Enter hexagram number (1-64): ")
        print(f"Looking up hexagram {number}...")
        # پیاده‌سازی واقعی اینجا قرار می‌گیره

def main():
    app = YiJing()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================")
        print("           易經 (I Ching) Explorer      ")
        print("========================================")
        print("1) Cast coins (擲筊占卜)")
        print("2) Lookup hexagram by number (1-64)")
        print("3) Exit")
        choice = input("Choose: ")

        if choice == "1":
            app.cast_hexagram()
        elif choice == "2":
            app.lookup_hexagram()
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid")

        input("\nPress any key to continue...")

if __name__ == "__main__":
    main()
