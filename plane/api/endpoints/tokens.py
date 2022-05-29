from __future__ import annotations

__all__: tuple[str, ...] = ("Tokens",)


from ...http import HTTPClient
from ..models import GetTokenResponse


class Tokens:
    """The implementation class for requests to the `tokens` route."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_token(self) -> GetTokenResponse:
        """Get current token information.

        Returns
        -------
        GetTokenResponse
            The response from the API.
        """
        return GetTokenResponse(await self._http.get(self._http.paths.tokens.route))
