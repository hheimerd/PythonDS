class Research:
    def file_reader(self):
        with open('data.csv') as file:
            return file.read()


if __name__ == "__main__":
    try:
        print(Research().file_reader())
    except Exception:
        print('File not found')
