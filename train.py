import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="Train a GSDNet model")
    parser.add_argument('--dataset', type=str, required=True, help='Path to dataset YAML file')
    parser.add_argument('--batch', type=int, required=True, help='Batch size for training')
    parser.add_argument('--size', type=str, choices=['n', 's', 'm', 'l'], required=True, help='Model size (n, s, m, l)')
    parser.add_argument('--imgsz', type=int, required=True, help='Input image size for training')

    args = parser.parse_args()

    project = f"runs/detect/gsdnet_{args.size}"
    model_path = f'ultralytics/cfg/models/glass/GSDNet{args.size}.yaml'

    model = YOLO(model_path)

    model.train(
        data=args.dataset,
        epochs=150,
        imgsz=args.imgsz,
        batch=args.batch,
        project=project,
        amp=True
    )


if __name__ == "__main__":
    main()

