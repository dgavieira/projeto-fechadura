#exemplo de teste para windows de fingerprint enroll
import sqlite3

def enroll():
    print("Waiting for Finger...")
    temp = int(input("Enter template position: \t"))
    print("Found Template Position at #" + str(temp))
    print("Fingerprint Registered")
    input('hit enter to exit')
    conn = sqlite3.connect('optima.db')
    cursor = conn.cursor()            
    try:
        cursor.execute("""
        ALTER TABLE optima
        ADD COLUMN pos_number INTEGER""")
        print("added new column")
    except:
        print("column already exists")
        pass
    conn.commit()
    cursor.execute("""
        UPDATE optima
        SET pos_number = (?)
        WHERE pos_number IS NULL OR LENGTH(pos_number) = 0
        """,(temp,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    enroll()