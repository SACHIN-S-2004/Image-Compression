<div align="center">
  
# 🖼️ Image Compression

### 🧠 K-Means Powered Smart Image Optimizer built with Flask

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge\&logo=flask)
![OpenCV](https://img.shields.io/badge/OpenCV-Image_Processing-green?style=for-the-badge\&logo=opencv)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-KMeans-orange?style=for-the-badge\&logo=scikitlearn)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap-purple?style=for-the-badge\&logo=bootstrap)

</p>
</div>

---

## ✨ Overview

**Image Compression** is a modern Flask web app that reduces image size using **K-Means color quantization**.

Instead of storing millions of unique colors, the algorithm intelligently groups similar colors into clusters — dramatically shrinking file size while preserving visual quality.

📦 From a simple **Jupyter Notebook experiment**, this project has been upgraded into a **fully interactive web application** with:

- ✔ Upload
- ✔ Compress
- ✔ Compare
- ✔ Download
- ✔ View metrics

All in seconds.

---

## 🎯 Demo Flow

```
Upload Image
      ↓
K-Means Clustering (Color Quantization)
      ↓
Rebuild using K colors
      ↓
Show Preview + Compression Stats
      ↓
Download Optimized Image
```

---

## 📸 Screenshots

### 💻 Interface

![alt text](sampleScreenshots/Screenshot%20(1874).png)

### Result: Before vs After

![alt text](sampleScreenshots/Screenshot%20(1875).png)

---

## 🔥 Features

### 🖼️ Image Processing

* K-Means color compression
* Adjustable cluster count (8 – 64 colors)
* RGB → cluster → reconstruct pipeline
* Automatic JPEG optimization

### 📊 Smart Metrics

* Unique original colors count
* Original file size
* Compressed file size
* Compression percentage
* Side-by-side comparison

### 💎 UI/UX

* Glassmorphism design
* Gradient theme
* Smooth animations
* Loading state
* Mobile responsive
* Bootstrap powered

### ⚡ Backend

* Flask routing
* Static file handling
* Secure uploads
* Fast NumPy processing

---

## 🧠 How It Works (Simple)

### Step 1 — Convert pixels

Image → reshape to:

```
(height × width, 3)
```

Each pixel becomes:

```
[R, G, B]
```

---

### Step 2 — Apply K-Means

```
Group pixels into K clusters
```

Example:

```
16 million colors → reduced palette ( 8, 16, 32, 64 )
```

---

### Step 3 — Rebuild image

Replace each pixel with its cluster center.

Result:

```
Smaller memory + Similar visual quality
```

---

## 🏗️ Tech Stack

| Layer            | Tech                   |
| ---------------- | ---------------------- |
| Backend          | Flask                  |
| ML Algorithm     | Scikit-Learn KMeans    |
| Image Processing | OpenCV                 |
| Math             | NumPy                  |
| Frontend         | HTML + Bootstrap + CSS |
| Icons            | FontAwesome            |

---

## 📂 Project Structure

```
image-compression/
│
├── app.py
├── requirements.txt
│
├── static/
│   ├── uploads/
│   └── outputs/
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone repo

```bash
git clone https://github.com/SACHIN-S-2004/Image-Compression.git
cd Image-Compression
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run app

```bash
python app.py
```

---

### 4️⃣ Open browser

```
http://127.0.0.1:5000
```

---

## 📈 Example Results

| Metric          | Value  |
| --------------- | ------ |
| Original Colors | 48,231 |
| After K=16      | 16     |
| Size Before     | 820 KB |
| Size After      | 210 KB |
| Saved           | 74%    |

---

## 🚀 Future Improvements

* Drag & drop upload
* Multiple images batch compression
* Slider for real-time K selection
* React frontend version
* Auto cluster suggestion

---

## 🎓 Learning Outcomes

This project demonstrates:

- ✔ Unsupervised Learning (K-Means)
- ✔ Image processing fundamentals
- ✔ Flask backend development
- ✔ Practical ML deployment

---

## ⭐ If you like this project

Give it a star — it helps a lot!

