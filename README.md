# UniNotes

Image recognition model for the app to help students learn. ML algorithm will recognize text from the
handwritten notes submitted by students and transcribe it to LaTex format for more convenient use.
Then another model will analyze the content and automatically sort them by theme enabling search
between all the files.

![image](https://github.com/user-attachments/assets/2bb56bd0-53f7-4858-8a95-d49393f8bc25)

## Structure

```bash
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── .gitignore
├── data/
│   └── external/
├── notebooks/
├── LaTeX-TrOCR/
|   ├── utils/
│   └── dataset/
├── config/
|   └── config.yaml
└── docker/
```
