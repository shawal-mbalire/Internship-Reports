# Internship Reports

A collection of internship reports, project implementations, and academic work from various internships.

## Contents

- **GreenHub/** - MoMo API integration with Django for GreenHub transactions
- **marconi/** - Audio activity detection using voice activity detection (VAD)
- **netLabsEwaste/** - LaTeX report on e-waste management
- **AiLab/** - AI Lab internship report (LaTeX)
- **greenHubReport/** - GreenHub project report (LaTeX)

## Tech Stack

- **Languages**: Python, LaTeX
- **Frameworks**: Django, Django REST Framework
- **Libraries**: psycopg2, mtnmomoapi, torchaudio, inaSpeechSegmenter
- **Database**: PostgreSQL

## Setup (GreenHub API)

```bash
cd GreenHub/momoapi/greenhub_trx_django
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Configure PostgreSQL in `api/settings.py` and run migrations:
```bash
python manage.py migrate
python manage.py runserver
```

## Building LaTeX Reports

```bash
cd <report_directory>
pdflatex main.tex
pdflatex main.tex
```

## Author

Shawal Mbalire