class Util:


    @staticmethod
    def check_file_type(file):
       if file.endswith(".s"):
           return "s"
       else:
           return "f"

    @staticmethod
    def calculate_overlaps(start_a, end_a, start_b, end_b):
        overlap_set = set()
        start = max(start_a,start_b)
        while start<= (end_b-1) and start <= (end_a-1) :
            overlap_set.add(start)
            start+=1
        return overlap_set