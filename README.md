# Assignment #2 MapReduce for the Big Data Management Systems course

In this project you will implement the first iteration of K-Means clustering algorithm in MapReduce and
apply it on synthetic data that you will create.
1. Install Hadoop (e.g. Cloudera distribution)
2. Create using whatever language you want a very large text file, containing at least 1M data
points in the form of (x, y), where x and y are real numbers. The generation of should be biased
toward the creation of three clusters. In other words, choose a-priori three centers (x1,y1),
(x2,y2) and (x3,y3) and generate the rest of the data points around these, using some random
distance following a skewed distribution (towards 0)
3. Move your file to HDFS
4. Write a MapReduce job that distributes the centers you have chosen at Step 2, (x1,y1), (x2,y2)
and (x3,y3) to all mappers and reads in the file that you have created in Step 2 and maps each
pair to the closest center. Reduce function should compute the new center for each constructed
list. All distances are Euclidean. This is the iteration step in K-means algorithm.
5. Now implement the full K-means algorithm (stop when centers are close enough to previous
step).




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
