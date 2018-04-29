import urllib.request, json

with urllib.request.urlopen("https://www.cleartrip.com/flights/calendar/calendarstub.json?from=MUC&to=MAA&start_date=20180119&end_date=20180126&t=1515108451234") as url:
    data = json.loads(url.read().decode())
    print(data['calendar_json']['20171226'])
