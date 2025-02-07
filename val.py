import argparse
from ultralytics import YOLO
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

def main():
    parser = argparse.ArgumentParser(description="Evaluate model on a given dataset and calculate COCO metrics")
    parser.add_argument('--anno_json', type=str, required=True, help='Path to the annotation JSON file')
    parser.add_argument('--save_path', type=str, required=True, help='Directory to save results')
    parser.add_argument('--model_weights', type=str, required=True, help='Path to the model weights file')

    args = parser.parse_args()

    model = YOLO(args.model_weights)  
    
    metrics = model.val(save_json=True, project=args.save_path, name=args.model_weights) 

    anno_json = args.anno_json
    pred_json = f"{args.save_path}/{args.model_weights}/predictions.json"

    anno = COCO(anno_json)
    pred = anno.loadRes(pred_json) 

    eval = COCOeval(anno, pred, 'bbox')
    eval.evaluate()
    eval.accumulate()
    eval.summarize()

if __name__ == "__main__":
    main()

