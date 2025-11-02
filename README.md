# 🧤 Glove vs Bare Hand Detection

This project detects **gloved** and **bare hands** in images using a custom-trained YOLOv8 model.

---

## 📁 Folder Structure

```
├── Glove_Detection.ipynb     # Jupyter notebook for training, validation, and testing
├── CLI_inference.py           # Command-line script for running inference
│
├── runs/                      # YOLOv8 auto-generated training outputs
│   └── glove_vs_bare_yolov8n/
│       └── weights/
│           ├── best.pt        # Best performing model checkpoint
│           └── last.pt        # Last saved checkpoint
│
├── output/                    # Annotated images generated during inference
│
├── logs/                      # Per-image JSON logs (filename, detections, bbox, confidence)
│
└── README.md                  # Project documentation (this file)
```

---

## 🚀 How to Run Inference via CLI

### 1️⃣ Requirements

Install dependencies (Python ≥ 3.11 recommended):
```bash
pip install ultralytics opencv-python-headless torch torchvision torchaudio
```

---

### 2️⃣ Command Example

Run inference directly from the terminal:
```bash
python CLI_inference.py \
  -i "path/to/input_images" \
  -o "path/to/output_folder" \
  -l "path/to/logs_folder" \
  -c 0.25
```

**Arguments**
| Flag | Description |
|------|--------------|
| `-i` or `--input` | Path to folder containing input images |
| `-o` or `--output` | Folder to save annotated output images |
| `-l` or `--logs` | Folder to save JSON detection logs |
| `-c` or `--confidence` | Confidence threshold (default: 0.25) |

---

## 🧠 About the Model

- **Model:** YOLOv8n (fine-tuned on glove vs bare hand dataset)  
- **Classes:** `glove_hand`, `bare_hand`  
- **Framework:** Ultralytics YOLOv8  
- **Dataset:** Exported from Roboflow, annotated for binary classification of hand states

---

## 📊 Dataset Details

- **Dataset name:** Glove-Hand-and-Bare-Hand  
- **Source:** [Roboflow Dataset ↗](https://app.roboflow.com/glove-detection-3vldq/glove-hand-and-bare-hand-zwvif/1)  
- **Classes:** `glove_hand`, `bare_hand` 
- **Split:**  
  - Train → 82%  
  - Validation → 16%  
  - Test → 2%  
- **Format:** YOLOv8 (images + labels + `data.yaml`) 

---

## 💡 What Worked
- Rebalanced dataset and removed unrelated “only glove” class → improved mAP & recall
- Training directly from Google Drive ensured model weights were not lost between Colab sessions
- Label mapping in inference standardized JSON output as gloved_hand / bare_hand
- Smaller YOLOv8n model gave faster inference with decent accuracy

## ⚠️ What Didn’t Work (and Fixes)

| Issue | Cause | Fix |
|-------|--------|-----|
| Dataset not loading | Folder paths were wrong after download | Fixed file paths in `data.yaml` - Adjusted to relative paths (`../train/images`, etc.) |
| Only glove images in validation | Random split created imbalance | Rebalanced dataset in Roboflow |
| Inference was slow on CPU | YOLOv8 defaulted to CPU mode | Switched to GPU runtime for faster processing |

---

## 🧩 Output Format

Each inference produces:
1. Annotated image (saved to `output/`)
2. Corresponding JSON file (saved to `logs/`) with the structure:
```json
{
  "filename": "image1.jpg",
  "detections": [
    {"label": "gloved_hand", "confidence": 0.92, "bbox": [x1, y1, x2, y2]},
    {"label": "bare_hand", "confidence": 0.85, "bbox": [x1, y1, x2, y2]}
  ]
}
```

---

## 📬 Notes
- Trained weights (`best.pt`) are located in `runs/glove_vs_bare_yolov8n/weights/`.  
- Works seamlessly with YOLOv8 for both local and Colab environments.  
- You can retrain or fine-tune using `Glove_Detection.ipynb`.
