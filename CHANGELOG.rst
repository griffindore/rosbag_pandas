^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package rosbag_parquet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.1.1 (2024-05-31)
------------------
* Improve timestamp datatype in parquet files

1.1.0 (2023-11-21)
------------------
* Disabled the progress bar by default in scripts and added a `-s`, `--show-progress` option to enable it.
* Added an optional `indexing_topic` parameter to `bag_to_dataframes` to specify the topic to use as an indexer for other topics.
  When set, an additional parquet file will be created that contains the row number of each topic at the time for each message of the indexer topic.
* Added an `-x`, `--indexing-topic` option to `bag_parquet` to specify the `indexing_topic` parameter.

1.0.0 (2023-10-20)
------------------
* Removed the copied versions of pathlib2 and flatten_dict and specified installation requirements in setup.py
* Changed `bag_to_dataframe` to `bag_to_dataframes`
  - Returns a dictionary of dataframes, 1 for each topic. Improves performance of creating the dataframe(s)
    and dataframes can be concatenated later with pandas improved performance for sparse data.
  - Added parameter to `exclude_strings` from being included in the dataframe
  - Added parameter to `flatten_lists` in the dataframe
  - Added parameter, `flatten_dict_sep`, to specify the separater used when flattening dict. Changed default from '/' to '.'

0.1.0 (2023-10-19)
------------------
* Fork rosbag_pandas from https://github.com/tsaoyu/rosbag_pandas
* Fixed numpy deprecation of np.object
* Add `bag_parquet` script
* Cleanup and reformat for setuptools, pytest, and flake8
* License maintained from fork: Apache 2.0
