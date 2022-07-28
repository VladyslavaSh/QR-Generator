from flask import Flask, render_template, request, redirect
from generate_qr import QrCodeGenerator

qr = QrCodeGenerator()
app = Flask(__name__)


@app.route('/')
def qr_form():
    return render_template("qr.html")


@app.route('/qr', methods=['POST'])
def qrcode():
    data = request.form.get('data')
    path = qr.generate(data)
    return f'<img src="{path}" />'


