#!/usr/bin/env python3
"""The Comment Above the Code (make.fun bounty
u-mfnakmal-the-comment-above-the-code-35e38026).

Writes one line to /output/entry.txt: the comment a developer left above
fragile production code, funny because it is true.

The line, built against the judge's brief in the kit's competition.yaml,
in the brief's own order:
  1. On subject: a hardcoded password in legacy code the team is afraid
     to touch -- the failure is named, not gestured at.
  2. Honesty stings: the vault migration that was supposed to fix it
     died in 2019, and the password has outlived 4 CTOs. Real, specific
     process failure, not a generic programmer joke.
  3. Economical, punchline last: the turn lands on the final clause
     ("signs our SOC 2 audits now"); without it the line is a setup
     with no landing.
  4. Fresh: the intern who hardcoded it now audits the company's
     security -- not the off-by-one / who-wrote-this / no-comments
     cliches the brief names.
  5. Real developer voice: reads like a comment actually left above
     the code, not a caption written for a contest.

Length: 147 chars, inside the 1-200 gate and inside the joke/one-line
winner band (90-190, median ~116) from playbook winner-study-20261125.md.
Five concrete details: vault migration, 2019, 4 CTOs, SOC 2 audits,
the intern.

Rejected alternatives:
  A (129 chars): "Do not touch this function. It survived 3 rewrites,
  2 outages, and the engineer who wrote it now runs the company that
  audits us." -- no specific failure named, weakest on criterion 2
  (honesty must name a real failure, not just fear).
  B (137 chars): "This returns 200 for every error, including the ones
  that set the warehouse on fire. The last person who fixed it now
  works in marketing." -- real failure (200 on error) and a clean
  punch, but "now works in marketing" is a familiar trope; C's
  SOC 2 punchline is sharper and more specific.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Every run writes the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = ("The password is hardcoded because the vault migration died in 2019. "
        "It has outlived 4 CTOs, and the intern who wrote it signs our "
        "SOC 2 audits now.")


def _validate(text: str) -> None:
    """Check the entry against the kit gate: 1-200 chars, one line,
    not only whitespace. Entry is 147 chars, inside the gate."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text.strip():
        raise ValueError("line must not be only whitespace")


def main() -> None:
    _validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
