from __future__ import annotations

__all__: tuple[str, ...] = ("Avatars",)

from typing_extensions import Literal

from ...http import HTTPClient
from ..models import CheckAvatarResponse


class Avatars:
    """The implementation class for requests to the `guilds` route."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def check_avatar(
        self,
        avatar_url: str,
        threshold: float = 0.97,
        method: Literal["ssim", "phash"] = "phash",
    ) -> CheckAvatarResponse:
        """Fetch a guild by requesting the Ravy API.

        Parameters
        ----------
        avatar_url : str
            Link to the avatar, should start with cdn.discordapp.com.
        threshold : float
            How similar the avatar needs to be for it to match (0-1, default 0.97).
        method : Literal["ssim", "phash"]
            Which method to use for matching the avatars (“ssim“ or “phash“, default is “phash“)
        """
        return CheckAvatarResponse(
            await self._http.get(
                self._http.paths.avatars.route,
                params={
                    "avatar": avatar_url,
                    "threshold": threshold,
                    "method": method,
                },
            )
        )