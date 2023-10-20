# rosbag_parqet

Python library for converting [ROS bagfiles](http://wiki.ros.org/rosbag) to [Parquet files](https://parquet.incubator.apache.org/) leveraging [Pandas dataframes](https://pandas.pydata.org/).


## Python library

```python
import rosbag_parquet

# Convert a ROSBag to a dataframe
dfs = rosbag_parquet.bag_to_dataframes('data/rosout.bag')
dfs_exclude = rosbag_parquet.bag_to_dataframes('data/example.bag', exclude=['/scan'])
dfs_include = rosbag_parquet.bag_to_dataframes('data/rosout.bag', include=['/rosout'])

# Select a dataframe key based on topic and (conform msgevalgen pattern http://docs.ros.org/api/rostopic/html/)
print(df['/rosout/header/stamp/secs'].to_string())

# Obtain possible ROS topics from a selection pattern (conform msgevalgen pattern http://docs.ros.org/api/rostopic/html/)
# This will return the possible topics: /pose, /pose/pose, /pose/pose/position
rosbag_parquet.topics_from_keys(["/pose/pose/position/x"])
```

## Key definition

Key definition conform the msgevalgen pattern http://docs.ros.org/api/rostopic/html/). Example:

```
/pose/pose/position/x
```

This will select the `/pose/position/x` property of topic `/pose` in the message of type http://docs.ros.org/api/geometry_msgs/html/msg/PoseStamped.html.

## Scripts

### bag_parquet

Convert a ROS bag file to a Parquet file:
```
usage: bag_parquet [-h] [-b BAG] [-i [INCLUDE [INCLUDE ...]]]
                   [-e [EXCLUDE [EXCLUDE ...]]] [-o OUTPUT] [-v]

Script to parse bagfile to parquet file

optional arguments:
  -h, --help            show this help message and exit
  -b BAG, --bag BAG     Bag file to read
  -i [INCLUDE [INCLUDE ...]], --include [INCLUDE [INCLUDE ...]]
                        List for topics to include
  -e [EXCLUDE [EXCLUDE ...]], --exclude [EXCLUDE [EXCLUDE ...]]
                        List for topics to exclude
  -o OUTPUT, --output OUTPUT
                        name of the output file
  -v, --verbose         Log verbose
```

### bag_csv

Convert a ROS bag file to a CSV file:
```
usage: bag_csv [-h] [-b BAG] [-i [INCLUDE [INCLUDE ...]]]
               [-e [EXCLUDE [EXCLUDE ...]]] [-o OUTPUT] [-v]

Script to parse bagfile to csv file

optional arguments:
  -h, --help            show this help message and exit
  -b BAG, --bag BAG     Bag file to read
  -i [INCLUDE [INCLUDE ...]], --include [INCLUDE [INCLUDE ...]]
                        List for topics to include
  -e [EXCLUDE [EXCLUDE ...]], --exclude [EXCLUDE [EXCLUDE ...]]
                        List for topics to exclude
  -o OUTPUT, --output OUTPUT
                        name of the output file
  -v, --verbose         Log verbose
```

### bag_plot

Plot a key (or multiple keys) in a ROS bag file:
```
usage: bag_plot [-h] -b BAG -k [KEY [KEY ...]] [-y  YLIM YLIM] [-c] [-v]

Bagfile key to graph

optional arguments:
  -h, --help            show this help message and exit
  -b BAG, --bag BAG     Bag file to read
  -k [KEY [KEY ...]], --key [KEY [KEY ...]]
                        Key you would like to plot
  -y  YLIM YLIM, --ylim YLIM YLIM
                        Set min and max y lim
  -c, --combined        Graph them all on one
  -v, --verbose         Log verbose
```

#### Example

```
bag_plot -b 2019-01-16-14-14-37.bag -k /cmd_vel/linear/x /cmd_vel/angular/z -c
```

![bag_plot](doc/bag_plot.png)

### bag_print

Print a key (or multiple keys) in a ROS bag file:
```
usage: bag_print [-h] -b BAG -k [KEY [KEY ...]] [-v]

Print one or multiple bag keys

optional arguments:
  -h, --help            show this help message and exit
  -b BAG, --bag BAG     Bag file to read
  -k [KEY [KEY ...]], --key [KEY [KEY ...]]
                        Key you would like to print
  -v, --verbose         Log verbose
```
