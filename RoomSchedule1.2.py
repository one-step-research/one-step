import re
import datetime
import pandas as pd

class searchRooms:
    def __init__(self, roomID):
        self.roomID = roomID # <---- Defines the user room thorugh input. Modify it to take input from the GUI as a command
        return
    
    def showRooms(self):
        roomMatches = []
        if self.roomID in roomList:
            print(self.roomID) # <---- Shows the room the user was looking for. Modify it to show it in the GUI rather than in the Shell
        else:
            for i in range(len(roomList)):
                check_room = re.search(self.roomID, roomList[i]) # Finds courses that start with what the user has input
                if check_room is not None:
                    roomMatches.append(roomList[i]) # Adds possible courses that the user may be looking for
            for j in range(len(roomMatches)):
                print(roomMatches[j]) # <---- Shows the course Suggestions to the user. Modify it to show it in the GUI rather than in the Shell
        return

class searchCourse:
    def __init__(self, courseID):
        self.courseID = courseID # <----- Defines the user course though input. Modify it to take input from the GUI as a command
        return
    
    def showCourses(self):
        courseMatches = []
        if self.courseID in roomList:
            print(self.courseID) # <----- Shows the course the user was looking for. Modify it to show it in the GUI rather than in the Shell
        else:
            for i in range(len(roomList)):
                check_room = re.search(self.courseID, roomList[i]) # Finds courses that start with what the user has input
                if check_room is not None:
                    courseMatches.append(roomList[i]) # Adds possible courses that the user may be looking for
            for j in range(len(courseMatches)):
                print(courseMatches[j]) # <----- Shows the course Suggestions to the user. Modify it to show it in the GUI rather than in the Shell
        return

class setSchedule:
    def __init__(self, month, day, year):
        # Get values of day, month, year from the user as inputs from GUI
        # ------------------
        self.month = month 
        self.day = day
        self.year = year
        # ------------------
        return 
        
    def combineDate(self):
        convertDate = str(self.month + "/" + self.day + "/" + self.year) # Convince month, day, and year
        userDate = datetime.datetime.strptime(convertDate, "%m/%d/%Y") # Converts the previous dat to a MM/DD/YYYY format
        return userDate

class setTime:
    def __init__(self, startHours, startMin = 0, endHours, endMin = 0, start_PM = False, end_PM = False):
        # Get values from the user in hours
        # ------------------------------------------------
        if (startHours < 12) and (endHours < 12): # The time format can only be between 0 and 12
            if (start_PM is False): # Checks if the course is in the afternoon
                self.startHours = startHours # Sets the hours for a course to start
            else :
                self.startHours = startHours + 12
                
            if (end_PM is False): # Checks if the course is in the afternoon
                self.endHours = endHours # Sets the hours for a course to end
            else :
                self.endHours = endHours + 12
        # ------------------------------------------------
        # Get values from the user in minutes
        # ------------------------------------------------
        self.startMin = startMin
        self.endMin = endMin
        # ------------------------------------------------
        return
    
    def timeStart(self):
        convertStart = str(str(self.startHours) + ":" + str(self.startMin))
        startTime = datetime.datetime.strptime(convertStart, "%H:%M").time()
        return startTime
    
    def timeEnd(self):
        convertEnd =  str(str(self.endHours) + ":" + str(endMinutes))
        endTime = datetime.datetime.strptime(convertEnd, "%H:%M").time()
        return endTime
        
    
# Import data from excel
# -----------------------------------------------------------------------------------------
courseData = pd.read_excel("CourseList.xlsx") # Imports the excel file "CourseList.xlsx" with the names of the courses
meetingDays = pd.read_excel("MeetingTimes.xlsx")
courseDuration = pd.read_excel("CreditDuration.xlsx")
setScheduleData = pd.read_excel("SetSchedule.xlsx")

roomData = pd.read_excel("RoomList.xlsx") # Imports the excel file "RoomList.xlsx" with the name of the rooms
# -----------------------------------------------------------------------------------------

# Convert excel files to dictionaries or lists
#-------------------------------------------------------------------------------------------------------------
# Lists
courseList = list(dict.fromkeys(courseData['Course'])) # List of courses for the program to search for matches
roomList = list(dict.fromkeys(roomData['Room'])) # List of rooms for the program to search for matches
# Dictionaries
creditsDict = dict(zip(courseDuration['Course'], courseDuration['Credits'])) # How many credits a course has
durationDict = dict(zip(courseDuration['Credits'], courseDuration['Duration'])) # How long a course will last according to their credits
# ------------------------------------------------------------------------------------------------------------
