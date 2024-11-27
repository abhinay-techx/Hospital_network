
# Hospital Management System

A comprehensive Hospital Management System built using **Flask** and **SQLite**, designed to streamline the management of patients, doctors, appointments, rooms, and more.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Features](#features)
- [How to Use](#how-to-use)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

---

## Project Structure

```plaintext
hospital-management/
├── __pycache__/
├── app.py
├── database/
│   ├── create_tables.sql
│   └── populate_data.py
├── requirements.txt
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

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hospital-management.git
   cd hospital-management
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database:**
   - **Create database tables:**
     ```bash
     sqlite3 database/hospital.db < database/create_tables.sql
     ```
   - **Populate initial data:**
     ```bash
     python database/populate_data.py
     ```

6. **Run the application:**
   ```bash
   python app.py
   ```

7. **Access the application in your browser:**
   ```
   http://127.0.0.1:5000/
   ```

---

## Features

- **Homepage:** A dashboard summarizing the hospital's activities.
- **Patient Management:** Register and view patient details.
- **Doctor Management:** Add and manage doctors.
- **Appointment Scheduling:** Book and manage appointments.
- **Prescription Management:** Add and manage prescriptions.
- **Room Assignment:** Assign rooms to patients and check availability.
- **Invoice Management:** Generate and view invoices.
- **Doctor-Patient View:** Track which patients are under which doctor.

---

## How to Use

1. Launch the application as outlined in the setup instructions.
2. Use the main dashboard to navigate through the system's features.
3. Add data (patients, doctors, appointments, etc.) using the respective forms.
4. Check and update information directly from the interface.
5. Use the room availability and invoice generation tools for advanced management.

---

## Contribution Guidelines

We welcome contributions to make this project even better! Here's how you can help:

1. **Fork the repository** on GitHub.
2. **Clone your forked repository** locally:
   ```bash
   git clone https://github.com/yourusername/hospital-management.git
   ```
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them:
   ```bash
   git commit -m "Describe your changes"
   ```
5. Push your branch to GitHub:
   ```bash
   git push origin feature-name
   ```
6. Open a Pull Request for review.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Happy coding! If you have any issues, feel free to open a GitHub Issue or contact the maintainers.
