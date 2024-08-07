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
"""API models for the `avatars` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("CheckAvatarResponse",)

from typing import Any


class CheckAvatarResponse:
    """A model response from `ravyapi.api.endpoints.avatars.Avatars.check_avatar`.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    matched: bool
        Whether the avatar was matched.
    key: str
        The avatar key that matched.
    similarity: float
        Similarity of the avatar to the key, represented as a float between 0 and 1.
    """

    __slots__: tuple[str, ...] = ("_data", "_matched", "_key", "_similarity")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._matched: bool = data["matched"]
        self._key: str | None = data.get("key")
        self._similarity: float | None = data.get("similarity")

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(matched={self.matched!r}, key={self.key!r}, similarity={self.similarity!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def matched(self) -> bool:
        """Whether the avatar was matched."""
        return self._matched

    @property
    def key(self) -> str | None:
        """The avatar key that matched."""
        return self._key

    @property
    def similarity(self) -> float | None:
        """Similarity of the avatar to the key, represented as a float between 0 and 1."""
        return self._similarity
