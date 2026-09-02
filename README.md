# 🏋️ Workout Tracker

A simple Python-based workout tracking application that uses an exercise/nutrition API to estimate **exercise duration and calories burned** from natural-language input and automatically saves the workout data to a spreadsheet using the Sheety API.

## 🚀 Features

* 🏃 Enter exercises using natural language
* 🔥 Calculates estimated calories burned
* ⏱️ Calculates exercise duration
* 📅 Automatically records the current date and time
* 📊 Stores workout information in a spreadsheet
* 🔐 Uses environment variables to keep API credentials private
* 🌐 Uses REST APIs with Python `requests`

## 🛠️ Technologies Used

* Python
* Requests
* REST API
* Exercise/Nutrition API
* Sheety API
* Google Sheets
* Environment Variables

## 📂 Project Structure

```text
Workout-Tracker/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

## ⚙️ How It Works

1. The program asks the user what exercise they performed.
2. The exercise description is sent to the nutrition/exercise API.
3. The API returns information such as:

   * Exercise name
   * Duration
   * Calories burned
4. The program adds the current date and time.
5. The workout information is sent to a Sheety spreadsheet.

## 💻 Example

```text
Tell me what exercise you did : 30 minutes running

```

The API response is then processed and the workout information is saved with:

* Date
* Time
* Exercise
* Duration
* Calories

## 🔑 Environment Variables

This project requires API credentials.

Create environment variables for:

```text
MY_TOKEN
API_ID
API_KEY
```

Example:

```env
MY_TOKEN=your_bearer_token
API_ID=your_api_id
API_KEY=your_api_key
```

**Never upload your real API keys or tokens to GitHub.**

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Workout-Tracker.git
cd Workout-Tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Set your API credentials:

```text
MY_TOKEN
API_ID
API_KEY
```

### 4. Run the program

```bash
python main.py
```

## 📋 Requirements

The project uses the Python `requests` library.

Install it using:

```bash
pip install requests
```

## 🎯 Learning Objectives

This project helped me practice:

* Python classes and methods
* API requests using `requests`
* POST requests
* JSON data handling
* Environment variables
* Exception handling
* Working with external APIs
* Automating spreadsheet data entry

## 🔮 Future Improvements

* Add a graphical user interface
* Add weekly/monthly workout summaries
* Display total calories burned
* Add user authentication
* Add charts and progress tracking
* Store data in a dedicated database
* Add more detailed workout statistics

## 👨‍💻 Author

**Harit Sharma**

B.Tech Computer Science Engineering Student

---

⭐ If you find this project useful, consider giving it a star!
