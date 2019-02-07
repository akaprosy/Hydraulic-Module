#Hydraulic module

def force_pascal(pressure, area):
    """Calculate pressure given pressure and area"""
    return pressure * area

def pressure_pascal(area, force):
    """Calculate pressure given area and force"""
    return force/pressure

def area_pascal(pressure, force):
    """Calculate area given pressure and force"""
    return force / pressure

def horsepower_pump(pressure,flow):
    """Calculate horsepower given pressure and flow"""
    return (pressure * flow)/1714

def pump_flow(displacement, speed):
    """Calculate flow given displacement and speed"""
    return (displacement * speed)/231


def horsepower_motor1(torque, speed):
    """Calculate horsepower given torque(in-lbs) and rpm"""
    return (torque * speed)/5252

def horsepower_motor2(torque, speed):
    """Calculate horsepower given torque(ft-lbs) and rpm"""
    return (torque * speed)/63025

def torque_motor(displacement, pressure):
    """Calculate torque given displacement and pressure"""
    return (displacement * pressure)/6.28
    
def cylinder_velocity(stroke, time):
    """Calculate cylinder velocity given stroke and time"""
    return stroke * (60/time)

def flow_velocity(velocity, area):
    """Calculate flow given velocity and area"""
    return (velocity*area)/231




