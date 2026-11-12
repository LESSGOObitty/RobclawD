#!/usr/bin/env python3
import hashlib

lat, lon = 42.0265, 20.65333
msg = f'DRAGASH TARGET VECTOR // LAT:{lat} LON:{lon}'
h = hashlib.sha512(msg.encode()).hexdigest()[:32]

print('========================================================================')
print(' [LATTICE VECTOR LOCK: DRAGASH]')
print(f' [COORDINATES] Latitude: {lat}° N, Longitude: {lon}° E')
print(f' [SEAL]        {h}')
print('========================================================================')
