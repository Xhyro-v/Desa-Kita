
# DesaKita - Semi Social Media for Villagers

A simple FastAPI web application designed to help village residents access information and announcements provided by the village head, secretariat, and village moderators.


## Roles

### 1. Admin / Moderator
**For:** Village officials such as village heads and secretariat staff.  
**Can do:**  
- Provide information or news  
- Post announcements for village residents  

### 2. Users
**For:** Village residents  
**Can do:**  
- View announcements and news  
- Participate in elections (polls)  
- Join discussions with other residents  


## Tech Stack
 
This project is built using a minimal Python web stack focused on learning backend fundamentals.
 
 
- **Python** – main programming language
 
- **FastAPI** – backend web framework used for routing and API development
 
- **Jinja2** – template engine for rendering dynamic HTML pages
 
- **Uvicorn** – ASGI server used to run the FastAPI application
 

 
## Project Structure
 `DesaKita/ │ ├── main.py │   Main FastAPI application containing routes and core logic │ ├── templates/ │   HTML templates rendered using Jinja2 │ ├── static/ │   Static files such as CSS and images │ ├── requirements.txt │   Python dependencies required to run the project │ └── README.md     Project documentation ` 
## Installation
 
Clone the repository:
 `git clone https://github.com/Xhyro-v/Desa-Kita.git cd Desa-Kita ` 
Install dependencies:
 `pip install -r requirements.txt ` 
## Run the Application
 
Start the development server:
 `uvicorn main:app --reload ` 
Open your browser and go to:
 `http://127.0.0.1:8000 ` 
## Screenshots
 
### Home Page
 
Homepage 
 
### Announcement Page
 
Announcement Page