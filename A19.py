from datetime import datetime,timedelta
presentday = datetime.now()
yesterday = presentday - timedelta(1)
tomorrow = presentday + timedelta(1)
print("Yesterday : ",yesterday.strftime('%d-%m-%y'))
print("Today : ",presentday.strftime('%d-%m-%y'))
print("Tomorrow : ",tomorrow.strftime('%d-%m-%y'))