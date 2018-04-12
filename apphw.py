import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurements

session = Session(engine)


app = Flask(__name__)


@app.route("/")
def welcome():
    """The routes for the Analysis."""
   
   
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return list of precipitation data """ 
    last_year_precipitation = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>'2016-12-31'.\
    order_by(Measurement.date).all()

    precip_list = np.ravel(last_year_precipitation)


    return jsonify(precip_list)

@app.route("/api/v1.0/tobs")
def tobs():
    last_year=session.query(Measurement.tobs,func.count(Measurement.tobs)).filter(Measurement.date > '2016-12-31').\
    filter(Measurement.station == "USC00519281").group_by(Measurement.tobs).order_by(Measurement.date).all()

    tobs_list= np.ravel(last_year)
    return jsonify(tobs_list)

Station=Base.classes.stations
session=Session(engine)
@app.route("/api/v1.0/stations")
def stations():
    """Return list of stations"""
   results = session.query(func.count(Station.station)).all()

    new_list= np.ravel(results)

    return jsonify(new_list)

@app.route("/api/v1.0/<start>")
def start():
    #the query
    #use calc temps function for the range of dates
    #jsonify


if __name__ == '__main__':
    app.run(debug=True)
