#exemplo de teste para windows de fingerprint enroll

def main():
    print("Waiting for Finger...")
    temp = int(input("Enter template position"))
    print("Found Template Position at #" + str(temp))
    print("Fingerprint Registered")

if __name__ == "__main__":
    main()