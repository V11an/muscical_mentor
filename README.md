# TEST HEADING

A simple paragragh

## MY SUBHEADING

Another simple paragragh

![title image](</flaskr/static/back.jpg>)

## ANOTHER SUBHEADING

- List item 1
- list item 2

* List item 3
* List item 4

1. List item 5
2. List item 6


front_end_url = https://deliveroo-front-end.onrender.com/

back_end_url = https://deliveroo-trak.onrender.com


# Deliveroo Project

## Project Overview

**Deliveroo** is a courier service application designed to streamline parcel delivery by allowing users to send parcels to various destinations efficiently. With features for creating delivery orders, modifying them, and viewing delivery details, Deliveroo provides users with an intuitive interface for managing their parcels. Additionally, the service offers real-time updates and visualization through Google Maps integration, ensuring users are always informed about their deliveries.

## Team

- **React (Frontend):**
 1. Chrispine Owino
2. Ted Gitonga

- **Flask (Backend):**

  1.Stacy Njehia

  2.Stella Mutuku

- **Figma Design:**
1. Andrew Langat

## MVP Features

The Minimum Viable Product (MVP) of Deliveroo includes the following features:

1. **User Account Management:**
   - Users can create an account and log in.

2. **Parcel Delivery Order Management:**
   - Users can create a parcel delivery order.
   - Users can change the destination of a parcel delivery order.
   - Users can cancel a parcel delivery order.
   - Users can view the details of a delivery order.

3. **Admin Features:**
   - Admins can change the status of a parcel delivery order.
   - Admins can update the present location of a parcel delivery order.

4. **Google Maps Integration:**
   - The application displays a Google Map with markers indicating the pickup location and the destination.
   - The application shows a line connecting both markers (pickup location and destination).
   - The application computes and displays the travel distance and journey duration between the pickup location and the destination.

## Optional Features

- **Real-Time Notifications:**
  - Users receive real-time email notifications when the Admin changes the status of their parcel.
  - Users receive real-time email notifications when the Admin updates the present location of their parcel.

> **Note:**
>
> - Users can only cancel or change the destination of a parcel delivery order if the parcel’s status has not been marked as delivered.
> - Only the user who created the parcel delivery order can cancel the order.

## Technical Expectations

- **Backend:** Flask
- **Database:** PostgreSQL
- **Wireframes:** Figma (Mobile Friendly)
- **Testing Framework:** Jest (Frontend) & Pytest (Backend)
- **Frontend:** ReactJS & Redux Toolkit (State Management)

## Getting Started

### Prerequisites

To run this project locally, you will need to have the following installed on your system:

- **Node.js** (for the frontend)
- **Python 3.10** (for the backend)
- **PostgreSQL** (for the database)

### Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:Moringa-SDF-PTO5/Deliveroo.git
   cd deliveroo
   ```

2. **Backend Setup:**

   - Navigate to the backend directory:

     ```bash
     cd Deliveroo_backend
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

   - Set up the PostgreSQL database and update the database connection settings in the `config.py` file.

   - Run the Flask development server:

     ```bash
     flask run
     ```

3. **Frontend Setup:**

   - Navigate to the frontend directory:

     ```bash
     cd ../Deliveroo_frontend
     ```

   - Install frontend dependencies:

     ```bash
     npm install
     ```

   - Start the React development server:

     ```bash
     npm start
     ```

4. **Access the Application:**

   - Open your web browser and navigate to `http://localhost:3000` to access the Deliveroo application.

## Testing

### Backend Testing with Pytest

- Navigate to the backend directory:

  ```bash
  cd Deliveroo_backend
  ```

- Run the tests:

  ```bash
  pytest
  ```

### Frontend Testing with Jest

- Navigate to the frontend directory:

  ```bash
  cd Deliveroo_frontend
  ```

- Run the tests:

  ```bash
  npm test
  ```

## Deployment

For deploying our Deliveroo Project we used [Render](render.com). Ensure to configure environment variables and update the production database settings.

## Contributing

We welcome contributions from the community. To contribute to Deliveroo, please follow these steps:

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

5. Open a pull request, describing the changes you made.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Google Maps API](https://developers.google.com/maps)
- [Flask](https://flask.palletsprojects.com/)
- [React](https://reactjs.org/)
- [Redux Toolkit](https://redux-toolkit.js.org/)
- [PostgreSQL](https://www.postgresql.org/)


Special thanks to the team and contributors who made this project possible.


This README provides a comprehensive overview of the Deliveroo project, guiding users through installation, setup, and contribution processes. Feel free to customize it further based on your specific project details and preferences.


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

