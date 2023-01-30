from setuptools import setup, find_namespace_packages

setup(
    name='Clean Folder',
    version='0.0.1',
    description='Clean folder',
    author='Kostiantyn Liapkalo',
    author_email='kostiantynliapkalo@gmail.com',
    license='MIT',
    url='https://github.com/Kostiantyn-Liapkalo/Garbage-sorting',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'startclean=clean_folder.sort_files:run']}
)
