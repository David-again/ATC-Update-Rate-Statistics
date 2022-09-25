## Release Test Plan: Update Rate Statistics [URS].

____
The Testing approach for testing the URS script/algorithm is two-fold: 
### 1. Test with small datasets: `UpdateRateStatistcs.py`
This involves using *relatively small datasets*, usually created artificially (often for testing purposes) to prove the accuracy of the script/algorithm.  As with all test procedures, it requires an alternative method of processing the dataset in parallel, for validation purposes.  

**Benefit(s)**
- Edge cases can be tested for, since test data is artificially created.

**Limitation(s)**
- If manual validation is required, this limits the size of the dataset that can be used, thereby eliminating real-life data in most cases. 

Some example datasets are provided, see below at the bottom of this document.  To change the file being used and conduct Manual Testing using `UpdateRateStatistics.py`, edit the line 6:

        `datafile_path = "data/sampledata1.csv"      #change input file here`
        
and replace with the filename of the desired file.
### 2. Test with live dataset, *one airplane/aircraft per time*: `ManualTest`
This involves testing with *large (operational-sized) datasets*, but "manually" processing one airplane per test run.  The advantage of this is that the output is more manageable and is not overwhelming to review manually, as only one JSON object is returned.

**Benefit(s)**
- Real-life input data can be used, as the data generated for one aircraft tends to be manageable for manual validation processes. 

**Limitation(s)**
- Edge cases may be missed during testing, if they relate to the process used to iterate over multiple aircraft.

#### 2.1 Manual Test Procedure: Input data parameters.
The following parameters should be used alongside `ManualTest.py` to conduct testing, similar to the process described above.  The files specified below can be found in the same folder named `/data`, which stores the `sampledata1.csv` file supplied with this exercise.

`Filename` | `Target Address`
-|- 
`"data/sample_0005recs.csv"` | `"ABCDEF"`or`"123456"`
`"data/sample_0199recs.csv"` | `"C054D1"`or`"89902F"`
`"data/sample_0499recs.csv"` | `"89902F"`or`"A6657E"`
`"data/sample_0999recs.csv"` | `"A6657E"`or`"A09947"`
`"data/sample_4999recs.csv"` | `"C038AA"`or`"A09947"`
`"data/sample_9999recs.csv"` | `"A6657E"`or`"A09947"`
`"data/sample_100krecs.csv"` | `"C038AA"`or`"A9FDEB"`

This can be done by editing lines 9 and 10 in `ManualTest.py`:

            `filepath = "data/sample_100krecs.csv"`
            `test_targetAddress = "C038AA"`

The difference amongst all these files is the number of records contained therein, as is implied in the respective filenames.  For example, `"data/sample_0099recs.csv"` contains 99 records (and therefore 100 lines, since each file comes with a coulumn header/column label by default).

#### 2.2 Error handling 
Error-handling is not done for the following scenarios: 
- Invalid file path
- Correct path, but wrongly formatted `.CSV` file
- Null values in the `.CSV` file

In the event an invalid targetAddress was provided during manual testing, the following will be written to the `output.json` file, and also printed:

`[{"error": "The specified targetAddress does not exist in the test file! Please check and then run this test again."}]`

**Note:** 
- This error handling is only done for `ManualTest.py`, and not for `UpdateRateStatistics.py`

>Thank you for taking the time to review my work.  I hope to hear from you soon, eager to answer any questions!
(c) 2022 David Ogunbanjo
d.ogunbanjo@yahoo.com