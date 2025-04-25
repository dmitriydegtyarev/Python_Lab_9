import re

# Open file
def create_file():
    try:
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sed metus ut ex congue efficitur nec id orci."

        file = open("TF1_1.txt", "w")
        print("File TF1_1.txt was opened.")
        file.write(text)
        print("File TF1_1.txt was changed.")
        file.close()
        print("File TF1_1.txt was closed.")

    except Exception as e:
        print(f"Open file error: {e}")

# File processing
def process_file():
    try:
        file = open("TF1_1.txt", "r")
        print("File TF1_1.txt was opened.")
        content = file.read()
        print("File TF1_1.txt was read.")
        file.close()
        print("File TF1_1.txt was closed.")

        words = re.findall(r'\b\w+\b', content)

        file = open("TF1_2.txt", "w")
        print("File TF1_2.txt was opened.")
        for word in words:
            file.write(word + "\n")
        print("File TF1_2.txt was changed.")
        file.close()
        print("File TF1_2.txt was closed.")

    except FileNotFoundError:
        print("Error: File TF1_1.txt not found. Run first create_file().")
    except Exception as e:
        print(f"Error processing file: {e}")

# --- 3. Читання TF1_2.txt ---
def read_file():
    try:
        file = open("TF1_2.txt", "r")
        print("File TF1_2.txt was opened.")
        for line in file:
            print(line.strip())
        file.close()
        print("File TF1_2.txt was closed.")

    except FileNotFoundError:
        print("Error: File TF1_2.txt not found. Run first create_file().")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    while True:
        print("\nMenu:"
              "\n1 -> Create file TF1_1.txt"
              "\n2 -> Process file (remove punctuation)"
              "\n3 -> Display Content TF1_2.txt"
              "\n4 -> Exit")

        choice = input("Your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            process_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            print("Complete the program.")
            break
        else:
            print("Invalid input. Choose one of the options..")

if __name__ == "__main__":
    main()