from flask import Flask, request, Response
from bll.patients import *
import json

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello, World!"

@app.route("/patients", methods = ['GET'])
def patients():
    if request.method=="GET":
        patients = get_patients()
        return Response(json.dumps(
            patients
        ),
            status=200,
            mimetype='application/json')

@app.route("/patient/<subject_id>", methods = ['GET'])
def patient_data(subject_id):
    if request.method=="GET":
        patients = get_patient(subject_id=subject_id)
        return Response(
            json.dumps(
                patients),
            status=200,
            mimetype='application/json')