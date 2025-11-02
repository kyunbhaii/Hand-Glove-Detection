from ultralytics import YOLO
from pathlib import Path
import argparse
import json  

parser = argparse.ArgumentParser(description="Glove Detection Inference")
parser.add_argument('-i', '--input', type=str, required=True, help="Path to input images")
parser.add_argument('-o', '--output', type=str, required=True, help="Path to save annotated images")
parser.add_argument('-l', '--logs', type=str, default="logs", help="Path to save JSON logs")
parser.add_argument('-c', '--confidence', type=float, default=0.25, help="Confidence threshold")
args = parser.parse_args()

run_inference_spec(
    weights="runs/glove_vs_bare_yolov8n/weights/best.pt",  # ✅ correct for your Drive folder
    source=args.input,
    out_dir=args.output,
    logs_dir=args.logs,
    conf=args.confidence,
    imgsz=640
)
