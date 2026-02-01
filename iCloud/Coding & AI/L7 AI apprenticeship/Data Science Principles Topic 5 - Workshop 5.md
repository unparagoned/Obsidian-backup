Hadoop is an ETL platform

One of the first frameworks that structures the data and processed in distributed, manageable way .

Data lake can store big data of any format

Date warehouse store structured data.

## What is Big data

Big data is data that is too big or too complex to be processed by traditional means. Usually tera or petabytes

Big five Vs of Big data

1. Volume
2. Variety of data(structured, unstructured, etc.)
3. Velocity: Speed the data is generated
4. Veracity: Degree the data can be trusted
5. Value: The business value of the data

## Explain main principles behind Hadoop

Apache Hadoop is an open source software framework for storing and processing big data.

It has the following :

- Distributed storage. More storage can be added offering scalability.
- Distributed processing.
- Resilience. If a node fails, the cluster can recover.
- Parallel processing. Implements MapReduce, which can split data into chunks and run the chunks in parallel.

The core components are

- Hadoop Distributed File System(HDFS). Files are split into blocks and distributed across multiple nodes in a cluster.
- MapReduce. Tasks are split up into sub tasks(Map) that can be executed in parallel across different nodes. Then they are combined for the final output(Reduce).
- YARN. A resource manager.
- Hadoop Common. Libraries and utilities.

Can be run on a variety of hardware, rather than relying on expensive specialised machines.

Process

- Data ingestion.
- Data storage. HDFS.
- Data processing. YARN allocates resources and tasks is run using MapReduce framework.
- Data Retrieval and analysis. Results can be stored in HDFS for further analysis.

Spark is a faster than MapReduce and is commonly used.

##  How does the move to cloud storage impact on Hadoop

If you are using s3 or other cloud storage you can still run Spark over the data, but the processing isn't done locally, it's done by the spark cluster.

Amazon EMR(Elastic MapReduce) allows you to use Hadoop. Uses HDFS on EC2 instances, integrated with S3. 

# Activity 2

Company Accounts(Semi structured and unstructured data) -> data lake -> Spark -> data mart -> BI and other analytics