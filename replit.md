# Background Removal API - System Documentation

## Overview

This is a Flask-based web API that provides background removal functionality for images. The service offers multiple background replacement options including transparent backgrounds, solid colors, and custom background images. The application is designed as a stateless REST API with comprehensive error handling and deployment-ready configuration.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask with Python 3.11+
- **API Style**: RESTful HTTP endpoints with CORS enabled
- **Web Server**: Gunicorn for production deployment
- **File Handling**: Temporary file storage using Python's `tempfile` module
- **Image Processing**: PIL (Pillow) for image manipulation with custom background removal algorithms
- **Database**: PostgreSQL support configured (via psycopg2-binary) though not actively used in current implementation

### Key Design Decisions
- **Stateless Design**: No persistent storage - files are processed and cleaned up immediately to avoid storage overhead
- **In-Memory Processing**: Uses temporary files for processing to eliminate persistent storage requirements
- **Multiple Processing Implementations**: Includes both alternative (PIL-based) and improved background removal implementations
- **Cloud-Ready**: Pre-configured for Render.com deployment with zero configuration required

## Key Components

### Core Application Files
- `app.py`: Main Flask application with route definitions, CORS configuration, and request handling
- `main.py`: Application entry point that configures host, port, and debug settings
- `improved_bg_remover.py`: Advanced background removal using edge detection and color analysis
- `alternative_bg_remover.py`: Fallback PIL-based background processing implementation
- `image_processor.py`: Original rembg-based implementation (currently disabled due to compatibility)
- `utils.py`: Utility functions for file validation, hex color validation, and security

### Main Classes
- **ImprovedBackgroundRemover**: Handles advanced background removal using image processing algorithms
- **AlternativeBackgroundRemover**: Basic fallback implementation using PIL filters
- **BackgroundRemover**: Original rembg-based processor (disabled)

### API Endpoints
- `/health`: Health check endpoint for monitoring and load balancer integration
- File upload endpoints for background removal operations (implementation in progress)

### Key Features
- Multiple background replacement options (transparent, solid color, image replacement)
- File validation (type, size, format checking)
- Secure filename handling with sanitization
- Comprehensive logging and error handling
- Image size optimization for performance

## Data Flow

1. **Image Upload**: Client uploads image via HTTP POST request
2. **Validation**: File undergoes validation for type, size, and format compliance
3. **Processing**: Image is processed through background removal algorithms:
   - Load and optionally resize image for performance
   - Apply advanced edge detection and color analysis
   - Generate subject mask and apply background replacement
4. **Response**: Processed image is returned to client
5. **Cleanup**: Temporary files are automatically cleaned up

## External Dependencies

### Core Dependencies
- **Flask 3.1.1**: Web framework for API endpoints
- **Flask-CORS 6.0.1**: Cross-origin request handling
- **Pillow 11.3.0**: Image processing and manipulation
- **NumPy 2.3.1**: Numerical operations for image arrays
- **Gunicorn 23.0.0**: Production WSGI server

### Database Support
- **psycopg2-binary 2.9.10**: PostgreSQL adapter (configured but not actively used)
- **Flask-SQLAlchemy 3.1.1**: ORM support for potential future database integration

### Validation
- **email-validator 2.2.0**: Input validation utilities
- **Werkzeug 3.0.3**: Security utilities and file handling

## Deployment Strategy

### Render.com Deployment (Zero Configuration)
The application includes complete deployment automation:

- **render.yaml**: Full Render.com service configuration with auto-detection
- **runtime.txt**: Python 3.11 version specification
- **requirements.txt**: Exact package versions for reproducible builds
- **DEPLOYMENT_READY.md**: Complete deployment guide with step-by-step instructions

### Build Process
- Automatic Python environment detection
- Dependency installation from pinned versions
- Health check configuration for monitoring
- Scaling and resource allocation settings

### Production Configuration
- **Environment Variables**: Configurable session secrets and port settings
- **Proxy Support**: ProxyFix middleware for proper header handling behind load balancers
- **CORS**: Configured for cross-origin requests from any domain
- **File Size Limits**: 10MB maximum file size with proper validation
- **Logging**: Comprehensive debug logging for troubleshooting

The application is designed to be deployment-ready with minimal configuration, making it suitable for cloud platforms like Render.com, Heroku, or similar PaaS providers.

## Recent Changes: Latest modifications with dates
- July 13, 2025: Background removal API successfully running on port 5000 with rembg integration
- Modified app.py to use rembg instead of manual background removal implementation
- Created MinimalBackgroundRemover with lazy initialization to avoid startup delays
- Dependencies installed: Flask, Flask-CORS, Pillow, NumPy, rembg, onnxruntime, and supporting libraries
- Health check endpoint confirmed working at /health ✅
- API ready for background removal requests at /remove-background ✅
- Supports transparent, solid color, and image backgrounds ✅

- API tested with user's image - processing works but takes time due to model initialization
- Project cleaned up and optimized for deployment ✅
- Removed unnecessary files and consolidated utility functions into app.py
- Updated render.yaml with proper build and start commands for Render.com deployment
- Created build.sh script with version-pinned dependencies for compatibility
- Added Procfile for deployment flexibility
- Updated README.md with deployment instructions