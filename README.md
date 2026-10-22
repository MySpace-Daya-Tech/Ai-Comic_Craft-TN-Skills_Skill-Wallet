ComicCraft — AI Comic Story Creator
ComicCraft is a web application prototype that helps turn a story idea into a panel-by-panel comic. Users provide a story prompt, main character, setting, tone, art style, and panel count. The application creates structured story text, attempts to generate illustrations, displays a browser preview, and can export the comic as a PDF.
Important: ComicCraft can use fallback story text and placeholder images when AI components are unavailable. A placeholder is not an AI-generated illustration. Review generated content before sharing or publishing it.

Abstract
ComicCraft explores how generative AI can support a simple comic-creation workflow. A FastAPI backend receives the user's creative preferences and uses the Google Gen AI SDK to request structured story content from Gemini when a valid API key is configured. The story is organized into panels containing a title, narration, dialogue, and an image prompt. A Hugging Face Diffusers Stable Diffusion pipeline is used to attempt local illustration generation. The web interface displays each panel and provides a PDF export action, with FPDF assembling the panel images and text. Fallback story templates and placeholder PNG generation allow the basic interface and export workflow to be exercised when some AI components are not available. The project demonstrates integration of Python web development, generative AI, frontend scripting, image processing, and document generation. Actual results depend on API access, compatible dependencies, model availability, and computing resources.

Features

- FastAPI backend
- HTML/CSS/JavaScript frontend
- Gemini-powered story generation
- Stable Diffusion image generation
- Tone selection
- Art-style selection
- 2–8 comic panels
- Panel-by-panel preview
- PDF export using FPDF
- Built-in fallback mode for testing without AI APIs/models

## Project structure

```text
ComicCraft/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── services/
│   ├── story_generator.py
│   ├── image_generator.py
│   └── exporters.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── generated/
```

## 1. Create virtual environment

Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell activation is blocked:

```cmd
venv\Scripts\activate
```

Then:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Python version

Python 3.12 is a conservative choice for Diffusers/PyTorch compatibility. If Python 3.14 is already installed, you can try it first, but if PyTorch/Diffusers reports compatibility or wheel errors, use Python 3.12.

## 2. Run the application

```powershell
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## 3. Gemini setup

Set the API key in your terminal:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
$env:GEMINI_MODEL="gemini-3.8-flash"
uvicorn app:app --reload
```

Never expose your real API key in frontend JavaScript or GitHub.

If no Gemini API key is supplied, the app uses a deterministic local story fallback.

## 4. Stable Diffusion

The first time Diffusers loads a model, it may download a large model from Hugging Face. A CUDA-capable NVIDIA GPU is strongly recommended for practical local generation.

If the Diffusers/PyTorch stack is not available or cannot initialize, ComicCraft automatically creates preview placeholder PNGs so that the rest of the application and PDF workflow can still be tested.

For production image generation, use a suitable licensed model and follow its Hugging Face/model-card terms.

## 5. Complete workflow

1. Enter story prompt.
2. Enter character name.
3. Enter setting.
4. Select tone.
5. Select art style.
6. Select panel count.
7. Click Generate Comic.
8. Gemini creates the storyline.
9. Stable Diffusion creates panel images.
10. Frontend displays the comic.
11. Click Download PDF.
12. FPDF assembles each image, title, narration and dialogue into the PDF.

## 6. API endpoints

### GET /

Web interface.

### GET /health

Health check.

### POST /api/generate

Generates the story and panel images.

Form fields:

```text
prompt
character_name
setting
tone
art_style
panels
```

### POST /api/export

Creates the final PDF.

Form fields:

```text
comic_id
title
panels_json
```

## 7. Production improvements

For a production system, add:

- User authentication
- Database for comic projects
- Cloud object storage for images
- Background jobs/queues for image generation
- GPU inference service
- Rate limiting
- Prompt/content moderation
- Image safety filtering
- Model licensing verification
- Per-user quotas
- Secure API-key management
- Cleanup/retention jobs for generated files
- Automated tests
- Logging and monitoring
- Pagination for large projects


Features
- Browser-based comic creation form.
- Inputs for story prompt, character name, setting, tone, art style, and panel count.
- Gemini-based structured story generation when configured.
- Template-based fallback story generation.
- Stable Diffusion image generation through Diffusers when the pipeline is available.
- Placeholder PNGs when the Diffusers/PyTorch imports are unavailable.
- Panel preview with titles, narration, dialogue, and images.
- PDF export using FPDF.
- Health-check endpoint and FastAPI interactive API documentation.
  
Technology Stack
Component	Technology	Purpose
Backend/API	Python, FastAPI, Uvicorn	HTTP routes and application server
Story generation	Google Gen AI SDK, Gemini	Structured story and panel text
Image generation	Hugging Face Diffusers, Stable Diffusion, PyTorch	Panel illustrations
Frontend	HTML, CSS, JavaScript	User form and comic preview
Templates	Jinja2	Render the HTML page
Image processing	Pillow	PNG fallback and PDF image conversion
PDF export	FPDF	Build downloadable comic PDF


Project Structure
The main implementation documented here is in ComicCraft/.
ComicCraft/
├── app.py
├── requirements.txt
├── README.md
├── services/
│   ├── story_generator.py
│   ├── image_generator.py
│   └── exporters.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── generated/        # generated images and PDF files

Repository note: The repository also contains root-level app.py, services/, static/, and related files that overlap with ComicCraft/. To avoid confusion, follow the commands below from inside ComicCraft/. The separate root-level app/ folder appears to be an auxiliary/test entry point, not the documented main workflow.
Prerequisites
- Python version compatible with the installed PyTorch and Diffusers packages. Python 3.12 is a reasonable starting point if dependency installation fails on a newer Python version.
- Internet access for installing dependencies, accessing Gemini, and downloading the Stable Diffusion model when needed.
- A Google Gemini API key for Gemini-powered story generation.
- Sufficient disk space and RAM. A compatible CUDA-enabled NVIDIA GPU is recommended for practical local image generation; CPU generation may be slow.
  
Installation (Windows PowerShell)
Open PowerShell in the repository folder, then enter the main application directory:
cd ComicCraft
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
If PowerShell blocks virtual-environment activation, use Command Prompt:
cd ComicCraft
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
Start the application from the ComicCraft/ directory:
uvicorn app:app --reload

Open the application at:
- Web interface: http://127.0.0.1:8000
- API documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

Configure Gemini
In the same PowerShell window, set your API key before starting the server:
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
$env:GEMINI_MODEL="MODEL_NAME_SUPPORTED_BY_YOUR_GEMINI_API_ACCESS"
uvicorn app:app --reload
Replace both placeholder values with valid configuration for your account. Do not paste a real key into source code, HTML, JavaScript, screenshots, or a public GitHub commit. If the key or Google Gen AI SDK is unavailable, the story service uses its fallback template. API/network exceptions may still need additional handling.

How to Use
1. Open the local web interface.
2. Enter a story idea.
3. Enter the main character name and setting.
4. Choose a tone and art style.
5. Choose a panel count (2, 4, 6, or 8).
6. Select Generate Comic and wait for the response.
7. Review each panel's image, title, narration, and dialogue.
8. Select Download PDF to export the comic.
  
Workflow
1. The frontend submits the form to POST /api/generate.
2. FastAPI bounds the panel count to 2–8 and passes the inputs to the story service.
3. The story service requests structured JSON from Gemini, or creates fallback story content.
4. The image service attempts to generate a PNG for each panel with Stable Diffusion.
5. The backend stores images under generated/ and returns panel data and image URLs.
6. JavaScript renders the comic preview.
7. The frontend sends panel data to POST /api/export.
8. FPDF assembles the available images and text into a downloadable PDF.
   
API Endpoints
Method	Endpoint	Purpose
GET	/	Main web interface
GET	/health	Basic service health response
POST	/api/generate	Generate story and panel images
POST	/api/export	Create and return the PDF
GET	/docs	Interactive API documentation provided by FastAPI
POST /api/generate accepts prompt, character_name, setting, tone, art_style, and panels as form fields.
POST /api/export accepts comic_id, title, and panels_json.

Testing Checklist
Before submitting or demonstrating the project, verify the following on your own computer:
- [ ] The app starts without import or dependency errors.
- [ ] The home page and static assets load.
- [ ] /health returns a healthy status.
- [ ] A request produces the expected number of panels.
- [ ] The no-key story fallback works.
- [ ] You can distinguish real model-generated images from placeholder previews.
- [ ] The PDF downloads and opens correctly.
- [ ] Invalid panel JSON returns an error instead of crashing the request.
Do not report tests as passed until you have run them and observed the results.

Known Limitations
- Gemini API/network errors are not comprehensively caught in the current story-generation service Sometimes.
- The image service creates placeholders when its imports are unavailable, but model-download or pipeline-initialization failures may still interrupt generation.
- Local Stable Diffusion can require substantial memory, storage, and compute.
- Character appearance may vary between panels, and image models may not render text reliably.
- PDF text is converted to Latin-1, so some non-Latin characters may be replaced.
- The repository currently contains duplicate/overlapping application files at the root and inside ComicCraft/; keep one clearly documented entry point.
- Authentication, database-backed project storage, cloud asset storage, rate limiting, automated tests, and production monitoring are not included in the current prototype.
