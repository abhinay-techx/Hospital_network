from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Database connection
def connect_db():
    conn = sqlite3.connect('database/hospital.db')
    return conn

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Register Patient
@app.route('/register_patient', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        data = request.form
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Patient (Patient_ID, Patient_FName, Patient_LName, Patient_Address, Patient_Phone_Number, Pharmacy_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (data['Patient_ID'], data['Patient_FName'], data['Patient_LName'], data['Patient_Address'], data['Patient_Phone_Number'], data['Pharmacy_ID']))
        conn.commit()
        conn.close()
        return render_template('register_patient.html', message="Patient registered successfully!")
    return render_template('register_patient.html')

# Register Doctor
@app.route('/register_doctor', methods=['GET', 'POST'])
def register_doctor():
    if request.method == 'POST':
        data = request.form
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Doctor (Doctor_ID, Doctor_FName, Doctor_LName, Department_ID, Doctor_Phone_Number)
            VALUES (?, ?, ?, ?, ?)
        """, (data['Doctor_ID'], data['Doctor_FName'], data['Doctor_LName'], data['Department_ID'], data['Doctor_Phone_Number']))
        conn.commit()
        conn.close()
        return render_template('register_doctor.html', message="Doctor registered successfully!")
    return render_template('register_doctor.html')

# Register Appointment
@app.route('/register_appointment', methods=['GET', 'POST'])
def register_appointment():
    if request.method == 'POST':
        data = request.form
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Appointment (Patient_ID, Doctor_ID, Date, Time)
            VALUES (?, ?, ?, ?)
        """, (data['Patient_ID'], data['Doctor_ID'], data['Date'], data['Time']))
        conn.commit()
        conn.close()
        return render_template('register_appointment.html', message="Appointment registered successfully!")
    return render_template('register_appointment.html')

# Assign Room
@app.route('/assign_room', methods=['GET', 'POST'])
def assign_room():
    if request.method == 'POST':
        data = request.form
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Rooms (Room_Num, Patient_ID, Staff_ID, Admission_Date)
            VALUES (?, ?, ?, ?)
        """, (data['Room_Num'], data['Patient_ID'], data['Staff_ID'], data['Admission_Date']))
        conn.commit()
        conn.close()
        return render_template('assign_room.html', message="Room assigned to patient!")
    return render_template('assign_room.html')

# Add Prescription
@app.route('/add_prescription', methods=['GET', 'POST'])
def add_prescription():
    if request.method == 'POST':
        data = request.form
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Prescription (Prescription_Num, Patient_ID, Medication_Name, Prescription_Date, Prescription_Cost)
            VALUES (?, ?, ?, ?, ?)
        """, (data['Prescription_Num'], data['Patient_ID'], data['Medication_Name'], data['Prescription_Date'], data['Prescription_Cost']))
        conn.commit()
        conn.close()
        return render_template('add_prescription.html', message="Prescription added successfully!")
    return render_template('add_prescription.html')

# Generate Invoice
@app.route('/generate_invoice', methods=['GET', 'POST'])
def generate_invoice():
    if request.method == 'POST':
        data = request.form
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Invoice (Invoice_Num, Patient_ID, Service_Description, Cost, Total)
            VALUES (?, ?, ?, ?, ?)
        """, (data['Invoice_Num'], data['Patient_ID'], data['Service_Description'], data['Cost'], data['Total']))
        conn.commit()
        conn.close()
        return render_template('generate_invoice.html', message="Invoice generated successfully!")
    return render_template('generate_invoice.html')

# View Patient Details
@app.route('/view_patient', methods=['GET', 'POST'])
def view_patient():
    if request.method == 'POST':
        patient_id = request.form['Patient_ID']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Patient WHERE Patient_ID = ?", (patient_id,))
        patient = cursor.fetchone()
        conn.close()
        if patient:
            return render_template('view_patient.html', patient=patient)
        else:
            return render_template('view_patient.html', error="Patient not found")
    return render_template('view_patient.html')

# View Doctor's Patients
@app.route('/view_doctor_patients', methods=['GET', 'POST'])
def view_doctor_patients():
    if request.method == 'POST':
        doctor_id = request.form['Doctor_ID']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.Patient_ID, p.Patient_FName, p.Patient_LName
            FROM Patient p
            JOIN Appointment a ON p.Patient_ID = a.Patient_ID
            WHERE a.Doctor_ID = ?
        """, (doctor_id,))
        patients = cursor.fetchall()
        conn.close()
        if patients:
            return render_template('view_doctor_patients.html', patients=patients)
        else:
            return render_template('view_doctor_patients.html', error="No patients found for this doctor")
    return render_template('view_doctor_patients.html')

# View Room Availability
@app.route('/room_availability', methods=['GET'])
def room_availability():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Room_Num, CASE 
            WHEN Patient_ID IS NULL THEN 'Available'
            ELSE 'Occupied'
        END AS Status
        FROM Rooms
    """)
    rooms = cursor.fetchall()
    conn.close()
    return render_template('room_availability.html', rooms=rooms)

# View Patient Invoices
@app.route('/view_invoices', methods=['GET', 'POST'])
def view_invoices():
    if request.method == 'POST':
        patient_id = request.form['Patient_ID']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Invoice WHERE Patient_ID = ?", (patient_id,))
        invoices = cursor.fetchall()
        conn.close()
        if invoices:
            return render_template('view_invoices.html', invoices=invoices)
        else:
            return render_template('view_invoices.html', error="No invoices found for this patient")
    return render_template('view_invoices.html')

if __name__ == '__main__':
    app.run(debug=True)
