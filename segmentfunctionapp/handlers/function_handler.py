from util.file_reader import FileReader


class FunctionFileHandler:

    def __init__(self, ffile):
        self.function_file=ffile


    def process_data(self):
        function_list=[]
        lines = FileReader.read_file(self.function_file)
        for line in lines:
            line=line.strip()
            try:
                function_list.append(float(line))
            except ValueError:
                print(f"Invalid value:{line}")
        return function_list