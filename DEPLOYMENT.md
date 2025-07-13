# Deployment Guide

## Quick Deploy Commands

### Build Command:
```bash
./build.sh
```

### Start Command:
```bash
gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 300 --preload app:app
```

## Render.com Deployment

### Automatic Configuration
The project includes `render.yaml` for automatic deployment:

1. **Fork/Clone** this repository
2. **Connect** to Render.com
3. **Create Web Service** from repository
4. **Auto-deploy** with included configuration

### Manual Configuration
If you prefer manual setup:

- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 300 --preload app:app`
- **Environment:** Python 3.11
- **Health Check:** `/health`
- **Memory:** 1GB minimum recommended

## Environment Variables

### Required:
- `PORT` - Set automatically by Render

### Optional:
- `SESSION_SECRET` - Generated automatically
- `FLASK_ENV` - Set to `production`
- `PYTHON_VERSION` - Set to `3.11`

## Dependencies

### Core Framework:
- Flask 3.1.1
- Flask-CORS 6.0.1
- Gunicorn 23.0.0

### AI/Image Processing:
- rembg 2.0.59
- onnxruntime 1.19.2
- Pillow 11.3.0
- numpy 2.3.1
- opencv-python-headless 4.10.0.84
- scikit-image 0.24.0
- scipy 1.13.1

## Performance Settings

- **Workers:** 1 (due to memory requirements)
- **Timeout:** 300 seconds (for large image processing)
- **Memory:** 1-2GB recommended
- **Disk:** 2GB temporary storage

## Health Check

The API provides a health endpoint at `/health` that returns:

```json
{
  "service": "background-removal-api",
  "status": "healthy", 
  "version": "1.0.0"
}
```

## Troubleshooting

### Common Issues:

1. **Memory Errors**: Increase memory allocation to 1-2GB
2. **Timeout Errors**: Increase timeout to 300+ seconds
3. **Model Loading**: First request may take 10-30 seconds for model initialization
4. **Build Failures**: Ensure Python 3.11 is used and dependencies are compatible

### Logs to Check:
- Build logs for dependency installation issues
- Application logs for runtime errors
- Health check endpoint for service status

## Production Optimizations

1. **Preload Models**: Uses `--preload` flag for faster subsequent requests
2. **Optimized Dependencies**: Version-pinned for stability
3. **Memory Management**: Single worker to manage memory usage
4. **Error Handling**: Comprehensive error responses
5. **CORS**: Configured for web client access