#!/bin/bash
# Build script for Render deployment

echo "Starting build process..."

# Upgrade pip
pip install --upgrade pip

# Install core dependencies first
echo "Installing core dependencies..."
pip install flask==3.1.1
pip install flask-cors==6.0.1  
pip install gunicorn==23.0.0
pip install gevent==24.10.3

# Install image processing libraries
echo "Installing image processing libraries..."
pip install pillow==11.3.0
pip install numpy==2.3.1
pip install opencv-python-headless==4.10.0.84
pip install scikit-image==0.24.0
pip install scipy==1.13.1

# Install AI/ML libraries
echo "Installing AI/ML libraries..."
pip install onnxruntime==1.19.2
pip install rembg==2.0.59

echo "Build completed successfully!"