# parser.py
# Objective: Read sequences from FASTA file and store them into MySQL database

import mysql.connector # can also use sqllite3
from Bio import SeqIO

# Step 1: Connect / Create database
conn = mysql.connector.connect("sequences.db")
cursor = conn.cursor()

# Step 2: Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sequences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seq_id TEXT,
        description TEXT,
        sequence TEXT
    )
''')

# Step 3: Parse FASTA file and insert into database
fasta_file = "sample_data.fasta"   # path to fasta file
for record in SeqIO.parse(fasta_file, "fasta"):
    cursor.execute('''
        INSERT INTO sequences (seq_id, description, sequence)
        VALUES (?, ?, ?)
    ''', (record.id, record.description, str(record.seq)))

# Step 4: Commit and close
conn.commit()
conn.close()

print("FASTA parsing completed and sequences saved in database!")
  
