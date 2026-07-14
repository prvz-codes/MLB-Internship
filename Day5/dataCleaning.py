import pandas as p

stdData = p.read_csv("student_records.csv")

stdData["Average_Marks"] = stdData[["Math" , "English","Science","Computer","Physics","Chemistry"]].mean(axis=1)


stdData.drop(columns=["City"] , inplace=True)


stdData.rename({'Attendance(%)' : 'Attendance'} , axis=1 , inplace=True)
stdData.rename({'StudentID':'Roll_No'}, axis=1 , inplace=True)
# print(stdData.head())


stdData["Country"] = "Pakistan"
print(stdData.head())


stdData["Performance"] = ""

stdData.loc[stdData["Average_Marks"] >= 90 , "Performance" ] = "Excellent"
stdData.loc[(stdData["Average_Marks"] < 90 )&(stdData["Average_Marks"] >= 80), "Performance" ] = "Good"
stdData.loc[(stdData["Average_Marks"] < 80 )&(stdData["Average_Marks"] >= 70), "Performance" ] = "Average"
stdData.loc[stdData["Average_Marks"] < 70 , "Performance" ] = "Needs Improvement"
print(stdData.head())
# print(uniqueNames["Name"])

# print(uniqueClasses)


stdData.fillna(0 , inplace=True)

stdData.to_csv("cleaned_student_data.csv" , index=False)

