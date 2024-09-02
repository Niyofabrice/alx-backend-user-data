#!/usr/bin/env python3
"""
Auth
"""


from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require authentication
        Returns:
            True: if the path is not in the list of strings excluded_paths
        """
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path not in excluded_paths:
            return True
        return False


    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        if request is not None:
            return request.headers.get("Authorization")
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None
