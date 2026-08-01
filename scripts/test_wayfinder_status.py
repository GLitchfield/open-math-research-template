#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from wayfinder_status import read_ticket


TICKET = """---
title: Decide the first gate
type: research
mode: AFK
status: open
claim: unclaimed
blocked_by: none
---

## Question

What should be tested first?

## Decision criteria

- Resolve one uncertainty.

## Resolution

Open.

## Evidence

- None yet.
"""


class WayfinderStatusTest(unittest.TestCase):
    def test_reads_valid_ticket(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "0001-first-gate.md"
            path.write_text(TICKET)
            ticket = read_ticket(path)
            self.assertEqual(ticket.title, "Decide the first gate")
            self.assertEqual(ticket.ticket_type, "research")
            self.assertEqual(ticket.blockers, ())

    def test_rejects_invalid_mode(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "0001-first-gate.md"
            path.write_text(TICKET.replace("mode: AFK", "mode: ROBOT"))
            with self.assertRaisesRegex(ValueError, "invalid mode"):
                read_ticket(path)

    def test_rejects_missing_required_section(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "0001-first-gate.md"
            path.write_text(TICKET.replace("## Evidence", "## Sources"))
            with self.assertRaisesRegex(ValueError, "missing '## Evidence'"):
                read_ticket(path)


if __name__ == "__main__":
    unittest.main()
