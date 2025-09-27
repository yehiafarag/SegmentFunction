class FileReader:
    @staticmethod
    def read_file(file):
        array_list = []
        with open(file, "r") as file:
          lines=  file.readlines()
        return lines

