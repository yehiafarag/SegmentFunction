import math

from segmentfunctionapp.handlers.function_handler import FunctionFileHandler
from segmentfunctionapp.handlers.segment_handler import SegmentFileHandler
from segmentfunctionapp.util.file_util import Util


class App:
    def __init__(self):
        # Util class is helping class
        self.segment_overlap_list = None


    def run(self, file_1, file_2):
        # Check files type (segment (.s) or function (.f)
        file_1_type=  Util.check_file_type(file_1)
        file_2_type = Util.check_file_type(file_2)
        #based on file type choose right function
        if file_1_type == file_2_type and file_1_type =="s":
            # case of 2 segments files calculate segments overlap between the 2 files
            self.process_segment_overlap(file_1,file_2)
        elif file_1_type == file_2_type and file_1_type =="f":
            # case of 2 function files calculate sample pearson correlation coefficient
            self.process_sample_pearson_correlation_coefficient(file_1,file_2)
        else:
            # case of 1 function file and 1 segment file calculate - function mean from a segment-covered
            if file_1_type =="s":
                self.process_function_mean_segments(file_1,file_2)
            else:
                self.process_function_mean_segments(file_2,file_1)


    def process_segment_overlap(self,file_1,file_2):
        segment_file_1_handler= SegmentFileHandler(file_1)
        segment_1_list = segment_file_1_handler.process_data()
        segment_file_2_handler= SegmentFileHandler(file_2)
        segment_2_list =segment_file_2_handler.process_data()
        self.calculate_segment_overlap(segment_1_list,segment_2_list)


    def calculate_segment_overlap(self,segment_1_list,segment_2_list):
        self.segment_overlap_list=set()
        for seg_1 in segment_1_list:
            for seg_2 in segment_2_list:
                if seg_2[0] >= seg_1[1]:
                    break
                if seg_1[0] >= seg_2[1]:
                    continue
                self.segment_overlap_list.update(Util.calculate_overlaps(seg_1[0],seg_1[1],seg_2[0],seg_2[1]))

        print(f"The overlaps number is {len(self.segment_overlap_list)}")
       # print(f"The overlaps are {self.segment_overlap_list}")

    def process_sample_pearson_correlation_coefficient(self,file_1,file_2):
        function_file_1_handler= FunctionFileHandler(file_1)
        function_1_list = function_file_1_handler.process_data()
        function_file_2_handler= FunctionFileHandler(file_2)
        function_2_list =function_file_2_handler.process_data()
        self.calculate_sample_pearson_correlation_coefficient(function_1_list,function_2_list)



    def calculate_sample_pearson_correlation_coefficient(self,function_1_list,function_2_list):
        mean_x = sum(function_1_list)/len(function_1_list)
        mean_y= sum(function_2_list)/len(function_2_list)
        sum_x_y=0
        sum_x_2=0
        sum_y_2=0
        for i in range(len(function_1_list)):
            updated_x = function_1_list[i]-mean_x
            updated_y = function_2_list[i]-mean_y
            sum_x_y += (updated_x*updated_y)
            sum_x_2 += (updated_x * updated_x)
            sum_y_2 += (updated_y * updated_y)

        sqrt_x = math.sqrt(sum_x_2)
        sqrt_y = math.sqrt(sum_y_2)
        pearson_correlation_coefficient=sum_x_y / (sqrt_x*sqrt_y)
        print(f"pearson_correlation_coefficient {pearson_correlation_coefficient} ")
        return pearson_correlation_coefficient

    def process_function_mean_segments(self,s_file,f_file):
        segment_file_handler= SegmentFileHandler(s_file)
        segment_list = segment_file_handler.process_data()
        function_file_handler= FunctionFileHandler(f_file)
        function_list = function_file_handler.process_data()
        self.compute_function_mean_segments(segment_list,function_list)


    def compute_function_mean_segments(self,segment_list,function_list):
        function_values=[]
        for segment in segment_list:
            for i in range(segment[0],segment[1]):
                function_values.append(function_list[i])

        function_mean = sum(function_values)/len(function_values)
        print(f"function mean from a segment-covered {function_mean}")
        return function_mean



def main():
  #for testing the main functions of the system
    app=App()
    segment_1_list = [[1, 2], [3, 6]]
    segment_2_list = [[0, 1], [1, 5]]
    app.calculate_segment_overlap(segment_1_list,segment_2_list)
    print(f"The overlaps are {app.segment_overlap_list}")

    function_1_list = [10.0,11.0,12.0,13.0,14.0,15.0,16.0]
    function_2_list = [10.5,11.5,12.0,13.0,13.5,15.0,14.0]
    app.calculate_sample_pearson_correlation_coefficient(function_1_list,function_2_list)

    app.compute_function_mean_segments(segment_1_list,function_2_list)



if __name__ == "__main__":
     main()
