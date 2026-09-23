# Student Performance Prediction

## 📌 Project Overview

**Student Performance Prediction** is a Machine Learning-based web application that predicts a student's academic performance based on different academic factors.

The application takes student details such as study hours, attendance, previous marks, assignment score, and internal marks as input and predicts whether the student has **Good Performance** or **Low Performance**.

The project uses **Logistic Regression** for classification and **FastAPI** to connect the machine learning model with the web interface.

---

## 🎯 Objective

The main objectives of this project are:

* To predict student academic performance using Machine Learning.
* To analyze important academic factors.
* To classify students into Good Performance or Low Performance.
* To provide a simple web interface for making predictions.
* To demonstrate the use of Machine Learning with a web application.

---

## 🛠️ Technologies Used

| Technology          | Purpose                            |
| ------------------- | ---------------------------------- |
| Python              | Main programming language          |
| Pandas              | Reading and processing the dataset |
| Scikit-learn        | Machine Learning                   |
| Logistic Regression | Performance classification         |
| FastAPI             | Backend and API                    |
| HTML                | Webpage structure                  |
| CSS                 | Webpage styling                    |
| Uvicorn             | Running the FastAPI application    |
| VS Code             | Development environment            |
| CSV                 | Dataset storage                    |

---

## 📊 Dataset

The project uses a dataset containing **100 student records**.

### Dataset Features

| Feature            | Description                   |
| ------------------ | ----------------------------- |
| `student_id`       | Student identification number |
| `study_hours`      | Hours spent studying          |
| `attendance`       | Attendance percentage         |
| `previous_marks`   | Previous academic marks       |
| `assignment_score` | Assignment score              |
| `internal_marks`   | Internal examination marks    |
| `performance`      | Target variable               |

### Target Variable

The `performance` column contains two labels:

* `0` → Low Performance
* `1` → Good Performance

These labels are used by the Machine Learning model to learn the relationship between the input features and student performance.

---

##
