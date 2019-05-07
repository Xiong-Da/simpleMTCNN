import Detection.detectorFactory as detectorFactory

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import io
import base64
import cv2
import numpy as np

host = ('localhost', 80)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps("plase use post").encode())

    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length']))
        imgbyte=base64.decodebytes(datas)
        image = cv2.imdecode(np.fromstring(imgbyte, dtype='uint8'),cv2.IMREAD_UNCHANGED)
        # cv2.imshow("test", image)
        # cv2.waitKey(0)

        all_boxes, landmarks = detectorFactory.getDefualtDetector().detect_single_image(image)

        print("\n" + "*" * 20)
        print(all_boxes)
        print(landmarks)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"boxes":all_boxes.tolist(),"landmarks":landmarks.tolist()}).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()