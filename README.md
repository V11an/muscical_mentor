
# Musical Mentor

## Project Overview

**Musical Mentor** is a courier service application designed to streamline parcel delivery by allowing users to send parcels to various destinations efficiently. With features for creating delivery orders, modifying them, and viewing delivery details, Deliveroo provides users with an intuitive interface for managing their parcels. Additionally, the service offers real-time updates and visualization through Google Maps integration, ensuring users are always informed about their deliveries.

![title image](</flaskr/static/dashboard.png>)


## MVP Features

The Minimum Viable Product (MVP) of Musical Mentor includes the following features:

1. **User Account Management:**
   - Users can create an account and log in.

2. ** Session Booking:**
   - Students can book a session with a tutor of their choice.

3. **Tutor registering to teach an instrument:**
    - Tutors can register to teach an instrument.


> **Note:**
>
> - Tutors can only approve or deny a session booking by a student

## Technical requirements

- **Backend:** Flask
- **Database:** SQLite3
- **Frontend:** HTML, CSS, JAVASCRIPT, Bootsrap
- **Deployment:** Render.com

## Getting Started

### Prerequisites

To run this project locally, you will need to have the following installed on your system:

- **Python 3.10** (for the backend)
- **SQLite3** (for the database)
- **Flask** 

### Installation


 **Backend Setup:**

   - Navigate to the backend directory:

     ```bash
     cd music_mentor
     ```

   - Create a virtual environment and activate it:

     ```bash  
     virtual venv env
     source venv/bin/activate  
     ```

   - Install backend dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Run the Flask development server:

     ```bash
     flask run
     ```

 **Access the Application:**

   - Open your web browser and navigate to `http://localhost:3000` to access the Deliveroo application.
## Deployment

For deploying our Deliveroo Project we used [Render](render.com). Ensure to configure environment variables and update the production database settings.

## Contributing

We welcome contributions from the community. To contribute to Musical Mentor, please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your message here"
   ```

4. Push your changes to your forked repository:

   ```bash
   git push origin feature/YourFeature
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This README provides a comprehensive overview of the Music Mentor project, guiding users through installation, setup, and contribution processes. Feel free to customize it further based on your specific project details and preferences.


creating flask environment
mkdir myproject
cd myproject (muscical_mentor)
python3 -m venv .venv
. .venv/bin/activate
pip install Flask

Initiating the project
mkdir flaskr
cd flaskr
flaskr/__init__.py
flask --app flaskr run --debug

