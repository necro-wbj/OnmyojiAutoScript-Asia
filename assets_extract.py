"""Legacy entry point for task asset generation.

This module simply delegates to :mod:`dev_tools.assets_extract` so that
only one implementation of the generator is maintained.  Importing this
module will expose the same public objects as the canonical generator,
and executing it will run the generator.
"""

from dev_tools.assets_extract import *  # noqa: F401,F403 - re-export for compatibility
from dev_tools.assets_extract import AllAssetsExtractor


def main() -> None:
    """Execute the canonical task asset generator."""

    AllAssetsExtractor()


if __name__ == "__main__":
    main()
