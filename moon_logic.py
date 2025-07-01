
def calculate_lunar_phase(dob):
    phases = ['New Moon', 'First Quarter', 'Full Moon', 'Last Quarter']
    index = dob.day % 4
    return phases[index]
