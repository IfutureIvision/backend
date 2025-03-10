# import snap7
# from snap7.util import get_int, get_real, get_string

# # Define PLC Connection Parameters
# PLC_IP = "192.168.0.1"  # Change to your PLC's IP address
# RACK = 0
# SLOT = 1  # For S7-1200/S7-1500 use Slot 1

# # Connect to PLC
# plc = snap7.client.Client()
# plc.connect(PLC_IP, RACK, SLOT)

# # Read Data from PLC (Example: Read from DB1)
# DB_NUMBER = 1  # Data Block number
# START_ADDRESS = 0  # Start from byte 0
# SIZE = 10  # Number of bytes to read

# data = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)

# # Extract values from data
# int_value = get_int(data, 0)      # Read INT (2 bytes)
# real_value = get_real(data, 2)    # Read REAL (4 bytes)
# string_value = get_string(data, 6, 4)  # Read STRING (4 bytes)

# # Print Values
# print(f"Integer Value: {int_value}")
# print(f"Real Value: {real_value}")
# print(f"String Value: {string_value}")

# # Close connection
# plc.disconnect()




# import snap7

# PLC_IP = "192.168.0.1"
# RACK = 0
# SLOT = 1

# plc = snap7.client.Client()
# plc.connect(PLC_IP, RACK, SLOT)

# try:
#     for db in range(1, 10):  # Check first 10 DBs
#         try:
#             data = plc.db_read(db, 0, 1)
#             print(f"✅ Successfully read from DB{db}")
#         except Exception as e:
#             print(f"❌ Failed to read DB{db}: {e}")

# finally:
#     plc.disconnect()

