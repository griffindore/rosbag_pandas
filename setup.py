from setuptools import setup, find_packages


def read_requirements(filename):
    with open(filename) as f:
        requirements = []
        for line in f:
            line = line.strip()
            if line.startswith("-r"):
                requirements.extend(read_requirements(line[2:].strip()))
            elif not line.startswith("#"):
                requirements.append(line.strip())
        return requirements


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='rosbag_parquet',  # 'rosbag_pandas' and 'rosbags-dataframe' are taken
    version='1.1.1',
    description='ROS bag to parquet converter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/griffindore/rosbag_parquet',
    author='Mike Lyons',
    license='Apache 2.0',
    scripts=['scripts/bag_parquet', 'scripts/bag_csv', 'scripts/bag_plot', 'scripts/bag_print'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.11',
    install_requires=read_requirements('requirements.txt'),
    zip_safe=False,
)
