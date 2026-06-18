# Example.code
# class CaesarCipherEngine:
#     def __init__(self, shift: int):
#         """
#         Constructor: Initialize the cipher with a specific shift key.
#         Using modulo 26 ensures that any large integer wrap around cleanly.
#         """
#         self.shift = shift % 26

#     def encrypt(self, plaintext: str) -> str:
#         """
#         Encrypts the raw plaintext into secured ciphertext using the IPO model logic.
#         """
#         ciphertext = ""
#         for char in plaintext:
#             # Task Checklist: Handle Uppercase Letters (ASCII 65 to 90)
#             if char.isupper():
#                 ascii_val = ord(char)
#                 zero_indexed = ascii_val - 65
#                 shifted = (zero_indexed + self.shift) % 26
#                 ciphertext += chr(shifted + 65)
            
#             # Task Checklist: Handle Lowercase Letters (ASCII 97 to 122)
#             elif char.islower():
#                 ascii_val = ord(char)
#                 zero_indexed = ascii_val - 97
#                 shifted = (zero_indexed + self.shift) % 26
#                 ciphertext += chr(shifted + 97)
            
#             # Edge Case Checklist: Leave spaces and punctuation untouched
#             else:
#                 ciphertext += char
                
#         return ciphertext

#     def decrypt(self, ciphertext: str) -> str:
#         """
#         Decrypts the ciphertext back to plaintext by reversing the mathematical shift.
#         """
#         plaintext = ""
#         for char in ciphertext:
#             # Reverse logic for Uppercase
#             if char.isupper():
#                 ascii_val = ord(char)
#                 zero_indexed = ascii_val - 65
#                 shifted = (zero_indexed - self.shift) % 26
#                 plaintext += chr(shifted + 65)
            
#             # Reverse logic for Lowercase
#             elif char.islower():
#                 ascii_val = ord(char)
#                 zero_indexed = ascii_val - 97
#                 shifted = (zero_indexed - self.shift) % 26
#                 plaintext += chr(shifted + 97)
            
#             # Keep spaces and symbols as they are
#             else:
#                 plaintext += char
                
#         return plaintext


# # --- INTERACTIVE USER INTERFACE (IPO Implementation) ---
# if __name__ == "__main__":
#     print("=== DecodeLabs Cryptographic Engine ===")
    
#     # 1. Input Logic: Take data and key from user
#     user_message = input("Enter your secret message: ")
#     try:
#         user_shift = int(input("Enter Shift Key (Integer, e.g., 3): "))
#     except ValueError:
#         print("[Error] Shift key must be an integer. Defaulting to 3.")
#         user_shift = 3

#     # Initialize our system module
#     cipher_system = CaesarCipherEngine(shift=user_shift)

#     print("\n--- Processing Data Flow ---")
    
#     # 2. Process & Output Logic: Encryption
#     encrypted_msg = cipher_system.encrypt(user_message)
#     print(f"Plaintext (Raw Data) : {user_message}")
#     print(f"Ciphertext (Secured) : {encrypted_msg}")
    
#     # 3. Validation Logic: Decryption verification
#     decrypted_msg = cipher_system.decrypt(encrypted_msg)
#     print(f"Decrypted Verification: {decrypted_msg}")
#     print("=======================================")




# Main.code
# ============================================
# Project 2: Basic Encryption & Decryption
# Caesar Cipher | DecodeLabs Cybersecurity
# ============================================

def encrypt(text, shift):
    """Encrypt text using Caesar Cipher."""
    encrypted = ""
    for char in text:
        if char.isupper():
            # Formula: E(x) = (x + n) % 26
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Edge case: spaces, punctuation, numbers -> unchanged
            encrypted += char
    return encrypted


def decrypt(text, shift):
    """Decrypt text using Caesar Cipher (reverse shift)."""
    decrypted = ""
    for char in text:
        if char.isupper():
            # Formula: D(x) = (x - n) % 26
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            # Edge case: spaces, punctuation, numbers -> unchanged
            decrypted += char
    return decrypted


def main():
    print("=" * 50)
    print("   DecodeLabs - Caesar Cipher Tool")
    print("=" * 50)

    # INPUT
    text = input("\nEnter the text to encrypt: ")
    shift = int(input("Enter shift key (1-25): "))

    # PROCESS + OUTPUT
    encrypted_text = encrypt(text, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("\n" + "=" * 50)
    print(f"  Original Text  : {text}")
    print(f"  Shift Key      : {shift}")
    print(f"  Encrypted Text : {encrypted_text}")
    print(f"  Decrypted Text : {decrypted_text}")
    print("=" * 50)

    # Validation check
    if text == decrypted_text:
        print("\n✅ Validation Passed: Decryption matches original!")
    else:
        print("\n❌ Validation Failed: Something went wrong.")


if __name__ == "__main__":
    main()