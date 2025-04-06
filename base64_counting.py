import base64

def decimal_to_base64_counting(number: int) -> str:
    return base64.b64encode(str(number).encode('utf-8')).decode('utf-8')

def base64_counting_to_decimal(b64_string: str) -> int:
    try:
        decoded = base64.b64decode(b64_string).decode('utf-8')
        return int(decoded)
    except Exception:
        raise ValueError("Invalid Base64 counting format.")

def main():
    print("Base64 Counting Helper (Discord-style)")
    while True:
        print("\n1. Convert decimal number to Base64 counting format")
        print("2. Convert Base64 counting string to decimal number")
        print("3. Exit")
        choice = input("Choose option (1, 2, or 3): ").strip()

        match choice:
            case "1":
                number = input("Enter a decimal number: ").strip()
                if number.isdigit():
                    print(f"Base64 counting string: {decimal_to_base64_counting(int(number))}")
                else:
                    print("Invalid input. Please enter a valid number.")
            case "2":
                b64 = input("Enter Base64 counting string: ").strip()
                try:
                    print(f"Decoded decimal number: {base64_counting_to_decimal(b64)}")
                except ValueError:
                    print("Invalid Base64 string or format.")
            case "3":
                print("Exiting. Goodbye!")
                break
            case _:
                print("Invalid option.")

if __name__ == "__main__":
    main()
