import numpy as np

points = {
    "A": np.array([2, 3]),
    "B": np.array([3, 4]),
    "C": np.array([6, 6]),
    "D": np.array([7, 7])
}

centroid1 = points["A"]
centroid2 = points["C"]

def ed(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

while True:
    cluster1 = []
    cluster2 = []

    for name, point in points.items():
        d1 = ed(point, centroid1)
        d2 = ed(point, centroid2)

        if d1 < d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    old_c1 = centroid1.copy()
    old_c2 = centroid2.copy()

    centroid1 = np.mean(cluster1, axis=0)
    centroid2 = np.mean(cluster2, axis=0)

    if np.allclose(old_c1, centroid1) and np.allclose(old_c2, centroid2):
        break

print("Final Clusters:")
print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print("Final Centroid1:", centroid1)
print("Final Centroid2:", centroid2)