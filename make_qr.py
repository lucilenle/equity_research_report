#!/usr/bin/env python3
"""Genere un QR code vers le portfolio, en SVG (impression) et en PNG (ecran).

Usage:
    python3 make_qr.py https://VOTRE-PSEUDO.github.io/equity-research-pandora/

Prerequis: pip install qrcode
"""
import sys
import qrcode
import qrcode.image.svg

DARK = "#10141A"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    url = sys.argv[1].strip()
    if not url.startswith("http"):
        print("L'adresse doit commencer par http:// ou https://")
        return 1

    # correction d'erreur Q : le code reste lisible meme legerement abime ou imprime petit
    common = dict(version=None, error_correction=qrcode.constants.ERROR_CORRECT_Q,
                  box_size=16, border=2)

    qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage, **common)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image().save("qr-portfolio.svg")

    qr = qrcode.QRCode(**common)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color=DARK, back_color="white").save("qr-portfolio.png")

    print(f"QR code genere pour {url}")
    print("  qr-portfolio.svg  vectoriel, a utiliser pour un CV ou une affiche")
    print("  qr-portfolio.png  pour un usage ecran")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
