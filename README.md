# UniNotes

Image recognition model for the app to help students learn. ML algorithm will recognize text from the
handwritten notes submitted by students and transcribe it to LaTex format for more convenient use.
Then another model will analyze the content and automatically sort them by theme enabling search
between all the files.




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
