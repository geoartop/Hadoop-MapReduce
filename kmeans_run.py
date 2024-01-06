__author__ = 'Theodoros Malikourtis & Georgios Artopoulos'

import sys

from kmeans_job import KMeans

if __name__ == '__main__':

    centers = "0,1,4,5,7,8"

    mr_job = KMeans(args=[sys.argv[1], '--centers=' + centers])

    # Run the job once to get the initial centers
    with mr_job.make_runner() as runner:
        runner.run()

    # Iterate until the centers have converged
    converged = False
    while not converged:

        # Run the job with the current centers
        mr_job = KMeans(args=[sys.argv[1], '--centers=' + centers])
        with mr_job.make_runner() as runner:
            runner.run()

            # Load the new centers from the reducer output
            new_centers = []
            for key, value in mr_job.parse_output(runner.cat_output()):
                new_centers.append(value)
            # Convert new_centers to a string
            new_centers2 = ",".join([str(y) for x in new_centers for y in x])
            # Check for convergence
            if centers == new_centers2:
                converged = True

            centers = new_centers2

    print(new_centers)
