from flask import Flask,render_template, Response
import cv2


app=Flask(__name__)
# camera=cv2.VideoCapture("/home/paulson/Documents/sample_vd.mkv")
camera=cv2.VideoCapture(2)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        cv2.waitKey(33)
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=2204, threaded=True)
