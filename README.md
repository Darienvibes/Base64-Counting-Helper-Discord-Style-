# Base64 Counting Helper (Discord-Style)

A simple Python script I made for converting decimal numbers into Base64 strings—like the kind you see in Discord counting channels (e.g., `NTUwMA==` for `5500`) — and back again.

## Features

- Convert decimal numbers (e.g., `1234`) into Base64 counting strings (`MTIzNA==`)
- Decode Base64 counting strings back into decimal numbers
- Simple and interactive command-line interface
- Great for teaching or supporting newcomers in Discord-based counting events



## How It Works

This tool **does not convert numbers into Base64 as a numeral system** (like base conversions), but instead:

1. **Converts the number to a string**
2. **Encodes the string as bytes**
3. **Encodes the bytes using standard Base64**

This is the exact method used in many Base64 Discord counting bots and games.



## Usage

### Requirements
- Python 3.6+

### Run the Script

````bash
python base64_counting.py

Output Example

Option 1 – Encode Decimal:

Choose option (1 or 2): 1
Enter a decimal number: 5500
Base64 counting string: NTUwMA==

Option 2 – Decode Base64:

Choose option (1 or 2): 2
Enter Base64 counting string: NTUwMA==
Decoded decimal number: 5500




Example Conversion Table




Code Preview

import base64

def decimal_to_base64_counting(number: int) -> str:
    return base64.b64encode(str(number).encode('utf-8')).decode('utf-8')

def base64_counting_to_decimal(b64_string: str) -> int:
    return int(base64.b64decode(b64_string).decode('utf-8'))




Use Cases

Discord bot developers

Educational communities

Newcomers learning about encoding

Obfuscating numbers in a readable, reversible way





License

This project is open source and free to use under the MIT License.
