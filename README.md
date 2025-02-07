# GSDNet：A Lightweight and Robust Detection Network for Diverse Glass Surface Defects via Scale- and Shape-Aware Feature Extraction
This is the official code of A Lightweight and Robust Detection Network for Diverse Glass Surface Defects via Scale- and Shape-Aware Feature Extraction.

# Glass Defect Dataset
We provide the download link for our custom dataset. For the open-source glass defect datasets, please refer to the original authors' download links.
| Dataset     | Type                           | Download Link |
|-------------|--------------------------------|---------------|
| SSGD        | Mobile Screen Glass Defects   | [Github](https://github.com/VincentHancoder/SSGD) |
| AiGD        | Aircraft Glass Defects        | [Github](https://github.com/core128/AGDD) |
| AuGD        | Automotive Glass Defects      | [Paper](https://pan.baidu.com/s/17zOqLvPzQ6-_7U6au4U_dw?pwd=itx4)|
| RSGD        | Recycled Mobile Screen Defects| [BaiduDisk](https://pan.baidu.com/s/17zOqLvPzQ6-_7U6au4U_dw?pwd=itx4) |
| CGD         | Construction Glass Defects    | [BaiduDisk](https://pan.baidu.com/s/17zOqLvPzQ6-_7U6au4U_dw?pwd=itx4) |

Please place the downloaded datasets in the following path:
- `dataset/`: Root directory for the dataset.
  - `SSGD/`: Contains the input glass defect images for the mobile screen dataset.
    - `annotations/`: Directory for the dataset annotations.
      - `instances_train.json`: COCO Annotation file for the training set.
      - `instances_val.json`: COCO Annotation file for the validation set.
    - `images/`: Directory for the training and validation images.
      - `train/`: Training images for the SSGD.
      - `val/`: Validation images for the SSGD.
    - `labels/`: Directory for the corresponding labels.
      - `train/`: Training labels for the SSGD.
      - `val/`: Validation labels for the SSGD.
    - `SSGD.yaml`: Configuration file for the SSGD dataset.
    ...
   
    
# GSDNet
## Code
### Setup
```
conda create -n GSDNet python==3.10
conda activate GSDNet
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu118
pip install ultralytics
```
### Train GSDNet
```
python train.py --dataset dataset/SSGD/SSGD.yaml --batch 64 --size m --imgsz 640
```
### Test
```
python val.py --anno_json dataset/SSGD/annotations/instances_val.json --save_path /path/to/save/results --model_weights /path/to/your/model/weights/best.pt
```

# Contact   
For any question, feel free to email <22225179@zju.edu.cn>

# Acknowledgments
We would like to thank the developers of [YOLO](https://github.com/ultralytics/ultralytics) for their open-source contributions, which greatly supported the development of our work.
Additionally, we would like to thank the following authors for their open-source contributions.
```

```
