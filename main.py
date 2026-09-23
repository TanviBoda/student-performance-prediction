from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Load dataset
data = pd.read_csv("dataset/student_performance_100.csv")

# Input features
X = data[
    [
        "study_hours",
        "attendance",
        "previous_marks",
        "assignment_score",
        "internal_marks"
    ]
]

# Target
y = data["performance"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"request": request}
)


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    study_hours: float = Form(...),
    attendance: float = Form(...),
    previous_marks: float = Form(...),
    assignment_score: float = Form(...),
    internal_marks: float = Form(...)
):

    input_data = [[
        study_hours,
        attendance,
        previous_marks,
        assignment_score,
        internal_marks
    ]]

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Good Performance"
    else:
        result = "Low Performance"

    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "request": request,
        "result": result
    }
)