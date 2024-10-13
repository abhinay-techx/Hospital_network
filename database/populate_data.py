import sqlite3
from faker import Faker
import random

# Connect to the SQLite database
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Initialize Faker
fake = Faker()

# Insert data into Hospital table
for _ in range(1000):
    cursor.execute("INSERT INTO Hospital (Hospital_ID, Hospital_Name, Hospital_Address, Hospital_Phone_Number, State, Pin_Code) VALUES (?, ?, ?, ?, ?, ?)", 
                   (fake.unique.random_int(min=10000, max=99999), fake.company(), fake.address(), fake.phone_number(), fake.state_abbr(), fake.zipcode()))

# Insert data into Department table
for _ in range(1000):
    cursor.execute("INSERT INTO Department (Department_ID, Department_Name, Hospital_ID) VALUES (?, ?, ?)", 
                   (fake.unique.random_int(min=1000, max=9999), fake.bs(), fake.random_int(min=10000, max=99999)))

# Insert data into Doctor table
for _ in range(1000):
    cursor.execute("INSERT INTO Doctor (Doctor_ID, Doctor_FName, Doctor_LName, Department_ID, Doctor_Phone_Number) VALUES (?, ?, ?, ?, ?)", 
                   (fake.unique.random_int(min=1000, max=9999), fake.first_name(), fake.last_name(), fake.random_int(min=1000, max=9999), fake.phone_number()))

# Insert data into Staff table
for _ in range(1000):
    cursor.execute("INSERT INTO Staff (Staff_ID, Department_ID, Staff_FName, Staff_LName, Staff_Address, Staff_Phone_Number) VALUES (?, ?, ?, ?, ?, ?)", 
                   (fake.unique.random_int(min=1000, max=9999), fake.random_int(min=1000, max=9999), fake.first_name(), fake.last_name(), fake.address(), fake.phone_number()))

# Insert data into Patient table
for _ in range(1000):
    cursor.execute("INSERT INTO Patient (Patient_ID, Patient_FName, Patient_LName, Patient_Address, Patient_Phone_Number, Pharmacy_ID) VALUES (?, ?, ?, ?, ?, ?)", 
                   (fake.unique.random_int(min=1000, max=9999), fake.first_name(), fake.last_name(), fake.address(), fake.phone_number(), fake.random_int(min=1000, max=9999)))

# Insert data into Pharmacy table
for _ in range(1000):
    cursor.execute("INSERT INTO Pharmacy (Pharmacy_ID, Pharmacy_Name, Pharmacy_Address, Pharmacy_Phone_Number) VALUES (?, ?, ?, ?)", 
                   (fake.unique.random_int(min=1000, max=9999), fake.company(), fake.address(), fake.phone_number()))

# Insert data into Appointment table
for _ in range(1000):
    cursor.execute("INSERT INTO Appointment (Patient_ID, Doctor_ID, Date, Time) VALUES (?, ?, ?, ?)", 
                   (fake.random_int(min=1000, max=9999), fake.random_int(min=1000, max=9999), fake.date(), fake.time()))

# Insert data into Rooms table
for _ in range(1000):
    cursor.execute("INSERT INTO Rooms (Room_Num, Patient_ID, Staff_ID, Admission_Date) VALUES (?, ?, ?, ?)", 
                   (fake.unique.random_int(min=1000, max=9999), fake.random_int(min=1000, max=9999), fake.random_int(min=1000, max=9999), fake.date()))

# Insert data into Invoice table
for _ in range(1000):
    cursor.execute("INSERT INTO Invoice (Invoice_Num, Patient_ID, Service_Description, Cost, Total) VALUES (?, ?, ?, ?, ?)", 
                   (fake.unique.random_int(min=1000, max=9999), fake.random_int(min=1000, max=9999), fake.sentence(nb_words=5), random.uniform(50.00, 500.00), random.uniform(50.00, 500.00)))

# Insert data into Prescription table
for _ in range(1000):
    cursor.execute("INSERT INTO Prescription (Prescription_Num, Patient_ID, Medication_Name, Prescription_Date, Prescription_Cost) VALUES (?, ?, ?, ?, ?)", 
                   (fake.unique.random_int(min=1000, max=9999), fake.random_int(min=1000, max=9999), fake.word(), fake.date(), random.uniform(10.00, 200.00)))

# Commit the changes and close the connection
conn.commit()
conn.close()
