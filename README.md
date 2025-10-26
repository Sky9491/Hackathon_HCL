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


## Project Plan — Sprint Breakdown  ## 


Sprint 1: Project Setup & Environment

  Goal: Create and configure a Django + DRF project environment
    Deliverables:
      Django project structure
      Virtual environment setup
      Installed dependencies
      Database setup (SQLite initially)
      Git repo initialized

Sprint 2: User & Profile Models
  Goal: Create the User and Profile models with a one-to-one relationship
  Deliverables:
    accounts app
    Profile model linked to Django User
    Admin registration
    Database migrations

Sprint 3: Secure User Registration

Goal: Implement user registration with validation and password hashing
  Deliverables:
    RegisterView API
    Strong password validation
    Unique username/email enforcement
    On registration → create empty Profile

Sprint 4: KYC Upload System
  
  Goal: Enable users to upload simulated KYC documents
    Deliverables:
      KYC model + upload path (media/kyc_docs/)
      File upload endpoint/form
      KYC status field: Pending / Approved / Rejected
      Admin panel to view and update status

Sprint 5: JWT Authentication

  Goal: Secure the system using JWT (via SimpleJWT)
    Deliverables:
      /api/token/ and /api/token/refresh/ endpoints
      Login using username/email + password
      Auth-protected routes

Sprint 6: Security & Validation

  Goal: Apply final security hardening
    Deliverables:
      Password hashing (built-in Django)
      Input sanitization & validation
      Permissions (e.g., only admin can approve KYC)
      CSRF & CORS setup (if needed for frontend)

Sprint 7: Frontend (Basic Forms)
  
  Goal: Build simple HTML forms for registration, login, and KYC upload
  Deliverables:
    Templates with Bootstrap/CSS
    User-friendly interactions
    Success/failure messages






Note :
 Django admin login :
   username : hcl
   password : hcl
