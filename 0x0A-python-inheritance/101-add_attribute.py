#!/usr/bin/python3
"""attribute add"""

def add_attribute(pObject, pName, pValue):
    """add att"""
    if not hasattr(pObject, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(pObject, pName)):
        pObject.__setattr__(pName, pValue)
