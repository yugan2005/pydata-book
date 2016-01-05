import numpy as np
from numpy.linalg import eigvals

def run_expreriment(niter=100):
    k =100
    results=[]
    for i in xrange(niter):
        mat = np.random.randn(k,k)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results

some_results = run_expreriment()
print 'Largest one we saw: %s' %np.max(some_results)
