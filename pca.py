import numpy as np

class PCA:
    def __init__(self,n_components=2):
        self.dim = n_components

    def fit(self,X):
        self.X = X
        self.mean = np.mean(X,axis = 0)
        self.X_norm = X - self.mean[np.newaxis,:]
        covariances = np.cov(self.X_norm,rowvar=0)
        eigenval, eigenvec = np.linalg.eigh(covariances)
        inds = np.argsort(eigenval)[::-1]
        eigenval = eigenval[inds]
        eigenvec = eigenvec[:,inds]
        self.allcomponents = eigenval
        self.principal_components = eigenvec[:,:self.dim]

    def transform(self):
        self.X_reduced = np.array(np.dot(self.principal_components.T,self.X_norm.T).T)
        return self.X_reduced

    def checkPCA(self):
        reconstructed = np.dot(self.X_reduced,self.principal_components.T)
        reconstructed += self.mean[np.newaxis,:]
        reconstruction_error = np.mean(np.abs(self.X - reconstructed))
        print(f"Reconstruction error = {reconstruction_error}")
        return reconstruction_error<=0.5

    def Scree(self):
        self.cumulative_components = np.cumsum(self.allcomponents)/np.sum(self.allcomponents)
        return self.cumulative_components