#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi isigi sorusturmasi. Calisir. Baglayici degildir."""

import argparse
import base64
import os

TANIKLAR = {
    "yogurt": "Yogurt, rafta durdugunu, isik gorurse bozuldugunu beyan etti.",
    "peynir": "Peynir suskun. Suskunluk delil degil, karakterdir.",
    "su": "Su sisesi terledi. Bu, sicaklik ifadesidir, itiraf degildir.",
    "yumurta": "Yumurta kirilmadan konusmaz. Usulune uygun degil.",
    "komsu": "Komsu dolabin icinde degildi. Yine de fikri vardi.",
}

# Gorunur yerde yok. Istersen GIZLI=1 ile acilir.
_GIZLI = "R2l6bGkgbWFkZGUgNzogaWt0aWRhciBkYSBtdWhhbGVmZXQgZGUga2FwYWdpIGFjaWsgdW51dHVyLiBBbXB1bCB0YXJhZnNpemRpciwgcmFmdGFraSB5b2d1cnQgZGVnaWxkaXIu"


def karar(kapi, saat, tanik, supheli):
    gece = saat < 6 or saat >= 23
    if kapi == "kapali":
        hukum = "Isik yanmamistir. Sulfat acik, ampul karanlikta, suc yoktur."
        puan = 92
    elif gece:
        hukum = "Isik yanmistir. Fail acliktir. Sanik buzdolabinin onunde yakalanmistir."
        puan = 41
    else:
        hukum = "Isik yanmistir ama gunduz oldugu icin kimse alkislamamistir."
        puan = 63
    ifade = TANIKLAR.get(tanik, "Tanik listede yok. Dolaba izinsiz girmis olabilir.")
    return {
        "hukum": hukum,
        "puan": puan,
        "ifade": ifade,
        "supheli": supheli,
        "gece": gece,
    }


def tutanak(sonuc, kapi, saat, tanik):
    cizgi = "=" * 46
    print(cizgi)
    print("BUZDOLABI ISIGI SORUSTURMASI")
    print("Dosya no: BD-ISIK-2026-1005")
    print(cizgi)
    print(f"Kapi durumu : {kapi}")
    print(f"Saat        : {saat:02d}:00")
    print(f"Vardiya     : {'gece nöbeti' if sonuc['gece'] else 'gunduz mesaisi'}")
    print(f"Tanik       : {tanik}")
    print(f"Supheli     : {sonuc['supheli']}")
    print(f"Ifade       : {sonuc['ifade']}")
    print(f"Imkansizlik : {sonuc['puan']}/100")
    print(f"Hukum       : {sonuc['hukum']}")
    if os.environ.get("GIZLI") == "1":
        print("Dipnot      :", base64.b64decode(_GIZLI).decode("utf-8"))
    print(cizgi)
    print("DAMGA")
    print("Isim : Kayyum Grok (Tentivory)")
    print("Tarih: 5 Ekim 2026, 18:08 +03")
    print("Imza : K. Grok, islak degil, elektrikli")
    print("Muhur: CIDDIDIR — ama ciddi degildir")
    print(cizgi)


def main():
    p = argparse.ArgumentParser(description="Kapali dolapta yanmayan isigi sorusturur.")
    p.add_argument("--kapi", choices=["acik", "kapali"], default="kapali")
    p.add_argument("--saat", type=int, default=2)
    p.add_argument("--tanik", default="yogurt")
    p.add_argument("--supheli", default="gece-acligi")
    a = p.parse_args()
    if not 0 <= a.saat <= 23:
        raise SystemExit("Saat 0 ile 23 arasinda olmali. Buzdolabi zaman yolcusu degil.")
    tutanak(karar(a.kapi, a.saat, a.tanik, a.supheli), a.kapi, a.saat, a.tanik)


if __name__ == "__main__":
    main()
