^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package rosbag_parquet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
