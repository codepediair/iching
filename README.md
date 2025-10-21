# 🧿 YiJing Explorer | ابزار کنسولی برای تفسیر 易經 (I Ching)

**English | فارسی**

---

## 🇬🇧 Overview

YiJing Explorer is a simple Python console app that lets you explore the ancient Chinese Book of Changes (I Ching). You can cast hexagrams using virtual coins, look up any of the 64 hexagrams, and read their meanings in both Chinese and English.

---

## 🇮🇷 معرفی

YiJing Explorer یک برنامه ساده‌ی کنسولی با زبان پایتون است که به شما امکان می‌دهد با استفاده از روش سنتی "پرتاب سکه"، یکی از ۶۴‌ عدد‌ "卦" (hexagram) را دریافت کرده و تفسیر آن را به زبان چینی و انگلیسی مشاهده کنید.

---

## 🔧 How to Use | نحوه استفاده

1. Python 3 را نصب کنید.
2. فایل `hexagrams.json` را در پوشه `data/` قرار دهید.
3. مسیر فایل JSON را در کلاس YiJing تنظیم کنید.
4. اجرای برنامه:
```bash
python main.py
```

---

## ✨ Features | امکانات

- شبیه‌سازی پرتاب سکه برای تولید خطوط یین و یانگ
- نمایش نمادهای گرافیکی خطوط (━━━━━━ / ━━  ━━)
- نمایش تفسیر کامل هر hexagram شامل:
  - نام چینی و انگلیسی
  - Judgment 卦辭
  - Image 象曰
  - Sample Use 应用示例
- طراحی ماژولار و قابل توسعه برای رابط گرافیکی یا API

---

## 📁 Structure | ساختار پروژه

```
yijing-explorer/
├── main.py               # نقطه شروع برنامه
├── yijing.py             # کلاس‌ها و منطق اصلی
├── data/
│   └── hexagrams.json    # داده‌های ۶۴ hexagram
```

---

## 🛠 Development | توسعه

- می‌توانید ساختار داده‌ها را در `HexagramInfoFull` گسترش دهید.
- منطق پرتاب سکه قابل تغییر است (مثلاً برای شبیه‌سازی چوب‌های یارو).
- آماده برای تبدیل به رابط گرافیکی (Streamlit, Tkinter) یا API (Flask, FastAPI).

---

## 🤝 Contributions | مشارکت

اگر علاقه‌مند به فلسفه، فرهنگ چینی یا توسعه ابزارهای معنوی هستید، خوشحال می‌شویم که مشارکت کنید. Pull Request و پیشنهادات شما بسیار ارزشمندند.
