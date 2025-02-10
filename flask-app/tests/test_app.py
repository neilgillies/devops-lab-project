from app import calculate_race_times, format_time
def test_format_time():
  assert format_time(0) == "00:00"
  assert format_time(1) == "00:01"
  assert format_time(60) == "01:00"
  assert format_time(3600) == "01:00:00"
  assert format_time(3661) == "01:01:01"
def test_calculate_race_times():
  # pace per k is 5 min
  #TODO: complete the dict with the expected times
  distance_result = {
  "5K": "25:00",
  "10K": "50:00",
  "Half Marathon": "1:45:29",
  "Marathon": "3:30:58"
  }
  assert calculate_race_times(5) == distance_result