#!/usr/bin/env python3
"""
Auth
"""


from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require authentication
        """
        return False


    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None
