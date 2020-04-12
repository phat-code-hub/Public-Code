START_OUT_DISTANCE=50
to_safety_distance=float(input('to safety:'))
roadrunner_speed=float(input('roadrunner: '))
cotoya_speed=float(input('Cotoya: '))
#time for roadrunner get to safety zone
time_to_safety=to_safety_distance/roadrunner_speed
cotoya_run_distance=time_to_safety*cotoya_speed
if cotoya_run_distance <(START_OUT_DISTANCE+to_safety_distance):
    print('Meep Meep')
else:
    print('Yum')