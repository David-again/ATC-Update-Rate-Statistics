import json
import pandas as pd
pd.options.mode.chained_assignment = None 

# Specify the following to be used for this manual test: 
#      1. filepath of the csv file,
#      2. string value for targetAddress

filepath = "data/sample_100krecs.csv"
test_targetAddress = "C038AA"

tmp01 = pd.read_csv(filepath)    # 1. Read the data from the input file
tmp01["timestamp"] = pd.to_datetime(tmp01["Time"])   #2 Create new time column of type datetime from existing string column
tmp01.rename(columns={"Target Address": "targetAddress"}, inplace=True)    #3 Rename the column to targetAddress
allAirData = tmp01[["timestamp", "targetAddress"]]  #4 create new DataFrame with datetime data,

#5 Extract data for 1 aircraft
acmask = allAirData["targetAddress"] == test_targetAddress    # Create boolean series
test_airData = allAirData[acmask]    # Filter with the mask

if test_airData.empty:
    # An invalid targetAddress has been provided.
    jsonError = {
        "error": "The specified targetAddress does not exist in the test file! Please check and then run this test again."
    }
    strOutput = "[" + json.dumps(jsonError) + "]"
    print(strOutput)
else:
    test_airData["timedelta"] = test_airData["timestamp"].diff()  # 6 Calculate time delta and store in a new column
    test_airData_gbo = test_airData.groupby("targetAddress")    # 7 Create GroupBy Object
    totalTimeSeries = test_airData_gbo["timedelta"].sum()    # 8 alculate the total time
    totalTime = totalTimeSeries[0]   # Convert from timedelta to seconds

    # 9 Calculate average update rate
    numUpdates = test_airData.shape[0] - 1     # First entry in the file is ignored.
    if numUpdates < 1: 
        # There's only 1 record for this airplane, or not enough to calculate update rate statistics.
        totalTime = 0
        avgUpdateRate = 0
    else:    
        avgUpdateRate = (totalTime / numUpdates)

    # 10a Store results in a dictionary
    test_airDict = {
        "targetAddress": test_targetAddress,
        "averageUpdateRateSeconds": avgUpdateRate.total_seconds(),
        "totalFlightTimeSeconds": totalTime.total_seconds() 
    }

    # 10b Convert dictionary to String
    strOutput = "[" + json.dumps(test_airDict) +"]"

# 11 Write results to a test output file.
f = open("test-output.json", "w")
f.write(strOutput)
f.close()
