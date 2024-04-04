import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Generate random data
policy_numbers = ['POL' + str(i) for i in range(1, 101)]
insured_names = ['John Doe', 'Alice Smith', 'Bob Johnson', 'Emma Brown', 'David Lee', 'Sophia Wang', 'Michael Jones', 'Olivia Taylor', 'James Davis']
receive_times = [datetime(2022, 1, 1) + timedelta(minutes=np.random.randint(1, 1440)) for _ in range(100)]
send_times = [receive + timedelta(minutes=np.random.randint(60, 1440)) for receive in receive_times]
start_dates = [datetime(2022, 1, 1) + timedelta(days=np.random.randint(1, 365)) for _ in range(100)]
end_dates = [start + timedelta(days=np.random.randint(30, 365)) for start in start_dates]

# Create DataFrame
data = {
    'Policy Number': policy_numbers,
    'Insured Name': [np.random.choice(insured_names) for _ in range(100)],
    'Receive Time': receive_times,
    'Send Time': send_times,
    'Start Date': start_dates,
    'End Date': end_dates
}
df = pd.DataFrame(data)
df.to_csv("C:/Users/PanuratSangchai(Tar)/Downloads/poetry-demo_update/poetry-demo/outputs/data.csv",
            index=False,
            sep=",",
            encoding="utf-8")
