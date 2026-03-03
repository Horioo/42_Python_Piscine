# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
# Oct 21 2022


import datetime

epochStart = datetime.datetime(1970, 1, 1)
today = datetime.datetime.now()

time_diff = today - epochStart
td_seconds = time_diff.total_seconds()
scientific_notation = "{:.2e}".format(td_seconds)

print("Seconds since", epochStart.strftime("%B %d, %Y") + ":", f"{td_seconds:,.4f}", "or", scientific_notation, "in scientific notation")
print(today.strftime("%b %d %Y"))