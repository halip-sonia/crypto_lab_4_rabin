import sys
import key_generation
import encryption
import decryption

def main():
    # variables to hold the keys
    p = None
    q = None
    n = None
    
    # variable to remember the last message for validation purposes
    last_plaintext = None

    print("--- Rabin Cryptosystem Lab ---")

    while True:
        print("\nMenu:")
        print("1. Generate Keys")
        print("2. Encrypt Message")
        print("3. Decrypt Ciphertext")
        print("4. Exit")
        
        choice = input("Select an option: ").strip()

        if choice == '1':
            print("\nGenerating keys (512-bit)...")
            try:
                p, q = key_generation.generate_private_key(bit_length=512)
                n = key_generation.generate_public_key(p, q)
                print(f"Keys generated successfully!")
                print(f"Public Key (n): {n}")
                print(f"Private Key (p): {p}")
                print(f"Private Key (q): {q}")
            except Exception as e:
                print(f"Error generating keys: {e}")

        elif choice == '2':
            if n is None:
                print("\n[!] Error: Please generate keys first (Option 1).")
                continue
            
            plaintext = input("\nEnter plaintext (Space and A-Z only): ")
            
            # store the plaintext (uppercase)
            last_plaintext = plaintext.upper()
            
            try:
                c = encryption.encrypt(plaintext, n)
                print(f"Ciphertext: {c}")
            except ValueError as e:
                print(f"[!] Validation Error: {e}")

        elif choice == '3':
            if p is None or q is None:
                print("\n[!] Error: Private keys (p, q) are missing. Generate keys first.")
                continue
            
            cipher_input = input("\nEnter ciphertext (integer): ").strip()
            if not cipher_input.isdigit():
                print("[!] Error: Ciphertext must be a positive integer.")
                continue
            
            c = int(cipher_input)
            
            print("Decrypting...")
            # rabin decryption returns 4 roots
            roots = decryption.decrypt(c, p, q, n)
            
            print("\nPossible plaintexts (Rabin produces 4 results):")
            print("-" * 40)
            
            match_found = False
            
            for i, root in enumerate(roots):
                try:
                    # convert the integer root back to text
                    decoded_text = encryption.int_to_text(root)
                    
                    # does this result match what we encrypted earlier?
                    if last_plaintext is not None and decoded_text == last_plaintext:
                        print(f"Option {i+1}: {decoded_text}   <-- [CORRECT MATCH]")
                        match_found = True
                    else:
                        print(f"Option {i+1}: {decoded_text}")
                        
                except Exception:
                    # if conversion fails show raw number
                    print(f"Option {i+1}: [Raw Value] {root}")
            print("-" * 40)
            
            if match_found:
                print("Success: The system identified the correct message based on your previous input.")
            elif last_plaintext is None:
                print("Note: No message was encrypted in this session yet, so automatic verification is skipped.")
            else:
                print("Note: None of the decrypted options matched the last encrypted message.")

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(10000)
    main()