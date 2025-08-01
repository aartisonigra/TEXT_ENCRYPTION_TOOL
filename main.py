import os
from encryption.aes_tool import encrypt_text_to_file, decrypt_file_to_text

# Create folders if not exist
os.makedirs("notes", exist_ok=True)

print("\n📒 Secure Notes App")
print("1. Create New Encrypted Note")
print("2. View (Decrypt) Existing Note")
choice = input("\nChoose (1 or 2): ").strip()

if choice == "1":
    text = input("✍️ Enter your note: ").strip()
    file_name = input("💾 Save as file (e.g. note1.bin): ").strip()
    path = f"notes/{file_name}"

    key = encrypt_text_to_file(text, path)
    print(f"\n✅ Note encrypted and saved to: {path}")
    print(f"🔑 Save this key to decrypt your note:\n{key.hex()}")

elif choice == "2":
    file_name = input("📂 Enter encrypted file name (e.g. note1.bin): ").strip()
    key_input = input("🔑 Enter decryption key (hex): ").strip()
    path = f"notes/{file_name}"

    try:
        key = bytes.fromhex(key_input)
        note = decrypt_file_to_text(path, key)
        print(f"\n🔓 Decrypted Note:\n{note}")
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
    except ValueError:
        print("❌ Invalid key format! Make sure it's a valid 32-character hex string.")
    except Exception as e:
        print(f"❌ Error decrypting note: {e}")
