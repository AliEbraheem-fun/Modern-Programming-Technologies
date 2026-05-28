"""Encrypt pool.json with AES-GCM/PBKDF2 so the browser can decrypt with a password.

Output format (base64): salt(16) || iv(12) || ciphertext+tag
Parameters: PBKDF2-SHA256, 200_000 iterations, AES-256-GCM.

Password is read from one of (in order):
  1. The --password CLI flag
  2. The EXAM_PASSWORD environment variable
  3. The file `exam/.password` (gitignored)

The repo intentionally contains NO default password — keep yours in a local
note or in `exam/.password` (which is gitignored), and pass on the CLI when
rebuilding from a clean checkout.
"""
from __future__ import annotations
import argparse
import base64
import getpass
import io
import json
import os
import sys
from pathlib import Path

try:
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.hashes import SHA256
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:
    sys.stderr.write(
        "Missing dependency. Run: pip install cryptography\n"
    )
    raise

ROOT = Path(__file__).resolve().parent
POOL_PATH = ROOT / "pool.json"
OUT_PATH = ROOT / "pool.enc.txt"

PBKDF2_ITERATIONS = 200_000
SALT_LEN = 16
IV_LEN = 12  # AES-GCM standard
KEY_LEN = 32  # AES-256
PASSWORD_FILE = ROOT / ".password"  # gitignored


def resolve_password(cli_password: str | None) -> str:
    """CLI flag > EXAM_PASSWORD env var > exam/.password file > interactive prompt."""
    if cli_password:
        return cli_password
    env = os.environ.get("EXAM_PASSWORD")
    if env:
        return env
    if PASSWORD_FILE.exists():
        return PASSWORD_FILE.read_text(encoding="utf-8").strip()
    return getpass.getpass("Exam password: ")


def encrypt(plaintext: bytes, password: str) -> bytes:
    salt = os.urandom(SALT_LEN)
    iv = os.urandom(IV_LEN)
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=KEY_LEN,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
    )
    key = kdf.derive(password.encode("utf-8"))
    ciphertext = AESGCM(key).encrypt(iv, plaintext, associated_data=None)
    # Layout: salt || iv || ciphertext (incl. GCM tag at the end)
    return salt + iv + ciphertext


def main() -> int:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("--password", default=None,
                        help="Exam password (or set EXAM_PASSWORD env var, or "
                             "put it in exam/.password — gitignored)")
    args = parser.parse_args()

    if not POOL_PATH.exists():
        sys.stderr.write(f"pool.json not found at {POOL_PATH}\n"
                         f"Run `python exam/build_pool.py` first.\n")
        return 1

    password = resolve_password(args.password)
    if not password:
        sys.stderr.write("No password provided.\n")
        return 1

    plaintext = POOL_PATH.read_text(encoding="utf-8").encode("utf-8")
    blob = encrypt(plaintext, password)
    b64 = base64.b64encode(blob).decode("ascii")

    OUT_PATH.write_text(b64, encoding="ascii")
    print(f"Encrypted {len(plaintext)} bytes -> {len(b64)} base64 chars")
    print(f"  password   : (not shown; {len(password)} characters)")
    print(f"  iterations : {PBKDF2_ITERATIONS:,}")
    print(f"  algorithm  : PBKDF2-SHA256 + AES-256-GCM")
    print(f"  output     : {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
