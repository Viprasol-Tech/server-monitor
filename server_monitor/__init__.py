"""
server-monitor - Monitor server health and uptime

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ServerMonitor, monitor, process, main

__all__ = ["ServerMonitor", "monitor", "process", "main"]
