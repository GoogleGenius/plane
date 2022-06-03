from __future__ import annotations

__all__: tuple[str, ...] = ("Users",)

from plane.api.models import (
    GetUserResponse,
    GetPronounsResponse,
    GetBansResponse,
    GetWhitelistsResponse,
    GetReputationResponse,
)
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class Users(HTTPAwareEndpoint):
    """The implementation class for requests to the `users` route."""

    @with_permission_check("users")
    async def get_user(self: HTTPAwareEndpoint, user_id: int) -> GetUserResponse:
        """Get extensive user information.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetUserResponse
            The response from the API.
        """
        if not isinstance(user_id, int):
            raise ValueError('Parameter "user_id" must be of "int" or derivative type')

        return GetUserResponse(
            await self._http.get(self._http.paths.users(user_id).route)
        )

    @with_permission_check("users.pronouns")
    async def get_pronouns(
        self: HTTPAwareEndpoint, user_id: int
    ) -> GetPronounsResponse:
        """Get pronouns.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetPronounsResponse
            The response from the API.
        """
        if not isinstance(user_id, int):
            raise ValueError('Parameter "user_id" must be of "int" or derivative type')

        return GetPronounsResponse(
            await self._http.get(self._http.paths.users(user_id).pronouns)
        )

    @with_permission_check("users.bans")
    async def get_bans(self: HTTPAwareEndpoint, user_id: int) -> GetBansResponse:
        """Get bans.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetBansResponse
            The response from the API.
        """
        if not isinstance(user_id, int):
            raise ValueError('Parameter "user_id" must be of "int" or derivative type')

        return GetBansResponse(
            await self._http.get(self._http.paths.users(user_id).bans)
        )

    @with_permission_check("users.whitelists")
    async def get_whitelists(
        self: HTTPAwareEndpoint, user_id: int
    ) -> GetWhitelistsResponse:
        """Get whitelists.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetWhitelistsResponse
            The response from the API.
        """
        if not isinstance(user_id, int):
            raise ValueError('Parameter "user_id" must be of "int" or derivative type')

        return GetWhitelistsResponse(
            await self._http.get(self._http.paths.users(user_id).whitelists)
        )

    @with_permission_check("users.rep")
    async def get_reputation(
        self: HTTPAwareEndpoint, user_id: int
    ) -> GetReputationResponse:
        """Get reputation.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetReputationResponse
            The response from the API.
        """
        if not isinstance(user_id, int):
            raise ValueError('Parameter "user_id" must be of "int" or derivative type')

        return GetReputationResponse(
            await self._http.get(self._http.paths.users(user_id).reputation)
        )
