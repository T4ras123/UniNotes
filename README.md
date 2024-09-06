![image](https://github.com/user-attachments/assets/90b51f92-0871-4a93-a8d7-a0d056398864)
# UniNotes

Imagerecognition model for the app to help students learn. ML algorithm will recognize text from the
handwritten notes submitted by students and transcribe it to LaTex format for more convenient use.
Then another model will analyze the content and automatically sort them by theme enabling search
between all the files.

![Uploading image.png…](https://arxiv.org/pdf/2010.11929)


# Structure
```
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── .gitignore
├── data/
│   ├── raw/
│   ├── processed/
│   ├── external/
│   └── interim/
├── notebooks/
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── inference/
│   └── utils/
├── models/
│   └── model.pkl
├── reports/
│   ├── final_report.pdf
│   └── figures/
├── experiments/
│   └── experiment1/
├── config/
│   └── config.yaml
└── scripts/
```
