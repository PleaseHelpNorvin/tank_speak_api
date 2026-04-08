
# Project Title

A brief description of what this project does and who it's for

example migrate using alembic:

"$ alembic revision --autogenerate -m "add is_admin to users" alembic upgrade head"

# Tank Speak API

This is the **Tank Speak** FastAPI backend project.

---

## Prerequisites

Make sure you have installed:

- **Python 3.11+**  
- **pip** (Python package manager)  
- **MySQL** (or your preferred SQL database)  
- **Git** (optional, if cloning the repo)  

---

## Setup Guide

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd tank_speak_api
```
### 2. Clone the repository

```bash
python -m venv venv
```

- **Activate the virtual environment:**

  - **Windows (Git Bash / MINGW64):**
  
    ```bash
    source venv/Scripts/activate
    ```

  - **Windows (CMD):**
  
    ```cmd
    venv\Scripts\activate
    ```

  - **Linux / MacOS:**
  
    ```bash
    source venv/bin/activate
    ```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database
##### Create a database on phpmyadmin named : tank_speak

```bash
DATABASE_URL = "mysql+pymysql://username:password@localhost/tank_speak"
```

### 5. run create_tables.py and run seed.py

```bash
python create_tables.py
python seed.py
```

## example migrate using alembic:

```bash
alembic revision --autogenerate -m "add is_admin to users" alembic upgrade head
```