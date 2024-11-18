import math

points = [(2, 3), (3, 5), (5, 7), (6, 2)]

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

min_distance = min(distances)

print("Öklid mesafeleri:", distances)
print("Minimum mesafe:", min_distance)