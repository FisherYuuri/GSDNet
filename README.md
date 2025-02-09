# GSDNet：A Lightweight and Robust Detection Network for Diverse Glass Surface Defects via Scale- and Shape-Aware Feature Extraction
This is the official code of A Lightweight and Robust Detection Network for Diverse Glass Surface Defects via Scale- and Shape-Aware Feature Extraction.

# Glass Defect Dataset
We provide the download link for our custom dataset. For the open-source glass defect datasets, please refer to the original authors' download links.
| Dataset     | Type                           | Download Link |
|-------------|--------------------------------|---------------|
| SSGD        | Mobile Screen Glass Defects   | [Github](https://github.com/VincentHancoder/SSGD) |
| AiGD        | Aircraft Glass Defects        | [Github](https://github.com/core128/AGDD)\|[BaiduDisk](https://pan.baidu.com/s/1ZgFMBykpl2OInRYTULn9xQ?pwd=we24) |
| AuGD        | Automotive Glass Defects      | [Paper](https://link.springer.com/article/10.1007/s00371-023-03225-x)|
| RSGD        | Recycled Mobile Screen Defects| [BaiduDisk](https://pan.baidu.com/s/1d3F1-1EQ3LcBOYfLZVMFrw?pwd=9c4v) |
| CGD         | Construction Glass Defects    | [BaiduDisk](https://pan.baidu.com/s/1wkaY7qSshOxYLzn0uVEENw?pwd=a2n4) |

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
### Test GSDNet
```
python val.py --anno_json dataset/SSGD/annotations/instances_val.json --save_path /path/to/save/results --model_weights /path/to/your/model/weights/best.pt
```

# Contact   
For any question, feel free to email <22225179@zju.edu.cn>

# Acknowledgments
We would like to thank the developers of [YOLO](https://github.com/ultralytics/ultralytics) for their open-source contributions, which greatly supported the development of our work.
Additionally, we would like to thank the following authors for their open-source contributions.
```
@article{chen2024defect,
  title={Defect detection in automotive glass based on modified YOLOv5 with multi-scale feature fusion and dual lightweight strategy},
  author={Chen, Zhe and Huang, Shihao and Lv, Hui and Luo, Zhixue and Liu, Jinhao},
  journal={The Visual Computer},
  pages={1--14},
  year={2024},
  publisher={Springer}
}
```
```
@inproceedings{han2023ssgd,
  title={SSGD: A smartphone screen glass dataset for defect detection},
  author={Han, Haonan and Yang, Rui and Li, Shuyan and Hu, Runze and Li, Xiu},
  booktitle={ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={1--5},
  year={2023},
  organization={IEEE}
}
```
```
@article{li2024dual,
  title={Dual-Modal Illumination System for Defect Detection of Aircraft Glass Canopies},
  author={Li, Zijian and Yao, Yong and Wen, Runyuan and Liu, Qiyang},
  journal={Sensors},
  volume={24},
  number={20},
  pages={6717},
  year={2024},
  publisher={MDPI}
}
```
