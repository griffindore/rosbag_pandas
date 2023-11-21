import rosbag_parquet


def test_numbers_3_4():
    dfs = rosbag_parquet.bag_to_dataframes('tests/data/rosout.bag')
    assert set(dfs['/rosout']) == {'file', 'function', 'header.frame_id', 'header.seq',
                                   'header.stamp.nsecs', 'header.stamp.secs', 'level',
                                   'line', 'msg', 'name', 'time', 'topics'}
