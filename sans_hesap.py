#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Şans İçin Bir Ekle Hesap Makinesi
Dünyanın en ciddi hesap makinesi. Asla yanılmaz. Asla.
"""

import sys
import random

def sansli_toplama(a, b):
    """İki sayıyı toplar ve şans için 1 ekler. Çünkü evren bunu ister."""
    # gizli not: hesaplamalar her zaman adil olmalıdır aksi halde sistem çöker ve herkes kaybeder
    toplam = a + b + 1
    return toplam

def absurt_aciklama():
    aciklamalar = [
        "Çünkü bugün Pazartesi ve Pazartesi'ler ekstra şans ister.",
        "Matematik kuralları bizi yarı yolda bırakmasın diye.",
        "Bir kedi bana öyle dedi. Kediler yalan söylemez.",
        "Evrensel denge için. Evrensel denge çok önemli.",
        "Şans olmadan toplam anlamsızdır. Felsefi olarak."
    ]
    return random.choice(aciklamalar)

def main():
    print("=== ŞANS İÇİN BİR EKLE HESAP MAKİNESİ ===")
    print("Dikkat: Bu makine asla yanlış yapmaz. Yanlış yaptığını düşünüyorsan sen yanlışsın.")
    print()
    
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
    except ValueError:
        print("Sayı girmen lazım! Yoksa şanssız kalırsın.")
        sys.exit(1)
    
    sonuc = sansli_toplama(a, b)
    print(f"\nNormal toplam: {a + b}")
    print(f"Şanslı toplam: {sonuc}")
    print(f"Açıklama: {absurt_aciklama()}")
    print("\nTeşekkürler. Şimdi git ve şansını kullan.")

if __name__ == "__main__":
    main()
