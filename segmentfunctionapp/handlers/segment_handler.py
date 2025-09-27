from util.file_reader import FileReader


class SegmentFileHandler:

    def __init__(self, sfile):
       self.segment_file=sfile


    def process_data(self):
        segment_list=[]
        lines = FileReader.read_file(self.segment_file)
        for line in lines:
             line=line.strip()
             line_arr=line.split("\t")
             if len(line_arr)==2:
                 try:
                     segment_list.append([int(line_arr[0]),int(line_arr[1])])
                 except ValueError:
                     print(f"Invalid value:{line_arr[0],line_arr[1]}")
        return segment_list
