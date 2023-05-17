# Simulator API challenge

In this challenge we would like to gather information about two main things: 
1) your ability to use your computational Physics background to configure a relevant simulation case;
2) your ability to quickly deal with new technology stacks and achieve a working prototype, with limited time and resources.

For that purpose we ask you to:

1) Implement a wind tunnel simulation, where one can place a parametric shape.
2) Deploy this in a client-server architecture, behind a simple API. 

Let's go into the details:


### Wind Tunnel Simulation 

Pick one existing open-source simulator for Computational Fluid Dynamics (CFD), for example:

https://www.openfoam.com/

https://su2code.github.io/

(or other alternative that you might find more suitable)

and define a simulation scneario that is representative of a wind tunnel where you can place an object of your choice.
For example, here is an illustration from the SU2 simulation:

<img width="1131" alt="image" src="https://user-images.githubusercontent.com/1058075/195038083-cc407b01-234c-4c50-b5b6-5c71e617a2cc.png">

Don't worry, we are going to simulate much simpler shapes! :)

### Parametric shape

Assume that the kind of objects you want to place inside the wind tunnel are cones (in an horizontal position), with three controlable parameters:

1) radius of the left circle
2) length of the cone
3) radius of the right circle

![image](https://user-images.githubusercontent.com/1058075/195039000-d1bd88ee-2ea5-4785-9685-89c37be5b599.png)

### Simple Web API

Use a technology such as [Flask](https://flask.palletsprojects.com/en/2.2.x/) or [FastAPI](https://fastapi.tiangolo.com/) to define a minimalistic Python webserver and API, where you can make a request where you pass the 3 parameters of the shape, plus one parameter of the simulation (such as wind speed) and this triggers the simulator to run.
Once the simulation is over, return some results (either the raw files, some important metrics, or simple visualizations).

Note: with a client-server architecture, the server could be running on a remote machine and the client on your local machine, but for simplicity you can deploy both locally, and one should still be able to test that everything works. 

### Containers

To make sure that your simulator can be installed and run in different computer architectures, consider packing it inside a [Docker](https://www.docker.com/) container (note: your simulator of choice might already provide instructions for this).

### Recommendations

- please check-in all the relevant code and files into the github repository.
- please add a README file with any running instructions.
- note that what is important in this exercise is that you are able to have something "good enough" running under this strict time constraints (just a few days). Our goal is not to evaluate whether it is super "polished" (e.g. don't worry about input validation, or very complicated visualizations -- if these prove to demand too much development effort). However, if you have the time, any creative improvement could be a plus, and we would be happy to hear about it.
- Do you need to simplify something? If running a 3d simulation turns out to be unfeasible for the computational resources you have available, what if you simplify it to a 2D scenario? Having something running that captures all the components of the simulation API, is more important than having an unfinished "powerful" simulator, but that one can not run.

Learning quickly, and having working prototypes in a short amount of time are very valuable in a startup environment! So, good luck and have fun!



