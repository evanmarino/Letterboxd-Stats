import pandas as pd
#panda option to not condense output 
pd.set_option("display.max_columns", None)

#Reads the original csv file
df = pd.read_csv("allWatched.csv")

#Drops the unneccessary columns
df= df.drop(df.columns[[2, 9]], axis =1)

#column "Date" becomes a date variable and reformats 
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.strftime("%m/%d/%Y")

#breaks down the csv file into the separate section based on Name
first = df.iloc[:, :4]
second = df.iloc[:, 4:6]
third = df.iloc[:, 6:8]
fourth = df.iloc[:, 8:]

#sorts the largest of the sections by name so all can be merged
second = second.sort_values(by="Name.1")

#merges all four sections together based on name 
df_merged = second.merge(first, left_on="Name.1", right_on="Name", how="left")
df = df_merged.merge(third, left_on="Name.1", right_on="Name.2", how="left")
df_merged = df.merge(fourth, left_on="Name.1", right_on="Name.3", how="left")

#drops all extra Name columns
df_merged= df_merged.drop(df_merged.columns[[3, 6, 8]], axis =1)

#renames Name.1 column into Movie Name
df_merged = df_merged.rename(columns={"Name.1": "Movie Name"})

#Reorders the columns
df_merged = df_merged[["Movie Name", "Year", "Ratings", "Dugan Ratings", "Date", "Liked", "Review"]]

#Uploads the sorted csv file to the computer
    #df_merged.to_csv("allWatched_ver3.csv", index=False)

#Checks if output is correct by displaying first 5 lines
print(df_merged.head())
