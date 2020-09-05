from datetime import datetime

FILENAME = 'attendance.csv'

def mark_attendance(name):
    with open(FILENAME, 'r+') as f:
        # we need to read beforehand so we don't write students twice
        names = set()
        for line in f:
            names.add(line.split(',')[0].strip())
        if name not in names:
            now = datetime.now().strftime("%H:%M:%S")
            f.writelines(f'\n{name},{now}')




