import numpy as np

class PointCloud():
    def __init__(self, n_samples = 1000, n_points = 'random', manifolds=['sphere'],  noise = 5.0):
        self.n_samples = n_samples
        self.n_points = n_points
        self.noise = noise

    def sphere(self):        
        '''
        Generate point cloud examples.
        '''
        data = []

        for _ in range(self.n_samples):
            if self.n_points == 'random':
                n_points = np.random.randint(1000,2000,1)[0]
            
            sample = np.zeros([n_points, 3])
            
            # domain of parameters
            t = np.random.uniform(0, 1*np.pi, n_points)
            s = np.random.uniform(0, 2*np.pi, n_points)
        
            # parametric equation of sphere
            sample[:, 0] = np.cos(s)*np.sin(t)   # x
            sample[:, 1] = np.sin(s)*np.sin(t)   # y
            sample[:, 2] = np.cos(t)             # z

            # random noise
            noise = np.random.normal(0, self.noise, size=sample.shape)
            data.append(sample + noise)
        return data

    def torus(self):
        '''
        Generate point cloud examples.
        '''
        data = []

        for _ in range(self.n_samples):
            if self.n_points == 'random':
                n_points = np.random.randint(1000,2000,1)[0]
            
            sample = np.zeros([n_points, 3])
            
            # domain of parameters
            t = np.random.uniform(0, 2*np.pi, n_points)
            s = np.random.uniform(0, 2*np.pi, n_points)
        
            # parametric equation of sphere
            sample[:, 0] = (2*np.cos(s)+4)*np.cos(t)   # x
            sample[:, 1] = (2*np.cos(s)+4)*np.sin(t)   # y
            sample[:, 2] = 2*np.sin(s)             # z

            # random noise
            noise = np.random.normal(0, self.noise, size=sample.shape)
            data.append(sample + noise)
        return data