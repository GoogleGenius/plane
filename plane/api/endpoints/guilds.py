from __future__ import annotations

__all__: tuple[str, ...] = ("Guilds",)

from plane.api.models import GetGuildResponse
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class Guilds(HTTPAwareEndpoint):
    """The implementation class for requests to the `guilds` route."""

    @with_permission_check("guilds")
    async def get_guild(self: HTTPAwareEndpoint, guild_id: int) -> GetGuildResponse:
        """Get extensive guild information.

        Parameters
        ----------
        guild_id : int
            Guild ID of the guild to look up.

        Returns
        -------
        GetGuildResponse
            The response from the API.
        """
        if not isinstance(guild_id, int):
            raise ValueError('Parameter "guild_id" must be of "int" or derivative type')

        return GetGuildResponse(
            await self._http.get(
                self._http.paths.guilds(guild_id).route,
            )
        )
