# Allow public access to dashboards like Gamma user
PUBLIC_ROLE_LIKE = "Gamma"

# Enable embedded dashboards
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}

# Allow embedding in iframes by disabling X-Frame-Options
ENABLE_CORS = True

TALISMAN_CONFIG = {
    "content_security_policy": {
        "default-src": ["'self'", "*"],
        "script-src": ["'self'", "*", "'unsafe-inline'", "'unsafe-eval'"],
        "style-src": ["'self'", "*", "'unsafe-inline'"],
        "frame-ancestors": ["*"],  # Allow all iframe embedding
    },
    "force_https": False,
    "strict_transport_security": False,
    "frame_options": None,  # Disable X-Frame-Options header
}
