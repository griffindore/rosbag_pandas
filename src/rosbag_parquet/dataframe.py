#!/usr/bin/env python

import logging

import numpy as np
import pandas as pd
import rosbag
from flatten_dict import flatten
from tqdm import tqdm
from rospy_message_converter.message_converter import convert_ros_message_to_dictionary


class RosbagPandaException(Exception):
    pass


def bag_to_dataframes(bag_name, include=None, exclude=None, exclude_strings=False,
                      flatten_dict_sep=".", flatten_lists=False, show_progress=False):
    """
    Read in a rosbag file and create a pandas data frames for each topic
    that is indexed by the time the message was recorded in the bag.

    :param bag_name: String name for the bag file
    :param include: None, or List of Topics to include in the dataframe
    :param exclude: None, or List of Topics to exclude in the dataframe (only applies if include is None)
    :param exclude_strings: Exclude keys that have string types
    :param flatten_dict_sep: Separator for flattening the dictionary
    :param flatten_lists: Flatten lists to have a column per element
    :param show_progress: Show progress bar while reading bagfile

    :return: Dictionary of pandas DataFrames
    """
    logging.debug("Reading bag file %s", bag_name)

    bag = rosbag.Bag(bag_name)
    type_topic_info = bag.get_type_and_topic_info()
    topics = type_topic_info.topics.keys()

    # get list of topics to parse
    logging.debug("Bag topics: %s", topics)

    if not topics:
        raise RosbagPandaException("No topics in bag")

    topics = _get_filtered_topics(topics, include, exclude)
    logging.debug("Filtered bag topics: %s", topics)

    if not topics:
        raise RosbagPandaException("No topics in bag after filtering")

    data_dict = {topic: {'time': np.empty(type_topic_info.topics[topic].message_count, dtype=np.float64)}
                 for topic in topics}
    msg_count_dict = {topic: 0 for topic in topics}
    if show_progress:
        df_length = sum([type_topic_info.topics[t].message_count for t in topics])
        pbar = tqdm(total=df_length)
    for topic, msg, t in bag.read_messages(topics=topics):
        flattened_dict = _get_flattened_dictionary_from_ros_msg(msg, flatten_dict_sep)
        time = t.to_sec()
        curr_msg_count = msg_count_dict[topic]
        data_dict[topic]["time"][curr_msg_count] = time
        for key, item in flattened_dict.items():
            if flatten_lists and isinstance(item, list):
                keys = [key + f'_{i}' for i in range(len(key))]
                items = item
            else:
                keys = [key]
                items = [item]
            for key, item in zip(keys, items):
                if exclude_strings and isinstance(item, str):
                    continue
                if key not in data_dict[topic]:
                    item_type = type(item)
                    message_count = type_topic_info.topics[topic].message_count
                    if item_type not in [bool, int, float, np.float64, np.float32, np.bool_,
                                         np.int64, np.int32, np.int16, np.int8,
                                         np.uint64, np.uint32, np.uint16, np.uint8]:
                        logging.info(f"Topic '{topic}' key '{key}' is of type {item_type} and will be stored as object")
                        item_type = object
                    data_dict[topic][key] = np.empty(message_count, dtype=item_type)

                data_dict[topic][key][curr_msg_count] = item
        msg_count_dict[topic] += 1
        if show_progress:
            pbar.update(1)
    if show_progress:
        pbar.close()

    bag.close()
    dfs = {}
    for topic in topics:
        df = pd.DataFrame(data_dict[topic])
        df.name = topic
        dfs[topic] = df
    return dfs


def _get_flattened_dictionary_from_ros_msg(msg, sep="."):
    """
    Return a flattened python dict from a ROS message
    :param msg: ROS msg instance
    :return: Flattened dict
    """
    return flatten(convert_ros_message_to_dictionary(msg), reducer=lambda a, b: b if not a else a + sep + b)


def _get_filtered_topics(topics, include, exclude):
    """
    Filter the topics.
    :param topics: Topics to filter
    :param include: Topics to include if != None
    :param exclude: Topics to exclude if != and include == None
    :return: filtered topics
    """
    logging.debug("Filtering topics (include=%s, exclude=%s) ...", include, exclude)
    return ([t for t in include if t in topics] if include is not None
            else [t for t in topics if t not in exclude] if exclude is not None else topics)
