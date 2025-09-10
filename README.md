# RenderCV

RenderCV is a Python microservice for generating modern, ATS-friendly PDF résumés from structured JSON data.

## Features

- **FastAPI**: REST API for résumé generation.
- **Jinja2**: HTML templating for dynamic résumé content.
- **WeasyPrint**: Converts HTML/CSS to high-quality PDF output.
- **SCSS/CSS Grid Layouts**: Responsive, maintainable, and visually precise résumé sections (skills, education, experience, languages).
- **Semantic HTML**: Ensures accessibility and ATS compatibility.
- **Custom Jinja2 Filters**: e.g., `base_url` for clean URL display.
- **n8n Integration**: Easily connect to n8n workflows for automation (e.g., saving PDFs to Google Drive).

## Usage

1. **Run the API**

   - Start with: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

2. **Send a POST request to `/render-cv`**

   - Body: JSON with résumé data (see below for example)
   - Response: PDF file

3. **Integrate with n8n**
   - Use n8n's HTTP Request node to POST résumé data
   - Use Google Drive node to save the returned PDF

## Example JSON Payload

```json
{
  "name": "John Doe",
  "titles": ["Cognitive Scientist", "Data Engineer", "Software Engineer"],
  "profile": "Experienced AI engineer...",
  "competencies_and_skills": [
    { "competency": "Data Engineering", "skills": ["ETL", "SQL"] },
    { "competency": "Data Science", "skills": ["Bayesian Modeling"] }
  ],
  "education": [
    { "degree": "BSc Computer Science", "institution": "Uni", "year": "2017" }
  ],
  "contact_info": {
    "email": "john@example.com",
    "phone": "123-456-7890",
    "linkedin": "https://linkedin.com/in/johndoe",
    "github": "https://github.com/johndoe",
    "website_link": "https://johndoe.com?utm_source=api"
  },
  "work_experience": [
    {
      "position": "Developer",
      "company": "Acme",
      "years": "2018-2021",
      "roles": ["Built scalable APIs", "Led migration to cloud"]
    }
  ],
  "languages": [
    { "language": "Spanish", "level": "Native" },
    { "language": "English", "level": "C1" }
  ]
}
```

## Notes

- **PDF only**: WeasyPrint does not support `.doc`/`.docx` output.
- **Customization**: SCSS/CSS and Jinja2 templates are fully customizable for layout, branding, and ATS requirements.

## License

MIT
