import base64

def decimal_to_base64_counting(number: int) -> str:
    # Convert number to string, encode to bytes, then base64
    return base64.b64encode(str(number).encode('utf-8')).decode('utf-8')

def base64_counting_to_decimal(b64_string: str) -> int:
    # Decode base64 to bytes, then decode to string and convert to int
    try:
        decoded = base64.b64decode(b64_string).decode('utf-8')
        return int(decoded)
    except Exception:
        raise ValueError("Invalid Base64 counting format.")

def main():
    print("Base64 Counting Helper (Discord-style)")
    print("1. Convert decimal number to Base64 counting format")
    print("2. Convert Base64 counting string to decimal number")
    choice = input("Choose option (1 or 2): ").strip()

    if choice == "1":
        number = input("Enter a decimal number (e.g., 5500): ").strip()
        if number.isdigit():
            encoded = decimal_to_base64_counting(int(number))
            print(f"Base64 counting string: {encoded}")
        else:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        b64 = input("Enter Base64 counting string (e.g., NTUwMA==): ").strip()
        try:
            decoded = base64_counting_to_decimal(b64)
            print(f"Decoded decimal number: {decoded}")
        except ValueError:
            print("Invalid Base64 string or format.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
