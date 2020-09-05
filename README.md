# Face Recognition Attendance

This program serves as a way to track student attendance via a webcam. There is a folder which stores student images with
their names, and is used as a way to detect students. Students will walk past the camera, and the program will mark them
as present and update a csv file: `attendance.csv`.

Demonstration: [YouTube Video](https://www.youtube.com/watch?v=wVKdivm72tg)

<img src="screens/dj.png"> 

img src="screens/csv.png"> 

Tested using `Python 3.6` (newer versions may or may not work)

Relevant Packages:

- `opencv-python`: 4.3.0.36
- `numpy`: 1.19.1
- `cmake`: 3.17.2
- `dlib`: 19.21.0
- `face-recognition`: 1.3.0

To add more students, add images to the `student_imgs` folder, with the title as the name of the person.

```bash
python app.py
```



