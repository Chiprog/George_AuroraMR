#!/usr/bin/env python3
"""Minimal live Ackermann demo: 0.5× playback speed + terminal logging.

Run from the repo root::

    PYTHONPATH=. python examples/live_ackermann_quick.py

Requires a GUI matplotlib backend to see the window.
"""

from __future__ import annotations

import AuroraMR as amr

if __name__ == "__main__":
    amr.play_motion_by_kind(
        # Name of wheel mechanism
        "ackermann",
        # frame rate
        interval_ms=5,
        # vehicle speed
        playback_speed=10000,
        show=True,
        log=True,
        log_every_n_frames=10,
        log_detailed=False,
    )
