# IDLE (Python 3.8.0)

# Maximum Acceleration, Velocity

import math

c = 299792458.0 # m/s
HHV = c * 299792458.0 # m/s 
# HHV means Hypothetical Highest Velocity. Once figured out would become a constant instead of a hypothetical.
HHFN = c / (10**-18 * 2.0) # Hz 
# HHFN means Hypothetical Highest Frequency Needed. Once figured out would become a constant instead of a hypothetical.
MAV = 299792457.9 # m/s
# MAV means Maximum Acceleration, Velocity. Can’t exceed 299,792,457.0 to avoid division by zero.

print('The T (time) is in S (seconds). Preferably just 1 S to process sensor data then initiate')
print('deceleration and at least and at most 1 S to decelerate.')
print()
T = float(input('Enter time: '))
# T means Time.
print()
print('The DBSAD (Distance Between Ships After Deceleration is in m (meters). Assume the ship is using the')
print('highest possible MAV (Maximum Acceleration, Velocity) calculated with a DBSAD of 0 m.')
print()
DBSAD = float(input('Enter desired DBSAD: '))
# DBSAD means Distance Between Ships After Deceleration.
print()
DAHT = c / 2.0 - (MAV / 2.0)
# DAHT means Distance After Half Time.
DAFT = DAHT - (DAHT / (c / MAV + 1.0))
# DAFT means Distance After "Full" Time.
HDAFT = DAFT / 2.0
# HDAFT means Half DAFT.
while HDAFT < DBSAD:
    MAV = MAV - 1.0
    DAHT = c / 2.0 - (MAV / 2.0)
    DAFT = DAHT - (DAHT / (c / MAV + 1.0))
    HDAFT = DAFT / 2.0
DTS = HDAFT - DBSAD
# DTS means Distance To Stop.
TTS = (DTS / (T + (T - 1.0)) * (T + (T - 1.0) - 1.0) / MAV) + math.sqrt(DTS / (T + (T - 1.0)) / (MAV / 2.0))
# TTS means Time To Stop.
if TTS < T:
    while TTS < T or TTS > (T + 0.000000000001):
        MAV = TTS / T * MAV
        DAHT = c / 2.0 - (MAV / 2.0)
        DAFT = DAHT - (DAHT / (c / MAV + 1.0))
        HDAFT = DAFT / 2.0
        DTS = HDAFT - DBSAD 
        TTS = (DTS / (T + (T - 1.0)) * (T + (T - 1.0) - 1.0) / MAV) + math.sqrt(DTS / (T + (T - 1.0)) / (MAV / 2.0))
    MAVF = MAV / HHV * HHFN
    # MAVF means MAV Frequency.
    FROF = 1.0 / (MAVF * 2.0) / 2.0 * 1.0
    # FROF means Fast Rise Or Fall.
    SFOR = 1.0 / (MAVF * 2.0) / 2.0 * 3.0
    # SFOR means Slow Fall Or Rise.
    MSOO = c * (MAVF * 2.0 / HHFN)
    # MSOO means Minimum Speed Of Oscillation.
    MLOO = 10**-18 * 2 / (MAVF * 2.0 / HHFN)
    # MLOO means Maximum Length Of Oscillation.
    DIF = 1.0 / (MAVF * 2.0 / HHFN)
    # DIF means Decrease, Increase Factor.
    print ('Maximum Acceleration Velocity (MAV):', '{:,}'.format(round(MAV, 3)), 'm/s (',
    '{:,}'.format(round((MAV / 1000.0), 6)), 'km/s,', MAV / 299792458.0, 'c )')
    print()
    print('Maximum Acceleration, Velocity Frequency (MAVF):', '{:,}'.format(MAVF), 'c/s')
    print()
    print('Fast Rise Or Fall (FROF):', '{:,}'.format(FROF), 's')
    print()
    print('Slow Fall Or Rise (SFOR):', '{:,}'.format(SFOR), 's')
    print()
    print('Minimum Speed Of Oscillation (MSOO):', '{:,}'.format(MSOO), 'm/s')
    print()
    print('Maximum Length Of Oscillation (MLOO):', '{:,}'.format(MLOO), 'm')
    print()
    print('Decrease, Increase Factor (DIF):', DIF)
    print()
    print('Distance Between Ships After Deceleration (DBSAD):', '{:,}'.format(round(DBSAD, 3)),
    'm (', '{:,}'.format(round((DBSAD / 1000.0), 6)), 'km )')
else:
    DTDIOS = DAFT - (MAV * 1.0)
    # DTDIOS means Distance To Decelerate In One Second
    DAD = DTDIOS - (MAV / 2.0 * (1.0 ** 2.0))
    # DAD means Distance After Deceleration
    DBSAD = DAD * 2.0
    MAVF = MAV / HHV * HHFN
    FROF = 1.0 / (MAVF * 2.0) / 2.0 * 1.0
    SFOR = 1.0 / (MAVF * 2.0) / 2.0 * 3.0
    MSOO = c * (MAVF * 2.0 / HHFN)
    MLOO = 10**-18 * 2.0 / (MAVF * 2.0 / HHFN)
    DIF = 1.0 / (MAVF * 2.0 / HHFN)
    print ('Maximum Acceleration Velocity (MAV):', '{:,}'.format(round(MAV, 3)), 'm/s (',
    '{:,}'.format(round((MAV / 1000.0), 6)), 'km/s,', MAV / 299792458.0, 'c )')
    print()
    print('Maximum Acceleration, Velocity Frequency (MAVF):', '{:,}'.format(MAVF), 'c/s')
    print()
    print('Fast Rise Or Fall (FROF):', '{:,}'.format(FROF), 's')
    print()
    print('Slow Fall Or Rise (SFOR):', '{:,}'.format(SFOR), 's')
    print()
    print('Minimum Speed Of Oscillation (MSOO):', '{:,}'.format(MSOO), 'm/s')
    print()
    print('Maximum Length Of Oscillation (MLOO):', '{:,}'.format(MLOO), 'm')
    print()
    print('Decrease, Increase Factor (DIF):', DIF)
    print()
    print('Distance After Deceleration (DAD):', '{:,}'.format(round(DAD, 3)), 'm (',
    '{:,}'.format(round((DAD / 1000.0), 6)), 'km )')
    print()
    print('Distance Between Ships After Deceleration (DBSAD):', '{:,}'.format(round(DBSAD, 3)),
    'm (', '{:,}'.format(round((DBSAD / 1000.0), 6)), 'km )')
    
