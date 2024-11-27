# Hospital Management System

This is a simple Hospital Management System built using Flask and SQLite. The application allows you to manage patients, doctors, appointments, and more.

## Project Structure


hospital-management/
├── __pycache__/
├── 

app.py


├── database/
│   ├── create_tables.sql
│   └── populate_data.py
├── 

requirements.txt


├── static/
│   └── style.css
├── templates/
│   ├── add_prescription.html
│   ├── assign_room.html
│   ├── generate_invoice.html
│   ├── index.html
│   ├── register_appointment.html
│   ├── register_doctor.html
│   ├── register_patient.html
│   ├── room_availability.html
│   ├── view_doctor_patients.html
│   ├── view_invoices.html
│   └── view_patient.html
└── venv/
    ├── Include/
    ├── Lib/
    ├── Scripts/
    └── pyvenv.cfg
```

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/hospital-management.git
   cd hospital-management
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Set up the database:**
   - Create the database tables:
     ```sh
     sqlite3 database/hospital.db < database/create_tables.sql
     ```
   - Populate the database with initial data:
     ```sh
     python database/populate_data.py
     ```

6. **Run the application:**
   ```sh
   python app.py
   ```

7. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000/
   ```

## Features

- **Homepage:** View the main dashboard.
- **Register Patient:** Add new patients to the system.
- **Register Doctor:** Add new doctors to the system.
- **Register Appointment:** Schedule appointments for patients.
- **Add Prescription:** Add prescriptions for patients.
- **Assign Room:** Assign rooms to patients.
- **View Invoices:** Generate and view invoices.
- **Room Availability:** Check room availability.
- **View Doctor's Patients:** View patients assigned to a specific doctor.
- **View Patient:** View detailed information about a patient.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```