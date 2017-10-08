import datetime

filename = datetime.datetime.now()

def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f"), "w") as file:
        file.write("")

create_file()
