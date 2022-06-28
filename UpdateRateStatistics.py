#1 Import Pandas, json and the input file
import json
import pandas as pd
pd.options.mode.chained_assignment = None  
# tmp01 = pd.read_csv("data/sample_999recs.csv")
tmp01 = pd.read_csv("data/sampledata1.csv")

#2 Create new time column of type datetime from existing string column
tmp01["timestamp"] = pd.to_datetime(tmp01["Time"])

#3 Rename the column to targetAddress 
tmp01.rename(columns={"Target Address": "targetAddress"}, inplace=True)

#4 create new DataFrame with datetime data, discarding extraneous info from original file
allAirData = tmp01[["timestamp", "targetAddress"]]

# 5a Initialize loop variable and String Accumulator for final result 
strAccumulator = ""

# Create list of unique target addresses, and loop through this list
tgtAddressList = allAirData["targetAddress"].unique()

for currTgtAdd in tgtAddressList:
    #  Extract DataFrame for current aircraft
    ac_mask = allAirData["targetAddress"] == currTgtAdd         # Create filter mask
    currAcDataFrame = allAirData[ac_mask]                        # DataFrame for current aircraft

    if currAcDataFrame.shape[0] < 2:
        # There's only 1 record for this airplane, or not enough to calculate update rate statistics.
        # Therefore, return zeros (for this aircraft only).
        currAcDict = {
            "targetAddress": currTgtAdd,
            "averageUpdateRateSeconds": 0,
            "totalFlightTimeSeconds": 0
        }
    else:
        #6 Calculate time delta and store in new column
        currAcDataFrame["timedelta"] = currAcDataFrame["timestamp"].diff()

        #7 Create GroupBy object
        currAcDataFrame_gbo = currAcDataFrame.groupby("targetAddress")

        #8 Calculate the total time
        totalTimeSeries = currAcDataFrame_gbo["timedelta"].sum()
        totalTime = totalTimeSeries[0]

        #9 Calculate average update rate
        numUpdates = currAcDataFrame.shape[0]
        avgUpdateRate = totalTime / (numUpdates - 1)  # The first entry in the DataFrame is ignored.

        #10a Store results of current aircraft in a dictionary
        currAcDict = {
            "targetAddress": currTgtAdd,
            "averageUpdateRateSeconds": avgUpdateRate.total_seconds(),
            "totalFlightTimeSeconds": totalTime.total_seconds()
        }
    # 10b Convert dictionary to String (in preparation for writing to output file)
    strResult = json.dumps(currAcDict)

    # 10c Append results of current aircraft to String Accumulator
    strAccumulator = strAccumulator + strResult 

    # Concatenate a comma, unless this is the last item
    if currTgtAdd != tgtAddressList[len(tgtAddressList)-1]:
         strAccumulator += ", "

# This is where each iteration ends.

# 11a Append Square braces to either side of string accumulator
strAccumulator = "[" + strAccumulator + "]"

# 11b Write the results to a file
f = open("output.json", "w")
f.write(strAccumulator)
f.close()