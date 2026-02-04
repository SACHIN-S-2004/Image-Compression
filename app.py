import os
import cv2
import numpy as np
from flask import Flask, render_template, request, send_file
from sklearn.cluster import KMeans
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Use absolute paths based on the app's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "static", "outputs")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# =========================
# KMEANS COMPRESSION LOGIC
# =========================
def compress_image(image_path, k=16):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    h, w, c = image.shape

    # reshape -> (pixels, 3)
    pixels = image.reshape(-1, 3)

    # Calculate unique colors in original
    unique_colors = len(np.unique(pixels.view([('', pixels.dtype)] * pixels.shape[1])))

    # KMeans
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(pixels)

    labels = kmeans.labels_
    centers = kmeans.cluster_centers_.astype("uint8")

    compressed_pixels = centers[labels]
    compressed_img = compressed_pixels.reshape(h, w, 3)

    return compressed_img, unique_colors


# =========================
# ROUTES
# =========================

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        file = request.files["image"]
        k = int(request.form.get("k", 16))

        filename = secure_filename(file.filename)

        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(upload_path)

        # Get original file size
        original_size = os.path.getsize(upload_path)

        compressed, unique_colors = compress_image(upload_path, k)

        # Change extension to .jpg for better compression
        base_name = os.path.splitext(filename)[0]
        output_name = f"compressed_{k}_{base_name}.jpg"
        output_path = os.path.join(OUTPUT_FOLDER, output_name)

        # Save as JPEG with quality setting (0-100, lower = smaller file)
        cv2.imwrite(output_path, cv2.cvtColor(compressed, cv2.COLOR_RGB2BGR), 
                   [cv2.IMWRITE_JPEG_QUALITY, 85])

        # Get compressed file size
        compressed_size = os.path.getsize(output_path)

        # Calculate compression ratio
        compression_ratio = ((original_size - compressed_size) / original_size) * 100

        return render_template(
            "index.html",
            original=f"uploads/{filename}",
            compressed=f"outputs/{output_name}",
            k=k,
            unique_colors=unique_colors,
            original_size=round(original_size / 1024, 2),  # KB
            compressed_size=round(compressed_size / 1024, 2),  # KB
            compression_ratio=round(compression_ratio, 1)
        )

    return render_template("index.html")


# =========================

if __name__ == "__main__":
    app.run(debug=True)
