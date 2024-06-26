from flask import Flask, request, Response
from bll.patients import *
from bll.home_analytics import *
import json

app = Flask(__name__)


@app.route("/healthcheck")
def home():
    return "OK"


@app.route("/patients", methods=['GET'])
def patients():
    if request.method == "GET":
        patients = get_patients()
        return Response(json.dumps(
            patients
        ),
            status=200,
            mimetype='application/json')


@app.route("/high_freq_patients", methods=['GET'])
def freq_patients():
    if request.method == "GET":
        patients = get_freq_patients()
        return Response(json.dumps(
            patients
        ),
            status=200,
            mimetype='application/json')


@app.route("/patient/<subject_id>", methods=['GET'])
def patient_data(subject_id):
    if request.method == "GET":
        patients = get_patient(subject_id=subject_id)
        return Response(
            json.dumps(
                patients),
            status=200,
            mimetype='application/json')


@app.route("/home/mortality_stats", methods=["GET"])
def mortality_stats():
    if request.method == "GET":
        data = get_mortality_stats()
        return Response(
            json.dumps(
                data),
            status=200,
            mimetype='application/json')


@app.route("/home/admission_reason_stats", methods=["GET"])
def admission_reason_stats():
    if request.method == "GET":
        data = get_admission_reason_data()
        return Response(
            json.dumps(
                data),
            status=200,
            mimetype='application/json')


@app.route("/patient/stats/<subject_id>", methods=["GET"])
def patient_stats(subject_id):
    if request.method == "GET":
        data = get_patients_stats(subject_id=subject_id)
        return Response(
            json.dumps(
                data),
            status=200,
            mimetype='application/json')
