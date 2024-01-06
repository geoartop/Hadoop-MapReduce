# Assignment #2 MapReduce for the Big Data Management Systems course

## Authors: Theodoros Malikourtis(8200097) & Georgios Artopoulos(8200016)

### Contents

- datagenerator.py : The python script that generates a data.txt file a set of more than one million data points to
be used later as an input for the k-means clustering algorithm.
- kmeans_job.py : The python script that contains the MapReduce job that performs the k-means clustering algorithm.
- kmeans_run.py : The python script that iteratively runs the k-means clustering algorithm on the data.txt file and contains the main method.

### How to run
-Note: To change the centers of the clusters you need to modify the code in the datagenerator.py script by replacing the centers variable with your own centers
and in the kmeans_job.py script by replacing the centers with your own centers in this style: centers = "0,1,2,3,4,5" if your centers
are (0,1), (2,3) and (4,5).

- Run the datagenerator.py script to generate the data.txt file.
- Transfer the data.txt file to the HDFS.
- Transfer the kmeans_job.py and kmeans_run.py files to the HDFS.
- Run the kmeans_run.py script to run the k-means clustering algorithm on the data.txt file using the command
`python kmeans_run.py data.txt -r hadoop`
- The output of the k-means clustering algorithm will be printed in the terminal.
- Note: ignore the warnings that appear in the terminal.
