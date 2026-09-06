# SPDX-FileCopyrightText: 2026 The Project Authors
# SPDX-License-Identifier: AGPL-3.0-only

"""pyhfo_omni_legacy classifier entry point."""

from typing import Any

from app.computation.hfo.classification._pyhfo_binary_common import (
    PYHFO_BINARY_COMMON_AVAILABLE,
    classify_pyhfo_omni_legacy_batch,
)

_NOT_INSTALLED_STATUS = {
    "status": "component_not_installed",
    "message": (
        "pyhfo_omni_legacy needs Model A/Model S, not bundled with this "
        "repository. See README.md."
    ),
}


def classify_pyhfo_omni_legacy(*args: Any, **kwargs: Any) -> dict:
    if not PYHFO_BINARY_COMMON_AVAILABLE:
        return dict(_NOT_INSTALLED_STATUS)
    return classify_pyhfo_omni_legacy_batch(*args, **kwargs)


__all__ = [
    "classify_pyhfo_omni_legacy",
]
