-- Create Hospital Table
CREATE TABLE Hospital (
    Hospital_ID CHAR(5) PRIMARY KEY,
    Hospital_Name VARCHAR(50),
    Hospital_Address VARCHAR(50),
    Hospital_Phone_Number VARCHAR(15),
    State CHAR(2),
    Pin_Code CHAR(6)
);

-- Create Department Table
CREATE TABLE Department (
    Department_ID CHAR(4) PRIMARY KEY,
    Department_Name VARCHAR(20),
    Hospital_ID CHAR(5),
    FOREIGN KEY (Hospital_ID) REFERENCES Hospital(Hospital_ID)
);

-- Create Doctor Table
CREATE TABLE Doctor (
    Doctor_ID CHAR(4) PRIMARY KEY,
    Doctor_FName VARCHAR(20),
    Doctor_LName VARCHAR(20),
    Department_ID CHAR(4),
    Doctor_Phone_Number VARCHAR(15),
    FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
);

-- Create Staff Table
CREATE TABLE Staff (
    Staff_ID CHAR(4) PRIMARY KEY,
    Department_ID CHAR(4),
    Staff_FName VARCHAR(20),
    Staff_LName VARCHAR(20),
    Staff_Address VARCHAR(50),
    Staff_Phone_Number VARCHAR(15),
    FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
);

-- Create Patient Table
CREATE TABLE Patient (
    Patient_ID CHAR(4) PRIMARY KEY,
    Patient_FName VARCHAR(20),
    Patient_LName VARCHAR(20),
    Patient_Address VARCHAR(50),
    Patient_Phone_Number VARCHAR(15),
    Pharmacy_ID CHAR(4),
    FOREIGN KEY (Pharmacy_ID) REFERENCES Pharmacy(Pharmacy_ID)
);

-- Create Appointment Table
CREATE TABLE Appointment (
    Patient_ID CHAR(4),
    Doctor_ID CHAR(4),
    Date DATE NOT NULL,
    Time TIME,
    PRIMARY KEY (Patient_ID, Doctor_ID),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
);

-- Create Rooms Table
CREATE TABLE Rooms (
    Room_Num CHAR(4) PRIMARY KEY,
    Patient_ID CHAR(4),
    Staff_ID CHAR(4),
    Admission_Date DATE NOT NULL,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);

-- Create Pharmacy Table
CREATE TABLE Pharmacy (
    Pharmacy_ID CHAR(4) PRIMARY KEY,
    Pharmacy_Name VARCHAR(20),
    Pharmacy_Address VARCHAR(50),
    Pharmacy_Phone_Number VARCHAR(15)
);

-- Create Invoice Table
CREATE TABLE Invoice (
    Invoice_Num CHAR(4) PRIMARY KEY,
    Patient_ID CHAR(4),
    Service_Description VARCHAR(40),
    Cost NUMBER(9, 2),
    Total NUMBER(9, 2),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

-- Create Prescription Table
CREATE TABLE Prescription (
    Prescription_Num CHAR(4) PRIMARY KEY,
    Patient_ID CHAR(4),
    Medication_Name VARCHAR(20),
    Prescription_Date DATE,
    Prescription_Cost NUMBER(9, 2),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);
