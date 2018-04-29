library(RJSONIO)

rawFlightData <- fromJSON("https://www.cleartrip.com/flights/calendar/calendarstub.json?from=MUC&to=MAA&start_date=20180109&end_date=20180208&t=1515450665")

print("Booking Munich Chennai Flights 1 Day in Advance")
print(rawFlightData)
for(i in 1:16)
{
  airline = rawFlightData[['calendar_json']][['20180109']][[i]][['aln']]
  price = rawFlightData[['calendar_json']][['20180109']][[i]][['pr']]
  print(sprintf("Cheapest %s flights available for %s INR", airline, price))
}

