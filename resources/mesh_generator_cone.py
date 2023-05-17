from resources import constants as c
import numpy as np


def generate_square_su2_file_mesh(r_min, r_maj, d, b_d, W, D, a, b):
    # control mesh-boundary dimensions here

    # mesh finesse here


    # form factor
    beta = float(r_maj / r_min)
    # x mesh division length
    dx = float(0.5 * r_min / (a * beta))
    # y mesh division length
    dy = float(d / b)
    # distance from base of the cone to the wall

    # triangle mesh-element reference
    t_r = "5"

    # line mesh-element reference
    l_r = "3"

    # number of points
    nx = (2*a * beta**2 + a * beta * W) * 2 + 1 ##base cone + distancia a fronteira * 2 (simetria) + 1 (centro)
    ny = b * (b_d + 1. + D) + 1  # back of mesh to base + cone + D
    nt = nx * ny
    total_nodes = (nx - 1) * 2 * (ny - 1)

    with open(c.OUTPUT_FILE_PATH + c.OUTPUT_SU2_SQ_MESH_FILE_NAME, 'w') as f:

        # generate mesh configs and points from left-right, bottom-top
        #f.write("nx= " + str(nx) + "ny= " + str(ny) + "\n")

        f.write("NDIME= " + str(int(c.DIM)) + "\n")
        f.write("NPOIN= " + str(int(nt)) + "\n")
        k = 0
        for y in np.arange(-(b_d +.5) * d, d / 2. + d * D + dy, dy):
            for x in np.arange(-r_maj - 0.5 * r_min * W, r_maj + 0.5 * r_min * W + dx, dx):
                #f.write(str(k) + " " + str(x) + " " + str(y) + "\n")
                k+=1
                #f.write(str(x) + "\t" + str(y) + "\t " + str(int(k-1)) + "\n")
                f.write( "%s \t %s \t %s\n" % (str(x), str(y), int(k-1)) )

        # generate nodes
        f.write("NELEM= " + str(int(total_nodes)) + "\n")
        #f.write("nt - nx - 1= " + str(nt - nx - 1) + "\n")

# For some reason this triangle-node generation didnt work properly with the SU2. After some debugging,
# I don't have time, knowledge, nor proper docs available to understand exactly what happened, whether it is a bug
# or a mesh problem. So I will leave it here for further analysis.
# error: The surface element (0, 0) doesn't have an associated volume element
 #       j = 0
  #      k = 0
   #     while j < nt - nx:
    #        i = j
     #       if k != 0:
      #          k += 1

       #     f.write(t_r + "\t" + str(int(i)) + "\t" + str(int(i + 1)) + "\t" + str(int(i + nx)) + "\t" + str(k) + "\n")

        #    i += 1

         #   while i < nx + j - 1:
          #      k += 1
           #     f.write(t_r + "\t" + str(int(i)) + "\t" + str(int(i + nx - 1)) + "\t" + str(int(i + nx)) + "\t" + str(k) + "\n")

            #    k += 1
             #   f.write(t_r + "\t" + str(int(i)) + "\t" + str(int(i + 1)) + "\t" + str(int(i + nx)) + "\t" + str(k) + "\n")
              #  i = i + 1

           # k += 1
           # f.write(t_r + "\t" + str(int(i)) + "\t" + str(int(i + nx - 1)) + "\t" + str(int(i + nx)) + "\t" + str(k) + "\n")
           # j += nx

        # generate nodes

        # Write the element connectivity
        iElem = 0
        for jNode in range(int(ny)-1):
             for iNode in range(int(nx)-1):
                iPoint = jNode*nx + iNode
                jPoint = jNode*nx + iNode + 1
                kPoint = (jNode + 1)*nx + iNode
                f.write( "%s \t %s \t %s \t %s \t %s\n" % (t_r, int(iPoint), int(jPoint), int(kPoint), iElem) )
                iElem = iElem + 1
                iPoint = jNode*nx + (iNode + 1)
                jPoint = (jNode + 1)*nx + (iNode + 1)
                kPoint = (jNode + 1)*nx + iNode
                f.write( "%s \t %s \t %s \t %s \t %s\n" % (t_r, int(iPoint), int(jPoint), int(kPoint), iElem))
                iElem = iElem + 1

        #mesh with square elements
        #iElem = 0
        #for jnode in range (int(ny)-1):
         #   for inode in range(int(nx-1)):
          #      iPoint = jnode*nx + inode
           #     jPoint = iPoint + 1
            #    kPoint = jPoint + nx
             #   lPoint = kPoint - 1
              #  f.write( "%s \t %s \t %s \t %s \t %s \t %s\n" % ("9", int(iPoint), int(jPoint), int(kPoint), int(lPoint), iElem))
               # iElem+=1



        f.write("NMARK= 2\n")


        # Write the boundary information for each marker
        #f.write( "MARKER_TAG= farfieldlower\n" )
        #f.write( "MARKER_ELEMS= %s\n" % int(nx-1))
        #for iNode in range(int(nx)-1):
         #   f.write( "%s \t %s \t %s\n" % (l_r, iNode, iNode + 1) )
        #f.write( "MARKER_TAG= farfieldright\n" )
        #f.write( "MARKER_ELEMS= %s\n" % int(ny-1))
        #for jNode in range(int(ny)-1):
         #   f.write( "%s \t %s \t %s\n" % (l_r, int(jNode*nx + (nx - 1)),  int((jNode + 1)*nx + (nx - 1)) ) )
        f.write( "MARKER_TAG= farfieldupper\n" )
        f.write( "MARKER_ELEMS= %s\n" % int((nx-1)))
        for iNode in range(int(nx)-1):
            f.write( "%s \t %s \t %s\n" % (l_r, int((nx*ny - 1) - iNode), int((nx*ny - 1) - (iNode + 1))) )
        #f.write( "MARKER_TAG= farfieldleft\n" )
        #f.write( "MARKER_ELEMS= %s\n" % (int(ny)-1))
        #for jNode in range(int(ny)-2, -1, -1):
        #    f.write( "%s \t %s \t %s\n" % (l_r, int((jNode + 1)*nx), int(jNode*nx) ) )

        #f.write( "MARKER_TAG= inlet\n" )
        #f.write( "MARKER_ELEMS= %s\n" % int(int(nx)-1-2*a * beta ** 2))
        #for iNode in range(int(a * beta ** 2), int(nx)-1-int(a * beta ** 2)):
        #   f.write( "%s \t %s \t %s\n" % (l_r, int((nx*ny - 1) - iNode ), int((nx*ny - 1) - (iNode + 1) )) )

        #f.write( "MARKER_TAG= sym\n" )
        #f.write( "MARKER_ELEMS= %s\n" % int(ny-1))
        #for jNode in range(int(ny)-1):
        #    f.write( "%s \t %s \t %s\n" % (l_r, int(jNode*nx + (nx - 1)/2),  int((jNode + 1)*nx + (nx - 1)/2) ) )


        # generate cone

        cnt=1
        for jnode in range(0, b+1):
            lower_left = int(nx * (b_d*b+jnode) + 0.5 * (nx - 1) - a * beta ** 2 + 1 - 1)+jnode
            lower_right = int(lower_left + 2*a * beta ** 2) -2*jnode
            for inode in range(lower_left, lower_right, 1):
                cnt+=1

        f.write("MARKER_TAG= cone\n")
        #f.write("MARKER_ELEMS= %s\n" % int(cnt-1))

        cone_grid = []
        for jnode in range(0, b+1):
            lower_left = int(nx * (b_d*b+jnode) + 0.5 * (nx - 1) - a * beta ** 2 + 1 - 1)+jnode
            lower_right = int(lower_left + 2*a * beta ** 2) -2*jnode
            for inode in range(lower_left, lower_right, 1):
                #f.write( "%s \t %s \t %s \t %s\n" % (t_r, int(inode), int(inode+1), int(inode+nx) ) )
                #f.write( "%s \t %s \t %s\n" % (l_r, int(inode), int(inode+1)) )
                cone_grid.append(int(inode))
                cone_grid.append(int(inode+1))

        # TODO: Sorry, I was tired and didnt want to think about more point calculations
        cnt=0
        for jnode in range(0, int(ny)):
            for inode in range(0, int(nx-1)):
                node=jnode*nx + inode
                if(node not in cone_grid):
                    cnt+=1
        f.write("MARKER_ELEMS= %s\n" % int(cnt))


        for jnode in range(0, int(ny)):
            for inode in range(0, int(nx-1)):
                node=jnode*nx + inode
                if(node not in cone_grid):
                    f.write( "%s \t %s \t %s\n" % (l_r, int(node), int(node+1)) )

        f.close()