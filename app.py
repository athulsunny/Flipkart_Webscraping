from flask import Flask,request,render_template,jsonify
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from flask_cors import CORS,cross_origin

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__==__main__:
    app.run()