"""
PhyTrade: Institutional Physics-Based Settlement Engine
Standardizing global trade arbitration through objective computational models.
"""

__version__ = "1.2.7"
__author__ = "Kazi Saad Asif"

# This file is intentionally left lean to prevent circular dependency 
# deadlocks. By not importing 'Engine' or 'Schema' here, we allow 
# the interpreter to load sub-modules independently.
