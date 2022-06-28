## Manual Test Procedure: Overview
The Manual Testing approach for testing the URS script/algorithm is two-fold: 
### 1. `ManualTest_01`: Test with small datasets:
This involves using *relatively small datasets*, usually created artificially (often for testing purposes) to prove the accuracy of the script/algorithm.  As with all test procedures, it requires an alternative method of processing the dataset in parallel, for validation purposes.  

**Benefit(s)**
- Edge cases can be tested for, since test data is artificially created.

**Limitation(s)**
- If manual validation is required, this limits the size of the dataset that can be used, thereby eliminating real-life data in most cases. 

### 2. `ManualTest_02`: Test with live dataset, *one airplane/aircraft per time* 
This involves testing with *large (operational-sized) datasets*, but "manually" processing one airplane at a time.  The advantage of this is that the output is more manageable and is not overwhelming to review manually.

**Benefit(s)**
- Real-life input data can be used, as the data generated for one aircraft tends to be manageable for manual validation processes. 

**Limitation(s)**
- Edge cases may be missed during testing, if they relate to the process used to iterate over multiple aircraft.

## Manual Test Procedure: Input data parameters.
The following parameters should be applied to conduct `Manual_02` testing as described above.  The files specified below can be found in the same folder named `/data`, which stores the `sampledata1.csv` file supplied with this exercise.

`Filename` | `Target Address`
-|- 
`"data/sample_0005recs.csv"` | `"ABCDEF"`
`"data/sample_0199recs.csv"` | `"ABCDEF"`
`"data/sample_0499recs.csv"` | `"ABCDEF"`
`"data/sample_0999recs.csv"` | `"ABCDEF"`
`"data/sample_499recs.csv"` | `"ABCDEF"`
`"data/sample_9999recs.csv"` | `"ABCDEF"`

The difference amongst all these files is the number of records contained therein, as is implied in the respective filenames.  For example, `"data/sample_0099recs.csv"` contains 99 records (and therefore 100 lines, since each file comes with a coulumn header/column label by default).