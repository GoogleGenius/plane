# Copyright 2022-Present GoogolGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Implementations for the `users` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("Users",)

from ravyapi.api.models import (
    BanEntryRequest,
    GetBansResponse,
    GetPronounsResponse,
    GetReputationResponse,
    GetUserResponse,
    GetWhitelistsResponse,
)
from ravyapi.http import HTTPAwareEndpoint
from ravyapi.utils import with_permission_check


class Users(HTTPAwareEndpoint):
    """A class with implementations for the `users` endpoint."""

    __slots__: tuple[str, ...] = ()

    @with_permission_check("users")
    async def get_user(self: HTTPAwareEndpoint, user_id: int) -> GetUserResponse:
        """Get extensive user information.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Raises
        ------
        TypeError
            If any parameters are of invalid types.

        Returns
        -------
        GetUserResponse
            A model response from `ravyapi.api.endpoints.users.Users.get_user`.
            Located as `ravyapi.api.models.users.GetUserResponse`.
        """
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

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

        Raises
        ------
        TypeError
            If any parameters are of invalid types.

        Returns
        -------
        GetPronounsResponse
            A model response from `ravyapi.api.endpoints.users.Users.get_pronouns`.
            Located as `ravyapi.api.models.users.GetPronounsResponse`.
        """
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

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

        Raises
        ------
        TypeError
            If any parameters are of invalid types.

        Returns
        -------
        GetBansResponse
            A model response from `ravyapi.api.endpoints.users.Users.get_bans`.
            Located as `ravyapi.api.models.users.GetBansResponse`.
        """
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        return GetBansResponse(
            await self._http.get(self._http.paths.users(user_id).bans)
        )

    @with_permission_check("admin.bans")
    async def add_ban(
        self: HTTPAwareEndpoint,
        user_id: int,
        *,
        provider: str,
        reason: str,
        moderator: int,
        reason_key: str | None = None,
    ) -> None:
        """Add ban.

        Parameters
        ----------
        user_id : int
            User ID of the user to ban.
        provider : str
            Source for where the user was banned.
        reason : str
            Why the user was banned.
        moderator : int
            User ID of the responsible moderator, usually Discord.
        reason_key : str | None
            Machine-readable version of the reason - only present for providers ravy and dservices.

        Raises
        ------
        TypeError
            If any parameters are of invalid types.
        ValueError
            If any parameters are invalid values.
        """
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        if not isinstance(provider, str):
            raise TypeError('Parameter "provider" must be of type "str"')

        if not provider:
            raise ValueError('Parameter "provider" must not be empty')

        if not isinstance(reason, str):
            raise TypeError('Parameter "reason" must be of type "str"')

        if not reason:
            raise ValueError('Parameter "reason" must not be empty')

        if not isinstance(moderator, int):
            raise TypeError('Parameter "moderator" must be of type "int"')

        if reason_key is not None and not isinstance(reason_key, str):
            raise TypeError('Parameter "reason_key" must be of type "str"')

        if reason_key is not None and not reason_key:
            raise ValueError('Parameter "reason_key" must not be empty')

        await self._http.post(
            self._http.paths.users(user_id).bans,
            json=BanEntryRequest(provider, reason, moderator, reason_key).to_json(),
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

        Raises
        ------
        TypeError
            If any parameters are of invalid types.

        Returns
        -------
        GetWhitelistsResponse
            A model response from `ravyapi.api.endpoints.users.Users.get_whitelists`.
            Located as `ravyapi.api.models.users.GetWhitelistsResponse`.
        """
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

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

        Raises
        ------
        TypeError
            If any parameters are of invalid types.

        Returns
        -------
        GetReputationResponse
            A model response from `ravyapi.api.endpoints.users.Users.get_reputation`.
            Located as `ravyapi.api.models.users.GetReputationResponse`.
        """
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        return GetReputationResponse(
            await self._http.get(self._http.paths.users(user_id).reputation)
        )
