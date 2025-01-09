from setuptools import setup, find_packages

setup(
    name='CameraOverlayStream',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
    ],
    description='A Python application for live camera overlay with hand and pose detection.',
    author='HUFLIT Tinh Hoa',
    author_email='your.email@example.com',
    url='https://github.com/your-repo/CameraOverlayStream',  # Replace with your GitHub repo link
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
