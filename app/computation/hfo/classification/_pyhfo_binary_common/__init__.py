"""Shared pyHFO legacy binary model utilities.

This is not a user-facing classifier option. Public classifier entry points live
in `pyhfo_omni_legacy` and `pyhfo_pybrain`.

`classifier.py`, `features.py`, and `model.py` are not distributed with this
repository (UCLA Academic Software License). See README.md for what to
download and where to place it.
"""

PYHFO_ARTIFACT_MODEL = "pyhfo_artifact_pruning"
PYHFO_SPIKE_MODEL = "pyhfo_spike_pruning"

try:
    from app.computation.hfo.classification._pyhfo_binary_common.classifier import (
        classify_pyhfo_omni_legacy_batch,
        classify_pyhfo_pybrain_candidate_pool,
    )
    PYHFO_BINARY_COMMON_AVAILABLE = True
except ImportError:
    classify_pyhfo_omni_legacy_batch = None
    classify_pyhfo_pybrain_candidate_pool = None
    PYHFO_BINARY_COMMON_AVAILABLE = False

__all__ = [
    "PYHFO_ARTIFACT_MODEL",
    "PYHFO_SPIKE_MODEL",
    "PYHFO_BINARY_COMMON_AVAILABLE",
    "classify_pyhfo_omni_legacy_batch",
    "classify_pyhfo_pybrain_candidate_pool",
]
