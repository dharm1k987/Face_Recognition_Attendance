import face_recognition

def find_encoding(imgs):
    encodings = []
    for img in imgs:
        encode = face_recognition.face_encodings(img)[0]
        encodings.append(encode)
    return encodings

