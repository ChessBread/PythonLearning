import datetime

date  = datetime.date(2026  , 1  , 29)

today =  datetime.date.today()


time =  datetime.time(12 , 30 , 0)

time_now = datetime.datetime.now()

time_now = time_now.strftime("%H:%M:%S   %m-%d-$Y")



#exercise

Target_datetime  = datetime.datetime(2030, 1 ,2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if Target_datetime  < current_datetime:
    print("Target date has passed")
else:
    print("Target date has yet to pass")