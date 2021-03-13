# IDLE (Python 3.8.0)

# Distance Between Ships After Deceleration

c = 299792458.0

print('Note: the velocity is in m/s. It can\'t exceed the highest possible maximum acceleration, velocity')
print('calculated with the same time that is going to be entered below.')
print()
VOS1 = float(input('Enter velocity of ship one: '))
# VOS1 means Velocity Of Ship 1.
print()
print('Note: the velocity is in m/s. It can\'t exceed the highest possible maximum acceleration, velocity')
print('calculated with the same time that is going to be entered below.')
print()
VOS2 = float(input('Enter velocity of ship two: '))
# VOS2 means Velocity Of Ship 2.
print()
print('Note: the time is in seconds. Preferably just 1 s to process sensor data then initiate deceleration')
print('and then just 1 s to decelerate.')
print()
T = float(input('Enter time: '))
# T means Time.
print()
VOSL = [VOS1, VOS2]
# VOSL means Velocity Of Ships List.
DBSAD = 0
# DBSAD means Distance Between Ships After Deceleration.
for V in VOSL:
    DAHT = c / 2.0 - (V / 2.0)
    # DAHT means Distance After Half Time.
    DAFT = DAHT - (DAHT / (c / V + 1.0))
    # DAFT means Distance After Full time.
    HDAFT = DAFT / 2.0
    # HDAFT means Half DAFT.
    DTDIOS = HDAFT - (V * (T - 1.0))
    # DTDIOS means Distance To Decelerate In One Second.
    WDBSAD = DTDIOS - (V / 2.0)
    # WDBSAD means Working DBSAD.
    DBSAD = DBSAD + WDBSAD
print('Distance between ships after deceleration:', '{:,}'.format(round(DBSAD, 3)), 'm (',
  '{:,}'.format(round((DBSAD / 1000.0), 6)),'km )')
