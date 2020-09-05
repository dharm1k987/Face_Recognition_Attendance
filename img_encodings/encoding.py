import face_recognition

def find_encoding(imgs):
    encodings = []
    for img in imgs:
        encode = face_recognition.face_encodings(img)[0]
        encodings.append(encode)
    return encodings

def find_location_and_encoding(img):
    location = face_recognition.face_locations(img)
    encodings = face_recognition.face_encodings(img, location)
    return location, encodings
