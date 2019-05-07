from Detection.MtcnnDetector import MtcnnDetector
from Detection.detector import Detector
from Detection.fcn_detector import FcnDetector
from models.mtcnn_model import P_Net, R_Net, O_Net

mtcnn_detector=None

def initGlobalDetetor():
    global mtcnn_detector
    if mtcnn_detector==None:
        thresh = [0.6, 0.7, 0.7]
        min_face_size = 20
        stride = 2
        slide_window = False

        batch_size = [2048, 64, 16]
        epoch = [18, 14, 16]
        prefix = ['./ckpt/PNet_landmark/PNet', './ckpt/RNet_landmark/RNet', './ckpt/ONet_landmark/ONet']
        model_path = ['%s-%s' % (x, y) for x, y in zip(prefix, epoch)]

        detectors=[
            FcnDetector(P_Net, model_path[0]),
            Detector(R_Net, 24, batch_size[1], model_path[1]),
            Detector(O_Net, 48, batch_size[2], model_path[2]),
        ]
        mtcnn_detector = MtcnnDetector(detectors=detectors, min_face_size=min_face_size,
                                       stride=stride, threshold=thresh, slide_window=slide_window)

def getDefualtDetector():
    global mtcnn_detector
    if mtcnn_detector==None:
        initGlobalDetetor()

    return mtcnn_detector