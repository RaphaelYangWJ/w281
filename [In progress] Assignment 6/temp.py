def plot_save_sphere(X,Y,Z,C,out_file):
    # write a function that takes the 
    # X,Y,Z and I NumPy array files as arguments,
    # plots the sphere,
    # then saves the figure to the out_file

    # display the sphere
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X,Y,Z, facecolors = C)
    ax.grid(False)
    ax.set_xticks([]) 
    ax.set_yticks([]) 
    ax.set_zticks([]) 
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    # plot and save the deliverable 
    plt.title('Plot the Sphere')
    plt.tight_layout(pad=5.08, h_pad=None, w_pad=None, rect=None)
    plt.savefig(out_file, bbox_inches='tight')
    plt.show()

    pass

def compute_normals(X,Y,Z):
    
    N = np.zeros((41*41, 3)) # your code should fill in the values for sphere normals
    
    # write a function that takes the 
    # X,Y,Z array files as arguments,
    # each input is of size (41, 41)
    # output N of size (41*41, 3)
    
    # TODO: vectorize the inputs to (41*41, 1)
    X = X.flatten()[:,np.newaxis]
    Y = Y.flatten()[:,np.newaxis]
    Z = Z.flatten()[:,np.newaxis]
    # TODO compute the normal at each point on the sphere
    N_normal = np.hstack([X,Y,Z])
    # TODO calculate the 2-norm of each normal
    N_2_norm = np.sqrt(N_normal[:,0]**2 + N_normal[:,1]**2 + N_normal[:,2]**2)[:,np.newaxis]
    # TODO divide each Normal by its norm
    N = N_normal / N_2_norm
    return N




# TODO calculate light direction using least squares
# vectorize I 
# consider only those points which are not in shadow
# solve for the light direction using least squares, remember I = N . l where l is the light direction

I = I.flatten()[:,np.newaxis]
I_filter = np.argwhere(I)
print(N.shape)
print(I_filter.shape)
# N_inv = N

# print the light direction
# print(l)
