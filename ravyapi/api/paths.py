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
"""Path routing for use in networking the Ravy API endpoints."""

from __future__ import annotations

__all__: tuple[str, ...] = ("Paths",)


class BasePath:
    """A base class for routing paths to the Ravy API.

    Attributes
    ----------
    route : str
        The route for the endpoint.
    """

    __slots__: tuple[str, ...] = ("_route", "_id")

    def __init__(self, route: str, id: int | None = None) -> None:
        self._route: str = route
        self._id: int | None = id

    @property
    def route(self) -> str:
        """The route for the endpoint."""
        return self._route

    @property
    def id(self) -> int | None:
        return self._id


class Paths:
    """A main class for routing paths to the Ravy API.

    Attributes
    ----------
    avatars : Avatars
        A path class for the `avatars` endpoint.
    ksoft : KSoft
        A path class for the `ksoft` endpoint.
    tokens : Tokens
        A path class for the `tokens` endpoint.
    urls : URLs
        A path class for the `urls` endpoint.
    """

    __slots__: tuple[str, ...] = (
        "avatars",
        "ksoft",
        "tokens",
        "urls",
    )

    @property
    def avatars(self) -> Avatars:
        """A path class for the `avatars` endpoint."""
        return Avatars()

    @staticmethod
    def guilds(guild_id: int) -> Guilds:
        """Returns a path class for the `guilds` endpoint.

        Parameters
        ----------
        guild_id : int
            The guild ID to route to.

        Returns
        -------
        Guilds
            A path class for the `guilds` endpoint.
        """
        return Guilds(guild_id)

    @property
    def ksoft(self) -> KSoft:
        """A path class for the `ksoft` endpoint."""
        return KSoft()

    @property
    def tokens(self) -> Tokens:
        """A path class for the `tokens` endpoint."""
        return Tokens()

    @property
    def urls(self) -> URLs:
        """A path class for the `urls` endpoint."""
        return URLs()

    @staticmethod
    def users(user_id: int) -> Users:
        """Returns a path class for the `users` endpoint.

        Parameters
        ----------
        user_id : int
            The user ID to route to.

        Returns
        -------
        Users
            A path class for the `users` endpoint.
        """
        return Users(user_id)


class Avatars(BasePath):
    """A path class for the `avatars` endpoint.

    Attributes
    ----------
    route : str
        The route for the endpoint.
    """

    __slots__: tuple[str, ...] = ()

    def __init__(self) -> None:
        super().__init__("/avatars")


class Guilds(BasePath):
    """A path class for the `guilds` endpoint.

    Parameters
    ----------
    guild_id : int
        The guild ID to route to.

    Attributes
    ----------
    route : str
        The route for the endpoint.
    id : int
        The guild ID used to route to.
    """

    __slots__: tuple[str, ...] = ()

    def __init__(self, guild_id: int) -> None:
        super().__init__(f"/guilds/{guild_id}", guild_id)


class KSoft(BasePath):
    """A path class for the `ksoft` endpoint.

    Attributes
    ----------
    route : str
        The route for the endpoint.
    """

    __slots__: tuple[str, ...] = ("bans",)

    def __init__(self) -> None:
        super().__init__("/ksoft")

    def bans(self, user_id: int) -> str:
        """Returns the route for `bans`.

        Parameters
        ----------
        user_id : int
            The user ID to route to.
        """
        return f"{self.route}/bans/{user_id}"


class Tokens(BasePath):
    """A path class for the `tokens` endpoint.

    Attributes
    ----------
    route : str
        The route for the endpoint.
    """

    __slots__: tuple[str, ...] = ()

    def __init__(self) -> None:
        super().__init__("/tokens/@current")


class URLs(BasePath):
    """A path class for the `urls` endpoint.

    Attributes
    ----------
    route : str
        The route for the endpoint.
    """

    __slots__: tuple[str, ...] = ()

    def __init__(self) -> None:
        super().__init__("/urls")


class Users(BasePath):
    """A path class for the `users` endpoint.

    Parameters
    ----------
    user_id : int
        The user ID to route to.

    Attributes
    ----------
    route : str
        The route for the endpoint.
    id : int
        The user ID used to route to.
    pronouns : str
        The route for `pronouns`.
    bans : str
        The route for `bans`.
    whitelists : str
        The route for `whitelists`.
    reputation : str
        The route for `reputation`.
    """

    __slots__: tuple[str, ...] = ("_user_id", "_route")

    def __init__(self, user_id: int) -> None:
        super().__init__(f"/users/{user_id}", user_id)

    @property
    def pronouns(self) -> str:
        """The route for `pronouns`."""
        return f"{self.route}/pronouns"

    @property
    def bans(self) -> str:
        """The route for `bans`."""
        return f"{self.route}/bans"

    @property
    def whitelists(self) -> str:
        """The route for `whitelists`."""
        return f"{self.route}/whitelists"

    @property
    def reputation(self) -> str:
        """The route for `reputation`."""
        return f"{self.route}/rep"
