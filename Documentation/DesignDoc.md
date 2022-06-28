# Update Rate Statistics [URS].
#### A tool for analyzing aircraft traffic data 
_______

"Update Rate Statistics", or URS, is a tool written in Python for interpreting and processing voluminous data gathered about aircraft as they communicate with Air Traffic Control (ATC) infrastructure. 

## Scope
Specifically, URS accepts as input, a CSV file containing time-series data, but for all aircraft, as this data is apparently recorded from the perspective of the ATC infrastructure on the receiving receiving end of a one-to-many connection with several airborne aircraft, over a period of time.

The goal of the tool is to "reduce" this data into an intelligible format (sorted by aircraft), thereby reflecting the frequency with which updates are received from each aircraft.  Hence the terms "Update Rate" in the name.

Additionally, it must be mentioned that only historical data is used for this analysis, hence the word "Statistics" in the name.

 

## Definitions and Acronyms

- ATC: Air Traffic Control
- O(N)-time: Time-complexity of an algorithm, a measure of how much time it would take for the said algorithm to run.
- O(N)-space: Space-complexity of an algorithm, a measure of how much memory is required.

## Architectural Design 

The "raw" data supplied by the .CSV file is "cleaned up" by converting from string format to date (for intelligible calculations), the aircraft identifier ("target address") is used to group data before it is processed, conditions are introduced to cater for edge cases, and finally, the results of all computations are output onto a JSON file, facilitating transmission among web applications, while also being easily human readable. 


## Data Design

Originally given only two columns, a time series and corresponding aircraft ID. This forms a "master table" from which "child tables" are created for each aircraft.
Table name | Purpose
-|- 
Master table | collate and group data per aircraft
Child table (per aircraft) | perform computations


A new column was created reflecting the *"time-deltas"* between successive signal updates received from each aircraft.

Python and the Pandas library is used because of its data manipulation and analysis capabilities for the complexities described above, as well as data the reduction requirement.


## Data Flow
With data manipulated, reduced/aggregated and processed per aircraft into the desired output format (JSON), it is written onto an `output.json` file in the same folder as the script, for easy access. Note that multiple runs of the script/program will overwrite previously created files.

## User Interface

The script can be run using Jupyter Notebooks.

## Appendices
Currently, this section is intentionally blank
>Thank you for taking the time to review my work.  I hope to hear from you soon!
(c) 2022 David Ogunbanjo
d.ogunbanjo@yahoo.com