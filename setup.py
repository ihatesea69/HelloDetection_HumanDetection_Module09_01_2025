from setuptools import setup, find_packages

setup(
    name='HumanWaveDetector',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
    ],
    description='A Python application for live camera overlay with hand and pose detection.',
    author='HUFLIT Tinh Hoa',
    author_email='hieunghiwork123@gmail.com',
    url='https://github.com/ihatesea69/HumanWaveDetector',  # Replace with your GitHub repo link
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
