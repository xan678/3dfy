# uvicorn_config.py

# Host and port configuration
host = "127.0.0.1"
port = 8000

# Set the log level
log_level = "info"

# Enable/Disable access logs
access_log = True

# Enable/Disable reloading (useful for development)
reload = True

# Specify the application instance
app = "appserver.main:app"
