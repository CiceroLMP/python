from .authController import auth_bp
from .dashboardController import dashboard_bp
from .restController import rest_bp
from .api import api_v1_bp

__all__ = ["auth_bp", "dashboard_bp", "rest_bp", "api_v1_bp"]
