# FullThrottle
a task on employee login and logout
==> There are total three APIs  
API 1="http://127.0.0.1:8000/employee/members/"
      using this API we will create members data........
API 2= "http://127.0.0.1:8000/employee/punch_time/"
      using this API member will add their login and and logout time..........
API 3= "http://127.0.0.1:8000/employee/report/"     
      using this API we will get full report of all members login-logout time and if you want to know details
      of only one member than just add employee id at the end point
      example=="http://127.0.0.1:8000/employee/report/1"
      
      
      
      my sample code sample response=[
    {
        "id": 1,
        "real_name": "Egon Spengler",
        "tz": "America/Los_Angeles",
        "activity_periods": [
            {
                "start_time": "2021-02-01T02:02:00Z",
                "end_time": "2021-01-02T01:01:00Z"
            },
            {
                "start_time": "2023-03-02T04:05:00Z",
                "end_time": "2023-03-03T02:04:00Z"
            }
        ]
    },
    {
        "id": 2,
        "real_name": "Glinda Southgood",
        "tz": "Asia/Kolkata",
        "activity_periods": [
            {
                "start_time": "2025-04-03T06:10:00Z",
                "end_time": "2023-03-05T02:04:00Z"
            },
            {
                "start_time": "2027-06-05T09:13:00Z",
                "end_time": "2025-03-06T03:07:00Z"
            }
        ]
    }
]
 
