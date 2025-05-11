 import datetime
chose=int(input("1.Compare from your setted time\n2.Compare by Time now\nchose:"))
if chose==1:
    def diff_time(start_time,end_time):
        """ This allow User to set time of start and end time by Entering Each
         y=str(input("Enter Start_Time in This Format:%Y-%m-%d %H:%M:%S : ")) 

         x=str(input("Enter End_Time in This Format:%Y-%m-%d %H:%M:S : "))
         This result different in time as shown in formular 
         Diffferent= end_time-start_time """
        try:
            start_time=datetime.datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")#This allow user to change entered time into valid time
            end_time=datetime.datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")#This allow user to change entered time into valid time
        except ValueError:
            print("Invalid format! try this :%Y-%m-%d %H:%M:%S")
            return
        Diffferent= end_time-start_time
        print(f"Time different:{abs(Diffferent).days}")
        if Diffferent.total_seconds()>0:
            print(f"Time Left:{Diffferent}")
        elif Diffferent.total_seconds()<0:
            print(f"Time passed:{Diffferent}")
        else:
            print(f"Same Time!:{Diffferent}")
    y=str(input("Enter Start_Time in This Format:%Y-%m-%d %H:%M:%S : "))
    x=str(input("Enter End_Time in This Format:%Y-%m-%d %H:%M:S : "))
    diff_time(y,x)#function call
if chose==2:
    def time_diff(star_time,End_time):
        """ This allow user to set End time only 
            then start time will be time now 
            them make different  of time bring result into days!"""
        try:
            End_time=datetime.datetime.strptime(End_time,"%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid format use this:%Y-%m-%d %H:%M:%S")
            return
        print(f"Start Time:{star_tim.strftime("%Y-%m-%d %H:%M:%S")}")
        different=End_time-star_time
        print(f"Time different:{abs(different).days} Day")#This return time as absolute without Negative sign
        if different.total_seconds()>0:
            print(f"Time Left:{different}")
        elif different.total_seconds()<0:
            print(f"Time passed:{abs(different)}")
        else:
            print(f"Same Time!:{different}")
    star_tim=datetime.datetime.now()
    Z=str(input("Enter End_Time in This Format:%Y-%m-%d %H:%M:S : "))#this allow user to set end time
    time_diff(star_tim,Z)#function call
else:
    print("Choice again!")