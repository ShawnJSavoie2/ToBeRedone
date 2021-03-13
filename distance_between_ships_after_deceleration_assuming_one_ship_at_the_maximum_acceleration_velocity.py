# IDLE (Python 3.8.0)

# Distance Between Ships After Deceleration Assuming One Ship At The Maximum Acceleration, Velocity

c = 299792458.0

print('Note: the velocity is in meters per second. It can\'t exceed 38,573,389.8308245 m/s')
print()
V = float(input('Enter velocity: '))
# V means Velocity.
print()
print('Note: the time is in seconds. One or more seconds --though preferably just one second-- to process')
print('sensor data then initiate deceleration and then one second to decelerate.')
print()
T = float(input('Enter time: '))
# T means Time.
print()
DAHT = c / 2.0 - (V / 2.0)
# DAHT means Distance After Half Time.
DAFT = DAHT - (DAHT / (c / V + 1.0))
# DAFT means Distance After Full time.
HDAFT = DAFT / 2.0
# HDAFT means Half DAFT.
DTDIOS = HDAFT - (V * (T - 1.0))
# DTDIOS means Distance To Decelerate In One Second.
DBSAD = DTDIOS - (V / 2.0)
# DBSAD means Distance Between Ships After Deceleration.
print('Distance between ships after deceleration:', '{:,}'.format(round(DBSAD, 3)), 'm (',
  '{:,}'.format(round((DBSAD / 1000.0), 6)), 'km )')
