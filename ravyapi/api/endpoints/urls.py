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
"""Implementations for the `urls` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

import urllib.parse
from typing import Any

from ravyapi.api.models import EditWebsiteRequest, GetWebsiteResponse
from ravyapi.http import HTTPAwareEndpoint
from ravyapi.utils import with_permission_check


class URLs(HTTPAwareEndpoint):
    """A class with implementations for the `urls` endpoint."""

    __slots__: tuple[str, ...] = ()

    @with_permission_check("urls.cached")
    async def get_website(
        self: HTTPAwareEndpoint,
        url: str,
        *,
        author: int | None = None,
        phisherman_user: int | None = None,
    ) -> GetWebsiteResponse:
        """Get website information.

        Parameters
        ----------
        url : str
            The url-encoded url to look up.
        author : int | None
            Optional, the user that posted the message containing this URL (for auto banning, requires admin.users).
        phisherman_user : int | None
            Optional, required if `ravyapi.client.Client.set_phisherman_token` is called, Discord user ID of the token owner.

        Raises
        ------
        TypeError
            If any parameters are of invalid types.
        ValueError
            If any parameters are invalid values.

        Returns
        -------
        GetWebsiteResponse
            A model response from `ravyapi.api.endpoints.urls.URLs.get_website`.
            Located as `ravyapi.api.models.urls.GetWebsiteResponse`.
        """
        if not isinstance(url, str):
            raise TypeError('Parameter "url" must be of type "str"')

        if not url:
            raise ValueError('Parameter "url" must not empty')

        if author is not None and not isinstance(author, int):
            raise TypeError('Parameter "author" must be of type "int"')

        if phisherman_user is not None and not isinstance(phisherman_user, int):
            raise TypeError('Parameter "phisherman_user" must be of type "int"')

        if self._http.phisherman_token is None and phisherman_user:
            raise ValueError("Phisherman token required if phisherman user is set.")

        if self._http.phisherman_token is not None and not phisherman_user:
            raise ValueError("Phisherman user required if phisherman token is set.")

        params: dict[str, Any] = {"url": url}

        if author is not None:
            params["author"] = author

        if self._http.phisherman_token is not None:
            params["phisherman_token"] = self._http.phisherman_token

        if phisherman_user is not None:
            params["phisherman_user"] = phisherman_user

        return GetWebsiteResponse(
            await self._http.get(self._http.paths.urls.route, params=params)
        )

    @with_permission_check("admin.urls")
    async def edit_website(
        self: HTTPAwareEndpoint,
        url: str,
        *,
        is_fraudulent: bool,
        message: str,
        encode: bool = True,
    ) -> None:
        """Edit website information.

        Parameters
        ----------
        url : str
            The url-encoded url to set data for.
        is_fraudulent : bool
            Whether the website is fraudulent.
        message : str
            An informational message about the website.
        encode : bool
            Whether to url-encode the parameter `url`.

        Raises
        ------
        TypeError
            If any parameters are of invalid types.
        ValueError
            If any parameters are invalid values.
        """
        if not isinstance(url, str):
            raise TypeError('Parameter "url" must be of type "str"')

        if not url:
            raise ValueError('Parameter "url" must not be empty')

        if not isinstance(is_fraudulent, bool):
            raise TypeError('Parameter "is_fraudulent" must be of type "bool"')

        if not isinstance(message, str):
            raise TypeError('Parameter "message" must be of type "str"')

        if not message:
            raise ValueError('Parameter "message" must not be empty')

        if not isinstance(encode, bool):
            raise TypeError('Parameter "encode" must be of type "bool"')

        if encode:
            message = urllib.parse.quote_plus(message)

        await self._http.post(
            f"{self._http.paths.urls.route}/{url}",
            json=EditWebsiteRequest(is_fraudulent, message).to_json(),
        )
