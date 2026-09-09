"""
This list contains the blocklist of the JWT tokent. It will be imported by app and 
the logout resource so that tokens can be added to blocklist when the user logs out.
"""

BLOCKLIST = set()
