__author__ = 'Theodoros Malikourtis & Georgios Artopoulos'

from mrjob.job import MRJob
import math


class KMeans(MRJob):

    def configure_args(self):
        super(KMeans, self).configure_args()
        self.add_passthru_arg('--centers', help='Comma-separated list of centers')

    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def mapper_init(self):
        # Load the centers and convert then to floats
        self.centers = []
        center_strings = self.options.centers.split(',')
        for i in range(0, len(center_strings), 2):
            self.centers.append((float(center_strings[i]), float(center_strings[i + 1])))


    def mapper(self, _, line):
        # Parse the data point from the input line
        x, y = map(float, line.strip().split(','))

        # Find the closest center to the data point
        closest_center = None
        closest_distance = float('inf')
        for center in self.centers:
            distance = self.euclidean_distance((x, y), center)
            if distance < closest_distance:
                closest_center = center
                closest_distance = distance

        # Output the closest center and the data point
        yield closest_center, (x, y)

    def reducer(self, center, points):
        # Compute the new center for the list of data points
        num_points = 0
        sum_x = 0
        sum_y = 0
        for point in points:
            num_points += 1
            sum_x += point[0]
            sum_y += point[1]
        new_center = (sum_x / num_points, sum_y / num_points)

        # Output the new center
        yield center, new_center
