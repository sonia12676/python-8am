import datetime

# b_date=datetime.datetime(1993,5,10) 
# print(type(b_date))

# date=datetime.datetime.strptime(b_date,"%Y-%m-%d")

# dates=datetime.datetime.isocalendar(date)
# print(dates)

# today=datetime.date.toady()
# print(today.strftime("%d/%m/%Y"))
# b_date-datetime.date(1993,5,10)
# today=datetime.date.today()
# dd=today-b_date
# print(dd.days)



jobs=[
    {'title':'python developer', 'exp_date': '2024-12-31'},
    {'title':'data scientist', 'exp_date': '2026-11-30'},
    {'title':'web developer', 'exp_date': '2025-01-15'},
]
for job in jobs:

    exp_date=datetime.datetime.strptime(job['exp_date'],"%Y-%m-%d")
    today=datetime.datetime.now()
    if exp_date>today:
        print(f"Job {job['title']} is still valid")
    else:
        print(f"Job {job['title']} is has expired")


# exception handling (file handling-> mode: a, w , r, x, b,t

# def display(jobs):
#     job_title=input("Enter job title:")
#     for job in jobs:
#         if job['title']==job_title:
#             exp_date=datetime.datetime.strptime(job['exp_date'],"%Y-%m-%d")
#             # print(type(exp_date))
#             # print(type(job['exp_date']))
#             today=datetime.datetime.now()
#             if exp_date>today:
#                 print(f"Job {job['title']} is still valid")
#             else:
#                 print(f"Job {job['title']} is has expired")
#         else:
#             print(f"Job {job_title} not found")


# display(jobs=[
#     {'title':'python developer', 'exp_date': '2024-12-31'},
#     {'title':'data scientist', 'exp_date': '2026-11-30'},
#     {'title':'web developer', 'exp_date': '2025-01-15'},
# ])
