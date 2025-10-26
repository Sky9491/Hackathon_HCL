# Hackathon_HCL


Overview
This project is a secure and scalable banking operations management system built using Django, Django REST Framework (DRF), and SQLite/MySQL.

1  User Registration & KYC
      Trigger: Customer signs up
      Flow:
      1. Customer submits personal details (name, email, etc.)
      2. Uploads KYC document (simulated upload)
      3. System validates and stores user profile securely
      4. Admin reviews and approves/rejects KYC



Objectives:
  1. Implement JWT-based authentication
  2. Secure password hashing
  3. Apply input validation and sanitization

Tech Stack:

Backend : 	Django + Django REST Framework
Database :	SQLite /MYSQL
Authentication	: JWT (using djangorestframework-simplejwt)
Frontend	: HTML, CSS (basic forms for interaction)
ORM	: Django ORM
Security :Password hashing, input validation

Features

1. User Registration
      Users provide a username, email, and password.
      Users can upload a KYC document (PDF, image, etc.).
      User data and profile are stored securely in the database.

2. KYC Trigger

      Uploaded KYC document is saved in the system.
      Users can view KYC verification status on their dashboard (Pending/Verified).
3. User Authentication
         Secure login and logout functionality.
         Dashboard access is restricted to logged-in users.

4. Profile Management
      Users can view their profile details, including email and phone number.
      Display of KYC verification status.


URL for access
      1. http://127.0.0.1:8000/accounts/register/
      2. http://127.0.0.1:8000/accounts/login/
      3.  http://127.0.0.1:8000/accounts/dashboard/

      
      


Note:
      Django admin username password
            username:hcl
            password:hcl
      
            
