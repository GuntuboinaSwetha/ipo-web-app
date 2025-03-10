# IPO Web Application
# IPO Web App

## Project Overview

The IPO Web App is a Django-based application that provides users with information related to Initial Public Offerings (IPOs). Users can view details such as company logos, names, price bands, opening and closing dates, issue sizes, and much more.

## Features

- View IPO details, including:
  - Company logo
  - Company name
  - Price band
  - Opening and closing dates
  - Issue size
  - Listing date
  - Current market price (CMP)
  - Downloadable RHP and DRHP PDFs
- User-friendly interface for easy navigation.

## Technologies Used

- Django 5.1.2
- PostgreSQL
- HTML/CSS
- JavaScript
- Git for version control

## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.x
- Git

### 1. Clone the Repository

Open your terminal and run the following command:

```bash
git clone https://github.com/ramuyeligapu3/ipo-web-app.git
```

### 2. Navigate into the Project Directory

Change into the project directory:

```bash
cd ipo-web-app
```

### 3. Create a Virtual Environment

Create a virtual environment named `bluestock`:

Using `virtualenv`:

```bash
pip install virtualenv
virtualenv bluestock
```

Or using Python's built-in `venv`:

```bash
python -m venv bluestock
```

### 4. Activate the Virtual Environment

Activate the virtual environment:

- On **Windows**:

```bash
bluestock\Scripts\activate
```

- On **macOS/Linux**:

```bash
source bluestock/bin/activate
```

### 5. Install Project Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 6. Run Database Migrations (if applicable)

If the project is a Django application, run the following command to set up the database:

```bash
python manage.py migrate
```

### 7. Start the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You can access the application in your web browser at `http://127.0.0.1:8000/`.

### 8. (Optional) Create a Superuser

If you need access to the admin interface, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set your username and password.

By following these steps, you should be able to set up and run the project on your local machine. If you have any questions or encounter issues, feel free to ask for help!
