
def replace_text_in_file(r, R, d, a, b, wind_velocity=10):
    dx = (r/2)/(a*(R/r))
    dy = d/b
    kinematic_visc_air = 0.00001
    rho_air = 1.23

    # Read in the file
    with open('./../output/Iam_cone_ref.cfg', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('${Reynolds}', str(r * wind_velocity/kinematic_visc_air))\
                       .replace('${RefLength}', str(r))\
                       .replace('${RefArea}', str(dx*dy))\
                       .replace('${InletPressure}', str(0.5*rho_air*wind_velocity**2)) \
                       .replace('${OutletPressure}', str((0.5*rho_air*wind_velocity**2)*0.85))

    # Write the file out again
    with open('./../output/Iam_cone.cfg', 'w') as file:
        file.write(filedata)