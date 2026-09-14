# LLM Integration (Frontend Content via OpenRouter)

## Overview
This agent generates short, practical LinkedIn posts for a frontend developer working with HTML, Tailwind CSS, Angular, React, TypeScript, and UI/UX.

## Setup
1. Create a `.env` file in the repository root:
   
   ```
   OPENROUTER_API_KEY=your_openrouter_key
   OPENROUTER_MODEL=openai/gpt-4o-mini
   ```

2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure `agent/repo_queue.json` has pending repos, and `agent/config.yaml` lists niche topics.

## How it works
- `agent/llm_generator.py` calls OpenRouter chat completions with prompts:
  - Repo posts: Includes name, description, README summary, topics, and URL.
   - Niche posts: Topic-focused stories about frontend engineering and user experience.
- The output is parsed to extract title, body, and up to 7 hashtags.
- SEO metrics are computed via `seo_optimizer.py`.

## Fallbacks
If the API call fails or no key is set, generation falls back to local templates.

## Security
- API keys are loaded from environment or `.env` (dotenv). Do not commit `.env`.