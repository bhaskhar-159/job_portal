# Job_Portal (Django)
#### Welcome!
A full-featured Job Portal Web Application built with Django. This project supports two types of users: Recruiters and Job Seekers. Recruiters can create companies, post jobs, and manage applications, while job seekers can browse jobs, apply online, and track their application status.

## Features of Project

### 1. Authentication

* User Registration
* User Login & Logout
* Role-Based Authentication (Recruiter & Job Seeker)
* Recruiter Dashboard
* Job Seeker Dashboard

### 2. User Profiles

* Recruiter Profile Management
* Job Seeker Profile Management
* Resume & Profile Image Upload

### 3. Company Management

* Create, View, Update, and Delete Companies

### 4. Job Management

* Create, View, Update, and Delete Job Listings
* Browse Available Jobs
* Search Jobs by Title, Company, or Location

### 5. Job Applications

* Apply for Jobs
* Upload Resume & Cover Letter
* Prevent Duplicate Applications
* Track Application Status

### 6. Recruiter Dashboard

* Manage Companies
* Manage Job Listings
* View Applicants
* Review Resumes
* Update Application Status (Pending, Shortlisted, Rejected, Hired)

### 7. Job Seeker Dashboard

* Browse Jobs
* View Job Details
* Manage Profile
* View Applied Jobs
* Track Application Progress

### Technologies Used

* Python 
* Django
* PostgreSQL
* HTML5
* CSS3
* Bootstrap 5 (planned)
* Git & GitHub  

# Installation
### Clone the repository
git clone (https://github.com/bhaskhar-159/job_portal.git)

cd <repository-name>

### Create a virtual environment
python -m venv env

### Activate the virtual environment

### * Windows

env\Scripts\activate

### * macOS / Linux

source env/bin/activate

### Install dependencies
pip install -r requirements.txt
### Apply migrations
python manage.py migrate
### Create a superuser
python manage.py createsuperuser
### Run the development server
python manage.py runserver

### Visit:

http://127.0.0.1:8000/
