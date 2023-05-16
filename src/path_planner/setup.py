from setuptools import setup

package_name = 'path_planner'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
install_requires=['setuptools'],
zip_safe=True,
maintainer='Your Name',
maintainer_email='you@example.com',
description='Path planning package for car racing',
license='Apache License 2.0',
tests_require=['pytest'],
entry_points={
'console_scripts': [
'planner_node = path_planner.planner_node:main',
],
},
)