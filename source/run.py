from flask import Flask, request, render_template
from resources import constants as c
from resources import mesh_generator_cone as mesh_generator
from resources import replace_file as rep_file
from resources import plot_data as image_plot

import sys
sys.path.append("/Users/HugoHugon/Documents/Code2022/simulator-api-challenge-00001/resources")

import os
import pandas as pd
import time

wind_simulator_app = Flask(__name__, template_folder='templates')

@wind_simulator_app.route('/', methods=["GET", "POST"])
def run_simulation():
    if request.method == "POST":
        major_radius = float(request.form.get("majradius"))
        minor_radius = float(request.form.get("minradius"))
        distance = float(request.form.get("dist"))
        wind_velocity = float(request.form.get("windvel"))

        # Boundary distances
        BD = 2 #2
        W = 2
        D = 1 #3

        # Mesh finesse x and y
        a = 4
        b = 8

        # Replace .cfg file placeholders according to input values
        rep_file.replace_text_in_file(minor_radius, major_radius, distance, a, b, wind_velocity)

        # Create mesh-file
        mesh_generator.generate_square_su2_file_mesh(minor_radius, major_radius, distance, BD, W, D, a, b)

        # Run SU2_CFD
        os.system('cp ./../output/' + c.OUTPUT_SU2_SQ_MESH_FILE_NAME + ' ' + c.SU2_HOME_RUN)

        os.system('cp ./../output/' + c.OUTPUT_SU2_CFG_FILE_NAME + ' ' + c.SU2_HOME_RUN)

        os.system('docker exec ' + c.DOCKER_CONTAINER + ' sh -c' + ' "cd ' + c.SU2_HOME_RUN_NAME \
                  + " && " + c.SU2_CFD_PARALLEL_BINARY + " " + c.OUTPUT_SU2_CFG_FILE_NAME + '"')

        os.system('docker ps')


        # make sure results are published
        time.sleep(2)
        # copy SU2_CFD results to output folder
        os.system('cp ' + c.SU2_HOME_RUN + '/history.csv ./../output/')
        os.system('cp ' + c.SU2_HOME_RUN + '/surface_flow.csv ./../output/')

        # Read and plot data
        surface_data = pd.read_csv("./../output/surface_flow.csv")
        image_plot.plot_image(minor_radius, major_radius, distance, BD, W, D, surface_data, "Energy")
        image_plot.plot_image(minor_radius, major_radius, distance, BD, W, D, surface_data, "Pressure")
        image_plot.plot_image(minor_radius, major_radius, distance, BD, W, D, surface_data, "Heat_Flux")


        return "Thank you for using wind_simulator_app!"

    return render_template("input_parameters.html")


if __name__ == '__main__':
    wind_simulator_app.run(debug=True, host='0.0.0.0', port=5000)
