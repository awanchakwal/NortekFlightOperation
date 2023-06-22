
from datetime import datetime, timedelta

# Calculate the date range for the current week
today = datetime.now().date()
print (today)
start_of_week = today - timedelta(days=today.weekday())
print (start_of_week)
end_of_week = start_of_week + timedelta(days=7)
print (end_of_week)
# Calculate the date range for the current week
# today = datetime.now().date()
# start_of_week = today - timedelta(days=today.weekday())
# end_of_week = start_of_week + timedelta(days=7)
#
# # Query to count flights meeting the criteria
# query = session.query(Flight).filter(
#     Flight.operator == 'AirArabia',
#     Flight.station == 'Lahore',
#     Flight.departure_date >= start_of_week,
#     Flight.departure_date < end_of_week
# )
# total_flights = query.count()
#////////////////////////////////////////////////////////////////
# Calculate the date range for the last week
today = datetime.now().date()
print(today)
one_week_ago = today - timedelta(days=7)
print(one_week_ago)
# Query to count flights
# count = session.query(Flight).filter(
#     Flight.operator == 'AirArabia',
#     Flight.station == 'Lahore',
#     Flight.departure_time >= start_date,
#     Flight.departure_time <= end_date
# ).count()
#
# print(f"Total flights: {count}")

#////////////////////////////////
# Get the current month
current_month = datetime.now().month
print(current_month)
# Query to count the flights
# total_flights = session.query(func.count()).\
#     filter(Flight.operator == 'AirArabia').\
#     filter(Flight.station == 'Lahore').\
#     filter(func.extract('month', Flight.date) == current_month).scalar()
#
# # Print the total number of flights
# print(f'Total flights where operator is AirArabia and station is Lahore in the current month: {total_flights}')

#////////////////////////////////////////////////////////////////
# Calculate the date range for the last month
last_month_start = datetime.now().date().replace(day=1) - timedelta(days=1)
print(last_month_start)
last_month_end = last_month_start.replace(day=1)
print(last_month_end)

# Perform the query
# total_flights = session.query(Flight).filter(
#     Flight.operator == 'AirArabia',
#     Flight.station == 'Lahore',
#     Flight.departure_time >= last_month_start,
#     Flight.departure_time <= last_month_end
# ).count()
#
# print(f"Total flights: {total_flights}")

#////////////////////////////////////////////////////////////////////////
# Define your table name and column names
# table_name = 'flights'
# operator_column = 'operator'
# station_column = 'station'
# date_column = 'date'
#
# # Build the query
# query = session.query(
#     getattr(table.c, operator_column),
#     getattr(table.c, station_column),
#     func.count()
# ).filter(
#     text(f"{date_column} >= :start_date AND {date_column} <= :end_date")
# ).group_by(
#     getattr(table.c, operator_column),
#     getattr(table.c, station_column)
# ).params(
#     start_date=start_date,
#     end_date=current_date
# )
#
# # Execute the query and fetch the results
# results = query.all()
#
# # Print the results
# for operator, station, count in results:
#     print(f"Operator: {operator}, Station: {station}, Count: {count}")
    #////////////////////////////////////////////////////////////////////////////////////////////////