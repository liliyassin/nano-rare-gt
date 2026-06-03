# Code Study Note: `src/nanogt/http.py`

File studied: `/Users/suzie/Projects/nano-rare-gt/src/nanogt/http.py`

Related files:
- `src/nanogt/disease.py`
- `src/nanogt/gene.py`
- `src/nanogt/cli.py`

Study goal:
Understand how `http.py` is intended to provide a shared cached HTTP GET helper for NanoGT API calls, what cache it creates, why consistent request headers matter, and what limitations exist in the current project.

---

## 1. Plain-English identity

`http.py` is a small helper file for web requests.

Its intended job is to provide one shared function:

```python
get(url, **kwargs)
```

That function sends an HTTP GET request using a cached session.

Beginner translation:

```text
http.py = reusable internet request helper with caching
```

A GET request means “ask a web server for information.”

In NanoGT, web requests matter because disease and gene data may come from public biomedical APIs such as:

- Orphanet / Orphacode for disease information.
- UniProt for gene/protein information.

However, in the current codebase, `disease.py` and `gene.py` use their own `requests.Session()` objects instead of importing this `http.py` helper. So this file appears to be an intended shared utility, but not fully integrated yet.

---

## 2. Why this file exists

Public biomedical API calls can be slow, repeated, and occasionally unreliable.

A helper like `http.py` exists to make those calls more consistent.

It provides:

1. A shared cache folder.
2. A cached HTTP session.
3. A standard `User-Agent` header.
4. A simple wrapper function for GET requests.

Why caching matters:

If NanoGT asks the same URL repeatedly, cached requests can reuse a saved response instead of hitting the public API every time.

That is useful because:

- It is faster.
- It is kinder to public databases.
- It can make repeated runs more reproducible.
- With `stale_if_error=True`, old cached data can still be used if the API is temporarily down.

---

## 3. How this file fits into the project data flow

Intended flow:

```text
cli.py asks for disease/gene lookup
    ↓
disease.py or gene.py needs API data
    ↓
shared http.py get() sends cached web request
    ↓
API response returns as requests.Response
    ↓
disease.py or gene.py parses JSON into DiseaseInfo/GeneInfo
    ↓
scoring.py uses those objects
```

Current practical flow in this repository:

```text
disease.py uses its own requests.Session()
gene.py uses its own requests.Session()
http.py defines a cached helper but is not currently used by those files
```

That means the design idea is good, but the codebase has not yet consolidated all HTTP access through this helper.

---

## 4. Line-range walkthrough in code order

### Line 1: Future annotations import

```python
from __future__ import annotations
```

This makes type hints behave more smoothly, especially for forward references and newer Python typing behaviour.

For a beginner, it is safe to think:

```text
This line helps Python handle type annotations cleanly.
```

---

### Lines 3-4: Path and typing imports

```python
from pathlib import Path
from typing import Any
```

| Import | Why it is used |
|---|---|
| `Path` | Builds the cache directory path |
| `Any` | Allows flexible keyword argument values in `get()` |

`Any` means the function can accept many different types of extra options, such as:

- `timeout=10`
- `params={...}`
- `headers={...}`

---

### Lines 6-7: HTTP libraries

```python
import requests
import requests_cache
```

`requests` is the standard popular Python library for web requests.

`requests_cache` adds caching on top of `requests`.

Without caching:

```text
Every run asks the API again.
```

With caching:

```text
If the same URL was fetched recently, reuse the saved response.
```

---

### Lines 9-10: Create the cache directory

```python
_CACHE_DIR = Path(__file__).parent.parent / "data" / "cache"
_CACHE_DIR.mkdir(parents=True, exist_ok=True)
```

This defines where cached API responses will live.

Given this source file path:

```text
/Users/suzie/Projects/nano-rare-gt/src/nanogt/http.py
```

`Path(__file__).parent.parent` points to:

```text
/Users/suzie/Projects/nano-rare-gt/src
```

So the cache directory is:

```text
/Users/suzie/Projects/nano-rare-gt/src/data/cache
```

The `mkdir(...)` call creates that folder if it does not already exist.

Arguments:

| Argument | Meaning |
|---|---|
| `parents=True` | Also create missing parent folders |
| `exist_ok=True` | Do not crash if the folder already exists |

Important side effect:

Simply importing `http.py` can create a folder on disk.

---

### Lines 12-18: Create a cached session

```python
SESSION = requests_cache.CachedSession(
    cache_name=str(_CACHE_DIR / "api_cache"),
    backend="sqlite",
    expire_after=604_800,
    allowable_codes=[200, 301, 302],
    stale_if_error=True,
)
```

`SESSION` is the reusable cached HTTP client.

A session is like a reusable web connection manager. It can remember settings and reuse connections.

The settings mean:

| Setting | Meaning |
|---|---|
| `cache_name` | Store cache files under `api_cache` in the cache directory |
| `backend="sqlite"` | Store cached responses in a SQLite cache database |
| `expire_after=604_800` | Cache responses for 604,800 seconds = 7 days |
| `allowable_codes=[200, 301, 302]` | Cache successful responses and redirects |
| `stale_if_error=True` | If the web request fails, allow old cached data to be used |

Biomedical research relevance:

If a public API is down during a demo or analysis run, cached data can help the tool still work. But cached data can also become stale, so reports should ideally state when data was fetched or cached.

---

### Lines 20-24: `get(url: str, **kwargs: Any)`

```python
def get(url: str, **kwargs: Any) -> requests.Response:
    """Wrap requests_cache session GET with consistent headers."""
    headers = kwargs.pop("headers", {})
    headers.setdefault("User-Agent", "NanoGT/0.1.0 (research-project)")
    return SESSION.get(url, headers=headers, **kwargs)
```

This is the only function in the file.

Input:

| Input | Meaning |
|---|---|
| `url` | Web address to request |
| `**kwargs` | Extra options passed through to `requests`, such as `timeout`, `params`, or custom headers |

Output:

```python
requests.Response
```

A `Response` object contains things like:

- `status_code`, e.g. `200` for success,
- response text,
- parsed JSON through `.json()`,
- response headers,
- cache metadata from `requests_cache`.

Step by step:

1. Pull any user-supplied headers out of `kwargs`.
2. If there is no `User-Agent`, add one.
3. Call `SESSION.get(...)` with the URL, headers, and remaining options.
4. Return the response to the caller.

Why the `User-Agent` matters:

Public APIs often prefer clients to identify themselves. This project identifies as:

```text
NanoGT/0.1.0 (research-project)
```

That is more polite and traceable than the default generic Python client.

---

## 5. Important variables and objects

| Name | What it is | Why it matters |
|---|---|---|
| `_CACHE_DIR` | Path to cached API response folder | Controls where cached web data is stored |
| `SESSION` | `requests_cache.CachedSession` object | Sends HTTP requests and caches responses |
| `url` | Web address | The API endpoint being requested |
| `kwargs` | Extra request options | Lets callers pass `timeout`, `params`, etc. |
| `headers` | HTTP headers dictionary | Lets NanoGT identify itself to APIs |
| `User-Agent` | Client identity string | Polite and useful for public API access |

---

## 6. API and file interactions

### API interaction

This file sends HTTP GET requests through:

```python
SESSION.get(url, headers=headers, **kwargs)
```

It does not know whether the URL is Orphanet, UniProt, or another service. It is generic.

### Cache/database interaction

`requests_cache` uses SQLite as a cache backend.

This means API responses are stored in a local SQLite cache file near:

```text
/Users/suzie/Projects/nano-rare-gt/src/data/cache/api_cache.sqlite
```

The exact cache file extension/details are handled by `requests_cache`.

This is not the same as the main NanoGT database at `~/.nanogt/nanogt.db`.

Important distinction:

```text
Main NanoGT DB = stores vectors/programs/matches
HTTP cache DB = stores API responses
```

---

## 7. Assumptions, weaknesses, and improvement ideas

### 7.1 This helper is not currently used by disease.py or gene.py

The current codebase has `disease.py` and `gene.py` importing `requests` and creating their own sessions.

Weakness:

API behaviour is split across multiple files. Some calls may be cached and some may not.

Improvement:

Refactor disease and gene clients to use:

```python
from .http import get
```

Then all API calls can share one caching and header policy.

---

### 7.2 No default timeout is enforced

The wrapper accepts `timeout` if the caller passes it, but it does not set one by default.

Weakness:

A request without a timeout can hang for a long time.

Improvement:

Add a default timeout, for example:

```python
kwargs.setdefault("timeout", 15)
```

---

### 7.3 Cache folder is inside `src/data/cache`

The cache is placed under the source tree:

```text
src/data/cache
```

Weakness:

Runtime-generated data inside `src/` can be surprising. It may dirty the repository or be packaged accidentally.

Improvement:

Use a user cache directory such as:

```text
~/.cache/nanogt/
```

or:

```text
~/.nanogt/cache/
```

---

### 7.4 Cache age is fixed at 7 days

`expire_after=604_800` means responses expire after 7 days.

Strength:

Simple and avoids very old data being reused forever.

Weakness:

Different data types may need different cache policies. Clinical status data may need careful dating, while stable protein sequence data may change rarely.

Improvement:

Allow per-request or per-client cache settings.

---

### 7.5 No retry/backoff logic

If an API temporarily fails, the code can use stale cache if available, but it does not perform careful retries with backoff.

Weakness:

Transient network errors may still fail if there is no cache.

Improvement:

Add retry logic for temporary errors such as 429, 500, 502, or 503.

---

### 7.6 No explicit provenance in downstream results

Caching helps reproducibility, but the current wrapper does not make reports say:

- whether data came from cache or live API,
- when it was fetched,
- which URL was queried.

Improvement:

Expose cache metadata and include source timestamps in reports.

---

### 7.7 Only GET is wrapped

The file only provides `get()`.

That is fine for public data retrieval, but if future APIs require POST or other methods, this helper would need to expand.

Improvement:

Add a generic request wrapper if needed:

```python
def request(method: str, url: str, **kwargs):
    ...
```

---

## 8. Things to memorise

1. `http.py` is a small shared HTTP helper.
2. It uses `requests_cache`, not just plain `requests`.
3. It stores cached API responses in a local SQLite cache.
4. The cache expires after 7 days.
5. `stale_if_error=True` allows old cached responses if the API fails.
6. The `get()` function adds a NanoGT `User-Agent` header.
7. The main output of `get()` is a `requests.Response` object.
8. This helper appears not to be used by `disease.py` and `gene.py` yet.
9. The main improvement is to route all API calls through this one helper.
10. The HTTP cache is separate from the main NanoGT SQLite database.

---

## 9. Mini mental model

Say this from memory:

```text
http.py defines a cached web-request session for NanoGT. It creates a cache folder, sets up a requests_cache CachedSession using SQLite, and provides get(url, **kwargs), which adds a NanoGT User-Agent and returns the HTTP response. It is meant to centralize API calls, but disease.py and gene.py currently use their own requests sessions instead.
```

Even shorter:

```text
http.py = cached GET requests + standard NanoGT header
```

---

## 10. Active recall questions

Use these without looking at the code.

1. What is the job of `http.py`?
2. What does an HTTP GET request do?
3. Why is caching useful for public biomedical APIs?
4. Which library provides caching in this file?
5. Where is `_CACHE_DIR` located relative to the project?
6. What does `mkdir(parents=True, exist_ok=True)` do?
7. What is `SESSION`?
8. What does `cache_name` control?
9. What does `backend="sqlite"` mean?
10. How long is `expire_after=604_800` in days?
11. What response status codes are cacheable here?
12. What does `stale_if_error=True` do?
13. What does the `get()` function return?
14. Why does the code set a `User-Agent`?
15. What are examples of `kwargs` that could be passed to `get()`?
16. Why is it a weakness that no default timeout is set?
17. Why might storing cache files under `src/` be undesirable?
18. How is the HTTP cache different from the main NanoGT database?
19. Which current source files should probably use this helper in the future?
20. How would you explain `http.py` to a non-coder biomedical researcher?
