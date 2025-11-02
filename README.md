# 🧤 Glove vs Bare Hand Detection

This project detects **gloved** and **bare hands** in images using a custom-trained YOLOv8 model.

---

## 📁 Folder Structure

```
Part_1_Glove_Detection/
│
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
