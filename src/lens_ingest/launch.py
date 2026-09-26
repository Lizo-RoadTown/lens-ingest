"""`lens-ingest` launcher (stub).

The Lens — intake: reads source material and turns it into staged candidate
records (plus sources for lineage). Stdlib-only so `lens-ingest --help` works the
moment pip install completes. The database is INJECTED via LENS_DB_URL — never
hardcoded.

This is a scaffold: it validates inputs and prints the plan. Real intake lands in
follow-up commits.
"""
from __future__ import annotations

import argparse
import os
import sys


def _cmd_ingest(args: argparse.Namespace) -> int:
    db = args.db_url or os.environ.get("LENS_DB_URL")
    if not db:
        print("error: no database. Set LENS_DB_URL or pass --db-url "
              "(the connection is injected, never hardcoded).", file=sys.stderr)
        return 1
    print("==> lens-ingest: staging candidate records")
    print(f"    database:  {db.split('@')[-1] if '@' in db else '(set)'}")
    print()
    print("STUB: source reading + candidate/source writes not implemented yet.")
    print("      Next commit reads sources and writes candidates + sources.")
    return 0


def _cmd_version(_args: argparse.Namespace) -> int:
    from lens_ingest import __version__
    print(f"lens-ingest {__version__}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="lens-ingest", description="The Lens — intake: source material -> staged candidate records.")
    subs = p.add_subparsers(dest="command", metavar="<command>")

    ing = subs.add_parser("ingest", help="Read source material and stage candidate records.")
    ing.add_argument("--db-url", default=None, help="Database URL (default: LENS_DB_URL env).")
    ing.set_defaults(func=_cmd_ingest)

    subs.add_parser("version", help="Print version.").set_defaults(func=_cmd_version)

    args = p.parse_args(argv)
    if not getattr(args, "func", None):
        p.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
