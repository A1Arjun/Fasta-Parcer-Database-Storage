# Objective: Test whether sequences are correctly inserted into database

import mysql.connector
import os
import subprocess

def test_parser():
    # Step 1: Remove old database if exists
    if os.path.exists("sequences.db"):
        os.remove("sequences.db")

    # Step 2: Run parser.py
    subprocess.run(["python", "parser.py"], check=True)

    # Step 3: Connect to new database
    conn = mysql.connector.connect("sequences.db")
    cursor = conn.cursor()

    # Step 4: Check if sequences are inserted
    cursor.execute("SELECT COUNT(*) FROM sequences")
    count = cursor.fetchone()[0]

    assert count > 0, "No sequences inserted into database!"

    conn.close()
    print("✅ Test passed: Sequences successfully inserted.")

if __name__ == "__main__":
    test_parser()
  
