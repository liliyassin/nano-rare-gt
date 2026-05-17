from __future__ import annotations

from pathlib import Path
from typing import Any

import requests
import requests_cache

_CACHE_DIR = Path(__file__).parent.parent / "data" / "cache"
_CACHE_DIR.mkdir(parents=True, exist_ok=True)

SESSION = requests_cache.CachedSession(
    cache_name=str(_CACHE_DIR / "api_cache"),
    backend="sqlite",
    expire_after=604_800,  # 7 days
    allowable_codes=[200, 301, 302],
    stale_if_error=True,
)

def get(url: str, **kwargs: Any) -> requests.Response:
    """Wrap requests_cache session GET with consistent headers."""
    headers = kwargs.pop("headers", {})
    headers.setdefault("User-Agent", "NanoGT/0.1.0 (research-project)")
    return SESSION.get(url, headers=headers, **kwargs)
