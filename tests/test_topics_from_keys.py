from rosbag_parquet.utils import topics_from_keys


def test_topics_from_keys():
    topics = topics_from_keys(["/pose/pose/position/x"])
    assert set(topics) == {'/pose', '/pose/pose', '/pose/pose/position'}
