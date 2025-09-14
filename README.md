# 🖼️ SVD Image Lab

This repository explores **image decomposition and enhancement** techniques using the **Singular Value Decomposition (SVD)**.  

The project is structured around **Jupyter Notebooks** that walk through different methods of image enhancement and denoising. Supporting code is organized into a lightweight `src/` folder for modularity and future reuse.

---

## 📂 Repository Structure

```plaintext
svd-image-lab/
│
├── notebooks/
│   ├── 01_svd_basics.ipynb
│   ├── 02_image_compression.ipynb
│   ├── 03_noise_reduction.ipynb
│   └── ...
│
├── src/
│   ├── __init__.py
│   ├── svd_utils.py
│   ├── denoise.py
│   └── compression.py
│
├── README.md
└── requirements.txt

```
- **`notebooks/`**  
  Jupyter notebooks that walk through experiments, explanations, and visualizations step by step.  
  Each notebook is self-contained and demonstrates a different perspective.

- **`src/svd_image_lab/`**  
  Isolated utility functions for Singular Value Decomposition (SVD) and image reconstruction.  
  These keep the math and algorithms reusable, clean, and easier to test or expand later.

- **`docs`**  
  Outlines core concepts discussed in the /givnotebooks and utilized in /src


---

## 🚀 Usage

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/svd-image-lab.git
cd svd-image-lab
```
2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Launch Jupyter Notebooks**

```bash
jupyter notebook notebooks/
```

4. **Explore the notebooks:**

- Open any notebook in the notebooks/ folder.
- Run cells sequentially to see explanations, visualizations, and SVD-based image processing in action.
- You can also import functions from src/svd_image_lab/ for your own experiments.