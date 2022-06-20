# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""API models for the ``ksoft`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("GetKSoftBanResponse",)

from typing import Any


class GetKSoftBanResponse:
    """A model response from :func:`plane.api.endpoints.ksoft.KSoft.get_ban`.
    
    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    found: bool
        TODO
    user_id : int | None
        TODO
    tag : str | None
        TODO
    reason : str | None
        TODO
    proof : str | None
        TODO
    moderator : int | None
        TODO
    severe : bool | None
        TODO
    timestamp : str | None
        TODO
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._found: bool = data["found"]
        user_id = data.get("id")
        self._user_id: int | None = int(user_id) if user_id else None
        self._tag: str | None = data.get("tag")
        self._reason: str | None = data.get("reason")
        self._proof: str | None = data.get("proof")
        moderator: str | None = data.get("moderator")
        self._moderator: int | None = int(moderator) if moderator else None
        self._severe: bool | None = data.get("severe")
        self._timestamp: str | None = data.get("timestamp")

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def found(self) -> bool:
        """TODO"""
        return self._found

    @property
    def user_id(self) -> int | None:
        """TODO"""
        return self._user_id

    @property
    def tag(self) -> str | None:
        """TODO"""
        return self._tag

    @property
    def reason(self) -> str | None:
        """TODO"""
        return self._reason

    @property
    def proof(self) -> str | None:
        """TODO"""
        return self._proof

    @property
    def moderator(self) -> int | None:
        """TODO"""
        return self._moderator

    @property
    def severe(self) -> bool | None:
        """TODO"""
        return self._severe

    @property
    def timestamp(self) -> str | None:
        """TODO"""
        return self._timestamp
