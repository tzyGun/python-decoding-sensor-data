# Runner script for all modules
from sensor import load_data
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_data.load_sensor_data()
print("Loaded records: {}".format(len(data)))
# Module 2 code here:

# Module 3 code here:

# Module 4 code here:

# Module 5 code here: