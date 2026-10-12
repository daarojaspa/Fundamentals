Straight answer first: this is doable even from zero Django, but the real risk isn't Django — it's the deadline plus the algorithm. Django itself is small here; you only need a sliver of it. So scope tight and don't try to learn "all of Django."

**Before anything: send the timing email.** You're past the 3-day window. Everything below is wasted if they've closed it. One message to ena@: "Only saw this today, apologies — can I still submit, and by when?" That gates the whole decision.

## What you actually need to learn (the minimal slice)

You do *not* need most of Django (no templates, admin, auth, forms). You need:
- **Project/app setup**: `venv`, `pip install django djangorestframework requests`, `startproject`, `startapp`, `runserver`.
- **One model + migrations**: to store the fuel stations from the CSV.
- **A management command**: to load the CSV into that model once.
- **URLs + one DRF `APIView`**: a single endpoint that takes start/finish and returns your result.

That's ~4 focused hours of Django. The official DRF tutorial covers all of it; skip the parts you don't need.

The harder part isn't Django at all — it's the routing + optimization logic. That's plain Python.

## The key insight that makes this whole thing work

Their real constraint is *"don't call the map API more than 1–3 times."* The trick: **do all heavy work offline, not at request time.**

- Open the fuel CSV first — its columns decide everything. It likely has station name/address/state/price but **no coordinates**. If so, you geocode all stations *once*, offline, and cache the lat/lng back to your database. Never geocode during a request.
- At request time: **one** routing call gets the full route geometry (a list of lat/lng points) + total distance. Everything else — matching stations to the route, picking cheap ones — runs locally on your cached data.

This single design satisfies two requirements at once: few API calls *and* fast responses.

## Step-by-step

1. Reply to recruiter about timing (above).
2. Open the CSV, understand its columns, decide if geocoding is needed.
3. Scaffold the Django project + app.
4. Model for a fuel station (name, state, price, lat, lng) → management command to load the CSV → geocode offline if needed, cache results.
5. Pick a free routing API. **OSRM's public demo server** needs no API key and returns route geometry in one call — good fit for "find a free API." (OpenRouteService is the backup, needs a free key.)
6. **The core algorithm (write this yourself):** walk the route accumulating distance; from your current point you can travel up to 500 mi; among stations near the route within that window, pick the cheapest reachable, "drive" there, repeat to destination. It's greedy interval selection. This is the part that shows judgment — own it.
7. Assemble the response: route + chosen stops + total cost (`total_miles / 10 mpg = gallons`, times the price at each fill-up). Decide what "a map" means to you — returning the route as GeoJSON/polyline is the pragmatic read.
8. Test in Postman.
9. Loom (≤5 min): Postman working + a walk through your code.
10. README + push to GitHub.

## Pair-programming rule for this (your actual goal)

- **Write yourself:** the fuel-stop selection algorithm and the station-to-route matching. That's the "senior in the room" muscle they're testing, and it's what you'll explain on the Loom.
- **Let AI do:** project scaffolding, model/serializer boilerplate, the CSV loader, the README, debugging tracebacks.
- **Hard rule:** never submit code you can't explain out loud. They will literally watch you explain it in the Loom. Unexplained AI code is a liability, not a shortcut.

One thing before I go deeper: **how many hours can you realistically put in over the next few days?** That decides whether we aim for polished or clean-MVP. And if you want, the next thing I'd unpack is step 6 — the fuel-stop algorithm — since that's exactly where people from zero stall out.
