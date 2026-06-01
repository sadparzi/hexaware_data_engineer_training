CREATE DATABASE hospital_capstonedb;
USE hospital_capstonedb;

CREATE TABLE patients
(
patient_id INT PRIMARY KEY,
patient_name VARCHAR(100),
gender VARCHAR(10),
age INT,
city VARCHAR(50),
phone VARCHAR(15)
);

CREATE TABLE departments
(
department_id INT PRIMARY KEY,
department_name VARCHAR(100)
);

CREATE TABLE doctors
(
doctor_id INT PRIMARY KEY,
doctor_name VARCHAR(100),
specialization VARCHAR(100),
department_id INT,
consultation_fee DECIMAL(10,2)
);

CREATE TABLE appointments
(
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
appointment_status VARCHAR(30)
);

CREATE TABLE treatments
(
treatment_id INT PRIMARY KEY,
appointment_id INT,
treatment_name VARCHAR(100),
treatment_cost DECIMAL(10,2)
);

CREATE TABLE bills
(
bill_id INT PRIMARY KEY,
patient_id INT,
appointment_id INT,
bill_date DATE,
total_amount DECIMAL(10,2),
bill_status VARCHAR(30)
);

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
bill_id INT,
payment_mode VARCHAR(30),
paid_amount DECIMAL(10,2),
payment_status VARCHAR(30)
);

INSERT INTO departments VALUES
(1,'Cardiology'),
(2,'Neurology'),
(3,'Orthopedics'),
(4,'Pediatrics'),
(5,'General Medicine');

INSERT INTO patients VALUES
(101,'Rahul Sharma','Male',35,'Hyderabad','9876543210'),
(102,'Priya Reddy','Female',29,'Hyderabad','9876543211'),
(103,'Amit Kumar','Male',42,'Bangalore','9876543212'),
(104,'Sneha Patel','Female',38,'Mumbai','9876543213'),
(105,'Arjun Verma','Male',50,'Delhi','9876543214'),
(106,'Meera Singh','Female',31,'Chennai','9876543215'),
(107,'Farhan Ali','Male',27,'Pune','9876543216'),
(108,'Divya Nair','Female',45,'Kochi','9876543217'),
(109,'Kiran Rao','Male',55,'Hyderabad','9876543218'),
(110,'Neha Gupta','Female',33,'Bangalore','9876543219'),
(111,'Ramesh Kumar','Male',40,'Chennai','9876543220'),
(112,'Ayesha Khan','Female',37,'Hyderabad','9876543221');

INSERT INTO doctors VALUES
(201,'Dr. Anil Kumar','Cardiologist',1,1200),
(202,'Dr. Priya Menon','Neurologist',2,1500),
(203,'Dr. Rajesh Singh','Orthopedic',3,1000),
(204,'Dr. Kavya Rao','Pediatrician',4,800),
(205,'Dr. Ahmed Ali','General Physician',5,700),
(206,'Dr. Sneha Iyer','Cardiologist',1,1300),
(207,'Dr. Vikram Shah','Neurologist',2,1400),
(208,'Dr. Meera Patel','Orthopedic',3,1100);

INSERT INTO appointments VALUES
(301,101,201,'2026-01-05','Completed'),
(302,102,202,'2026-01-06','Completed'),
(303,103,203,'2026-01-08','Completed'),
(304,104,204,'2026-01-10','Cancelled'),
(305,105,205,'2026-01-12','Completed'),
(306,106,206,'2026-01-15','Completed'),
(307,107,207,'2026-01-18','Pending'),
(308,108,208,'2026-01-20','Completed'),
(309,109,201,'2026-01-22','Completed'),
(310,110,202,'2026-01-25','Pending'),
(311,111,203,'2026-01-28','Completed'),
(312,112,204,'2026-02-01','Completed'),
(313,101,205,'2026-02-03','Completed'),
(314,102,206,'2026-02-05','Pending'),
(315,103,207,'2026-02-08','Completed'),
(316,104,208,'2026-02-10','Completed'),
(317,105,201,'2026-02-12','Completed'),
(318,106,202,'2026-02-15','Cancelled'),
(319,107,203,'2026-02-18','Pending'),
(320,108,204,'2026-02-20','Completed');

INSERT INTO treatments VALUES
(401,301,'ECG',1500),
(402,302,'Brain Scan',4000),
(403,303,'Fracture Care',3500),
(404,305,'General Checkup',1000),
(405,306,'Heart Screening',5000),
(406,308,'Joint Therapy',4500),
(407,309,'Angiogram',8000),
(408,311,'Bone Scan',3000),
(409,312,'Vaccination',1200),
(410,313,'Blood Test',800),
(411,315,'Neurology Consultation',3500),
(412,316,'Physiotherapy',2500),
(413,317,'ECG',1500),
(414,320,'Child Checkup',1000),
(415,310,'MRI Scan',6000);

INSERT INTO bills VALUES
(501,101,301,'2026-01-05',2700,'Paid'),
(502,102,302,'2026-01-06',5500,'Paid'),
(503,103,303,'2026-01-08',4500,'Paid'),
(504,105,305,'2026-01-12',1700,'Paid'),
(505,106,306,'2026-01-15',6300,'Paid'),
(506,108,308,'2026-01-20',5600,'Paid'),
(507,109,309,'2026-01-22',9200,'Paid'),
(508,111,311,'2026-01-28',4100,'Paid'),
(509,112,312,'2026-02-01',2000,'Paid'),
(510,101,313,'2026-02-03',1500,'Paid'),
(511,103,315,'2026-02-08',4900,'Paid'),
(512,104,316,'2026-02-10',3600,'Paid'),
(513,105,317,'2026-02-12',2700,'Paid'),
(514,110,310,'2026-01-25',7400,'Pending'),
(515,108,320,'2026-02-20',1800,'Pending');

INSERT INTO payments VALUES
(601,501,'UPI',2700,'Success'),
(602,502,'Card',5500,'Success'),
(603,503,'Cash',4500,'Success'),
(604,504,'UPI',1700,'Success'),
(605,505,'Card',6300,'Success'),
(606,506,'UPI',5600,'Success'),
(607,507,'Net Banking',9200,'Success'),
(608,508,'Cash',4100,'Success'),
(609,509,'UPI',2000,'Success'),
(610,510,'Card',1500,'Success'),
(611,511,'UPI',4900,'Success'),
(612,512,'Cash',3600,'Success'),
(613,513,'Net Banking',2700,'Success'),
(614,514,'UPI',0,'Pending'),
(615,515,'Card',NULL,'Pending');

-- Query 1
SELECT *
FROM patients;

-- Query 2
SELECT *
FROM doctors;

-- Query 3
SELECT *
FROM patients
WHERE city = 'Hyderabad';

-- Query 4
SELECT d.*
FROM doctors d
INNER JOIN departments dept
ON d.department_id = dept.department_id
WHERE dept.department_name = 'Cardiology';

-- Query 5
SELECT *
FROM appointments
WHERE appointment_date > '2026-01-01';

-- Query 6
SELECT *
FROM appointments
WHERE appointment_status = 'Cancelled';

-- Query 7
SELECT *
FROM bills
WHERE total_amount > 5000;

-- Query 8
SELECT *
FROM payments
WHERE payment_mode = 'UPI';

-- Query 9
SELECT *
FROM patients
WHERE age BETWEEN 30 AND 50;

-- Query 10
SELECT *
FROM doctors
WHERE consultation_fee > 800;

-- Query 11
SELECT COUNT(*) AS TotalPatients
FROM patients;

-- Query 12
SELECT COUNT(*) AS TotalDoctors
FROM doctors;

-- Query 13
SELECT COUNT(*) AS TotalAppointments
FROM appointments;

-- Query 14
SELECT AVG(consultation_fee) AS AverageConsultationFee
FROM doctors;

-- Query 15
SELECT MAX(treatment_cost) AS HighestTreatmentCost
FROM treatments;

-- Query 16
SELECT SUM(total_amount) AS TotalBillingAmount
FROM bills;

-- Query 17
SELECT SUM(paid_amount) AS TotalPaidAmount
FROM payments;

-- Query 18
SELECT
    city,
    COUNT(*) AS PatientCount
FROM patients
GROUP BY city;

-- Query 19
SELECT
    specialization,
    COUNT(*) AS DoctorCount
FROM doctors
GROUP BY specialization;

-- Query 20
SELECT
    appointment_status,
    COUNT(*) AS AppointmentCount
FROM appointments
GROUP BY appointment_status;

-- Query 21
SELECT
    p.patient_name,
    a.appointment_date,
    a.appointment_status
FROM patients p
INNER JOIN appointments a
ON p.patient_id = a.patient_id;

-- Query 22
SELECT
    d.doctor_name,
    dept.department_name
FROM doctors d
INNER JOIN departments dept
ON d.department_id = dept.department_id;

-- Query 23
SELECT
    p.patient_name,
    d.doctor_name,
    a.appointment_date
FROM appointments a
INNER JOIN patients p
ON a.patient_id = p.patient_id
INNER JOIN doctors d
ON a.doctor_id = d.doctor_id;

-- Query 24
SELECT
    a.appointment_id,
    t.treatment_name,
    t.treatment_cost
FROM appointments a
INNER JOIN treatments t
ON a.appointment_id = t.appointment_id;

-- Query 25
SELECT
    b.bill_id,
    p.patient_name,
    b.total_amount
FROM bills b
INNER JOIN patients p
ON b.patient_id = p.patient_id;

-- Query 26
SELECT
    b.bill_id,
    p.payment_mode,
    p.paid_amount,
    p.payment_status
FROM bills b
INNER JOIN payments p
ON b.bill_id = p.bill_id;

-- Query 27
SELECT
    p.patient_name,
    d.doctor_name,
    dept.department_name,
    a.appointment_date,
    a.appointment_status,
    t.treatment_name,
    t.treatment_cost,
    b.total_amount,
    pay.payment_status
FROM appointments a
INNER JOIN patients p
ON a.patient_id = p.patient_id
INNER JOIN doctors d
ON a.doctor_id = d.doctor_id
INNER JOIN departments dept
ON d.department_id = dept.department_id
LEFT JOIN treatments t
ON a.appointment_id = t.appointment_id
LEFT JOIN bills b
ON a.appointment_id = b.appointment_id
LEFT JOIN payments pay
ON b.bill_id = pay.bill_id;

-- Query 28
SELECT
    d.doctor_name,
    COUNT(*) AS AppointmentCount
FROM doctors d
INNER JOIN appointments a
ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_name;

-- Query 29
SELECT
    dept.department_name,
    COUNT(*) AS AppointmentCount
FROM departments dept
INNER JOIN doctors d
ON dept.department_id = d.department_id
INNER JOIN appointments a
ON d.doctor_id = a.doctor_id
GROUP BY dept.department_name;

-- Query 30
SELECT
    dept.department_name,
    SUM(b.total_amount) AS Revenue
FROM departments dept
INNER JOIN doctors d
ON dept.department_id = d.department_id
INNER JOIN appointments a
ON d.doctor_id = a.doctor_id
INNER JOIN bills b
ON a.appointment_id = b.appointment_id
GROUP BY dept.department_name;

-- Query 31
SELECT
    treatment_name,
    SUM(treatment_cost) AS TotalTreatmentCost
FROM treatments
GROUP BY treatment_name;

-- Query 32
SELECT
    p.city,
    SUM(b.total_amount) AS TotalBilling
FROM patients p
INNER JOIN bills b
ON p.patient_id = b.patient_id
GROUP BY p.city;

-- Query 33
SELECT
    d.doctor_name,
    COUNT(*) AS AppointmentCount
FROM doctors d
INNER JOIN appointments a
ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_name
HAVING COUNT(*) > 2;

-- Query 34
SELECT
    dept.department_name,
    SUM(b.total_amount) AS Revenue
FROM departments dept
INNER JOIN doctors d
ON dept.department_id = d.department_id
INNER JOIN appointments a
ON d.doctor_id = a.doctor_id
INNER JOIN bills b
ON a.appointment_id = b.appointment_id
GROUP BY dept.department_name
HAVING SUM(b.total_amount) > 20000;

-- Query 35
SELECT
    city,
    COUNT(*) AS PatientCount
FROM patients
GROUP BY city
HAVING COUNT(*) > 2;

-- Query 36
SELECT *
FROM patients
WHERE patient_id IN
(
    SELECT patient_id
    FROM appointments
);

-- Query 37
SELECT *
FROM patients
WHERE patient_id NOT IN
(
    SELECT patient_id
    FROM appointments
);

-- Query 38
SELECT *
FROM doctors
WHERE doctor_id NOT IN
(
    SELECT doctor_id
    FROM appointments
);

-- Query 39
SELECT *
FROM bills
WHERE total_amount >
(
    SELECT AVG(total_amount)
    FROM bills
);

-- Query 40
SELECT DISTINCT
    p.patient_id,
    p.patient_name
FROM patients p
INNER JOIN bills b
ON p.patient_id = b.patient_id
WHERE b.total_amount =
(
    SELECT MAX(total_amount)
    FROM bills
);

-- Query 41
SELECT *
FROM doctors
WHERE consultation_fee >
(
    SELECT AVG(consultation_fee)
    FROM doctors
);

-- Query 42
SELECT DISTINCT
    p.patient_id,
    p.patient_name
FROM patients p
INNER JOIN appointments a
ON p.patient_id = a.patient_id
INNER JOIN doctors d
ON a.doctor_id = d.doctor_id
INNER JOIN departments dept
ON d.department_id = dept.department_id
WHERE dept.department_name = 'Cardiology';

-- Query 43
SELECT *
FROM bills
WHERE bill_status <> 'Paid';

-- Query 44
SELECT *
FROM appointments
WHERE appointment_id IN
(
    SELECT appointment_id
    FROM treatments
);

-- Query 45
SELECT
    p.patient_id,
    p.patient_name,
    SUM(b.total_amount) AS TotalBilling
FROM patients p
INNER JOIN bills b
ON p.patient_id = b.patient_id
GROUP BY p.patient_id, p.patient_name
HAVING SUM(b.total_amount) >
(
    SELECT AVG(PatientTotal)
    FROM
    (
        SELECT SUM(total_amount) AS PatientTotal
        FROM bills
        GROUP BY patient_id
    ) AS AvgTable
);

-- Query 46
SELECT a.*
FROM appointments a
LEFT JOIN treatments t
ON a.appointment_id = t.appointment_id
WHERE t.appointment_id IS NULL;

-- Query 47
SELECT b.*
FROM bills b
LEFT JOIN payments p
ON b.bill_id = p.bill_id
WHERE p.bill_id IS NULL;

-- Query 48
SELECT *
FROM payments
WHERE paid_amount IS NULL
OR paid_amount = 0;

-- Query 49
SELECT
    a.appointment_id,
    a.appointment_status,
    b.bill_id
FROM appointments a
INNER JOIN bills b
ON a.appointment_id = b.appointment_id
WHERE a.appointment_status = 'Cancelled';

-- Query 50
SELECT
    b.bill_id,
    b.total_amount,
    p.paid_amount
FROM bills b
INNER JOIN payments p
ON b.bill_id = p.bill_id
WHERE p.payment_status = 'Success'
AND p.paid_amount < b.total_amount;

-- Query 51
SELECT d.*
FROM doctors d
LEFT JOIN departments dept
ON d.department_id = dept.department_id
WHERE dept.department_id IS NULL;

-- Query 52
SELECT a.*
FROM appointments a
LEFT JOIN patients p
ON a.patient_id = p.patient_id
LEFT JOIN doctors d
ON a.doctor_id = d.doctor_id
WHERE p.patient_id IS NULL
OR d.doctor_id IS NULL;