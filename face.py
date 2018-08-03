import requests
from json import JSONDecoder
import cv2
import os

def face_recognition(pic1, pic2='./img/img.jpg'):
	'''
	use the API provided by Face++
	'''
	compare_url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
	key = '===========PUT YOUR KEY HERE=========='
	secret = '===========PUT YOUR SECRET HERE========='

	data = {"api_key": key, "api_secret": secret}
	files = {"image_file1": open(pic1,"rb"),"image_file2": open(pic2,"rb")}
	try:
		response = requests.post(compare_url,data=data, files=files)

		req_con = response.content.decode('utf-8')
		req_dict = JSONDecoder().decode(req_con)

		confidence = req_dict['confidence']
	except Exception:
		confidence = 0
	return confidence

def make_photo(path):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("capture",frame)
            
            if cv2.waitKey(1):
                file_name = "capture.jpg"
                file = os.path.join(path, file_name)
                cv2.imwrite(file, frame)
                break
            else:
                break
    
    cap.release()
    cv2.destroyAllWindows()
    return file

def is_same_person(confidence):
	if confidence >= 85.7:
		return True
	else:
		return False