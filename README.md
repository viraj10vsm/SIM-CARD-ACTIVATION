# SIM Card Activation Service

This project provides a simple RESTful API for managing the activation, deactivation, and retrieval of SIM card information.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation and Setup](#installation-and-setup)
- [API Endpoints](#api-endpoints)
  - [Activate SIM Card](#activate-sim-card)
  - [Deactivate SIM Card](#deactivate-sim-card)
  - [Get SIM Details](#get-sim-details)
- [Testing the API](#testing-the-api)
  - [Using Postman](#using-postman)
  - [FastAPI Interactive Docs](#fastapi-interactive-docs)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project simulates a telecom company's SIM card management service. It provides the following functionalities:
- Activate a SIM card and record its activation date.
- Deactivate a SIM card.
- Retrieve details of a SIM card by its unique SIM number.

## Tech Stack

- **FastAPI**: Web framework for building APIs quickly and efficiently.
- **MongoDB**: NoSQL database to store SIM card details.
- **Pydantic**: Data validation and parsing based on Python type hints.
- **Uvicorn**: Fast ASGI server to run FastAPI.

## Features

- **SIM Activation**: Activate a SIM card, set its status to `active`, and store the activation date.
- **SIM Deactivation**: Deactivate a SIM card by updating its status to `inactive`.
- **SIM Details**: Fetch the details of a SIM card, including status and phone number.
- **Error Handling**: Handle errors such as invalid SIM numbers or incorrect input formats.

## Folder Structure

```bash
.
├── models
│   └── sim_card.py         # SIM card model for Pydantic validation
├── config
│   └── db.py               # MongoDB connection setup
├── schemas
│   └── sim_card.py         # Schema for SIM card serialization
├── routes
│   └── sim_card.py         # SIM card activation routes
└── main.py                 # Main entry point of the FastAPI app
Installation and Setup
Prerequisites
Python 3.8+
MongoDB (locally installed or hosted on services like MongoDB Atlas)
Virtual environment (using pipenv or virtualenv)
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/sim-card-activation-service.git
cd sim-card-activation-service
Create and activate a virtual environment: Using pipenv:

bash
Copy code
pipenv install
pipenv shell
Or using virtualenv:

bash
Copy code
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure MongoDB connection: Update config/db.py to connect to your MongoDB instance:

python
Copy code
client = MongoClient("mongodb://localhost:27017/")
Run the FastAPI server: Start the FastAPI app using Uvicorn:

bash
Copy code
uvicorn index:app --reload
