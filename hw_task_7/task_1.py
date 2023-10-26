import cv2

class FaceDetector:
    def __init__(self, path):
        self.path = path
        self.image = None
        self.video = None

    def preprocess(self):
        if self.path.endswith('.jpg') or self.path.endswith('.png'):
            self.image = cv2.imread(self.path)
        elif self.path.endswith('.mp4') or self.path.endswith('.avi'):
            self.video = cv2.VideoCapture(self.path)

    def detect(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces

    def infer(self):
        faces = self.detect()
        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    def display(self, width=None, height=None):
        if self.image is not None:
            if width or height:
                h, w = self.image.shape[:2]
                if width is None:
                    ratio = height / h
                    dimension = (int(w * ratio), height)
                else:
                    ratio = width / w
                    dimension = (width, int(h * ratio))
                self.image = cv2.resize(self.image, dimension)
            cv2.imshow('image', self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif self.video is not None:
            while True:
                ret, frame = self.video.read()
                if ret:
                    if width and height:
                        frame = cv2.resize(frame, (width, height))
                    cv2.imshow('video', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            self.video.release()
            cv2.destroyAllWindows()

face = FaceDetector('test.jpg')
face.preprocess()
face.infer()
face.display(None, 800)