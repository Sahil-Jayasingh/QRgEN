from flask import Flask, request, send_file
import qrcode
import io
app=Flask(__name__)

from flask_cors import CORS #browser gate opening
CORS(app)

@app.route('/generate')
def generate_qr():
    url = request.args.get('url')
    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()
    img_buffer = io.BytesIO()
    img.save(img_buffer)
    img_buffer.seek(0)
    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)