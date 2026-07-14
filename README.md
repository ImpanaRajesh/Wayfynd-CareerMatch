# Wayfynd CareerMatch — AI Job Recommender System

An AI-powered resume analyzer and job recommender. Upload a resume (PDF), get an AI-generated summary, skill-gap analysis, and a personalized career roadmap — then pull matching live job listings from LinkedIn and Naukri.

Built with Streamlit, Groq (Llama 3.3 70B) for AI inference, and Apify for job scraping. Also includes an optional MCP server so the job-fetching tools can be used by MCP-compatible clients (e.g. Claude Desktop).


## Features


📥 Resume Upload — extracts text from any PDF resume using PyMuPDF
🧠 AI Resume Summary — highlights skills, education, and experience
🛠️ Skill Gap Analysis — identifies missing skills/certifications for better opportunities
🚀 Career Roadmap — suggests skills to learn, certifications, and industry exposure
💼 Live Job Search — fetches real job listings from LinkedIn and Naukri based on AI-extracted keywords from your resume
🔌 MCP Server — exposes job-fetching as tools for MCP clients



## Project Structure

Wayfynd-CareerMatch/
├── app.py                  # Streamlit app (main entry point)
├── mcp_server.py            # MCP server exposing job-fetch tools
├── src/
│   ├── helper.py            # PDF extraction + AI (Groq) calls
│   └── job_api.py           # LinkedIn & Naukri job fetching via Apify
├── .env                      # API keys (not committed)
├── requirements.txt
└── README.md


## Tech Stack

ComponentToolUIStreamlitAI InferenceGroq API (Llama 3.3 70B Versatile) — via OpenAI-compatible SDKPDF ParsingPyMuPDF (fitz)Job ScrapingApify (LinkedIn Jobs Scraper + Naukri Jobs Scraper actors)MCP IntegrationFastMCP


Note: This project uses Groq, not OpenAI, for AI inference — despite variable names like OpenAI and client being reused from the OpenAI Python SDK. Groq's API is OpenAI-compatible, so the same SDK works by pointing base_url at Groq's servers.



## Prerequisites


Python 3.12+
A free Groq API key
An Apify API token



## Setup & Installation

1. Clone the repository

bashgit clone <your-repo-url>
cd Wayfynd-CareerMatch

2. Create and activate a virtual environment

bashpython3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

3. Install dependencies

bashpip install -r requirements.txt

If you don't have a requirements.txt yet, create one with:

streamlit
PyMuPDF
python-dotenv
openai
apify-client
mcp

4. Configure environment variables

Create a .env file in the project root:

envGROQ_API_KEY=gsk_your_groq_api_key_here
APIFY_API_TOKEN=your_apify_api_token_here

5. Run the app

bashstreamlit run app.py

The app will open at http://localhost:8501.


## How It Works


Upload a resume (PDF) → text is extracted via extract_text_from_pdf().
AI analysis (ask_openai(), powered by Groq) generates:

A resume summary
A skill-gap analysis
A future career roadmap



Job keyword extraction — the AI condenses the resume summary into a comma-separated list of job search keywords.
Job fetching:

fetch_linkedin_jobs() builds a LinkedIn job-search URL from the keywords and calls the Apify LinkedIn Jobs Scraper actor.
fetch_naukri_jobs() calls the Apify Naukri Jobs Scraper actor directly with the keyword.



Results are rendered in the Streamlit UI with clickable job links.



## MCP Server (Optional)

mcp_server.py exposes two tools — fetchlinkedin and fetchnaukri — over the Model Context Protocol, so they can be called from any MCP-compatible client.

Run it standalone:

bashpython mcp_server.py

To connect it to Claude Desktop, add it to your MCP config (e.g. claude_desktop_config.json):

json{
  "mcpServers": {
    "job-recommender": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_server.py"]
    }
  }
}




## Notes


LinkedIn and Naukri scraping is done via third-party Apify actors — results depend on the actor's current schema and availability, and are subject to their scraping/rate limits.
Groq's Llama 3.3 70B model is used for all AI text generation (summary, gap analysis, roadmap, keyword extraction).
Store all API keys in .env — never commit them to version control.