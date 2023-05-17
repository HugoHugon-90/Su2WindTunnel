#2-D
DIM = 2

#Paths
OUTPUT_FILE_PATH = './../output/'
OUTPUT_SU2_SQ_MESH_FILE_NAME = 'square_mesh.su2'
OUTPUT_SU2_CFG_FILE_NAME = 'Iam_cone.cfg'


#Docker container name
DOCKER_CONTAINER = 'SU2Container'

#SU2 Run directory
SU2_HOME_RUN_NAME = 'SU2HomeRun'
SU2_HOME_RUN ='/Users/HugoHugon/'+SU2_HOME_RUN_NAME

#SU2 executable (c++)
SU2_CFD_BINARY = "SU2_CFD"
SU2_CFD_PARALLEL_BINARY = "mpirun --allow-run-as-root -n 2 SU2_CFD"