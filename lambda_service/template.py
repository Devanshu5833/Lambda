from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify

app = Flask(__name__)

@app.route(%API_URL%,methods = [%METHOD%])
%FUNCTIONDATA%

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug = True)
