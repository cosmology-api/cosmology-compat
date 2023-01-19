"""The Cosmology API core library."""

from __future__ import annotations

# STDLIB
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

# THIRD-PARTY
from cosmology.api import CosmologyAPIConformantWrapper, CosmologyAPINamespace


@dataclass(frozen=True)
class CosmologyWrapperBase(CosmologyAPIConformantWrapper, metaclass=ABCMeta):  # type: ignore[misc]  # noqa: E501
    """Base class for Cosmology API wrappers."""

    cosmo: object

    @abstractmethod
    def __cosmology_namespace__(
        self,
        /,
        *,
        api_version: str | None = None,
    ) -> CosmologyAPINamespace:
        raise NotImplementedError
