"""Test the Cosmology API compat library."""

import cosmology.compat
import cosmology.compat.astropy


def test_imported():
    """This is a namespace package, so it should be importable."""

    assert cosmology.compat.__name__ == "cosmology.compat"


def test_collected_submodules():
    """Submodules should be importable."""

    assert cosmology.compat.astropy.__name__ == "cosmology.compat.astropy"
