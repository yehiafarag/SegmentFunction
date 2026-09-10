# SegmentFunction

SegmentFunction is a lightweight Python tool for the computation of segment overlap between two segment files, calculation of the sample Pearson correlation coefficient between two function files, and calculating the mean for function values based on
entries indexed by segment regions.

## 🧬 What It Does
- Reads a SEGMENT file containing genomic intervals (start–end positions).
- Reads a FUNCTION file with one float per line, indexed by position.
- Compute segment overlap between two segment files.
- Calculation of the sample Pearson correlation coefficient between two function files
- Computes the mean of function values at positions covered by segment regions.

📁 Input Format
SEGMENT File
Tab-separated file with two columns per line with file extension  <b>(.s)</b> :
```
start<TAB>end
```

Example:
```text
1	3
4	5
```

FUNCTION File
Plain text file with one float per line with file extension <b>(.f)</b> :
```
1.0
2.0
3.0
4.0
5.0
```


For testing the system, download the latest release and sample input data:

**➡️ [release_1.0.zip](https://github.com/yehiafarag/SegmentFunction/releases/tag/v1.0)**

**➡️[Sample input data files](https://hyperbrowser.uio.no/hb/static/hyperbrowser/files/task_files/testfiles.tar.gz)**


### Unzip the downloaded file:

Locate the downloaded release_1.0.zip file on your computer.

Right-click on the file and select "Extract All" or use a tool like WinRAR or 7-Zip to unzip the file.

Extract the contents to a folder of your choice.


## 🚀 Usage
```
python path\to\segment_function_folder\run.py path\to\segment.s path\to\function.f
```
### Inputs
-  Two segments.s files (calculate segment overlap).
-  Two functions.f files (calculate the sample Pearson correlation coefficient between values in the two function files.
-  One function.f file and one segments.s file (Computes the mean of function values at positions covered by segment regions).

## 🛠 Requirements
- Python 3.13.7 or higher
- Recommended: virtual environment for isolation

<!--- test merge---->


## 🧪 Testing
Unit tests are included in the test folder. To run the function tests:
```
python -m unittest path\to\segment_function_folder\test\test_app.py
```






