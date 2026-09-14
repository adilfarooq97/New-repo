#!/usr/bin/env python3
"""
Setup script for AI LinkedIn Agent
Creates necessary directories and default config files
"""

import os
import json
import yaml
from pathlib import Path

def create_directories():
    """Create necessary directories"""
    dirs = [
        'agent',
        'content_backlog',
        'scripts',
        '.github/workflows'
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {dir_path}")

def create_config_files():
    """Create default configuration files if they don't exist"""
    
    # Default config.yaml
    config_path = Path('agent/config.yaml')
    if not config_path.exists():
        default_config = {
            'user': {
                'name': 'Frontend Developer',
                'persona': 'Frontend Developer working with HTML, Tailwind CSS, Angular, React, and TypeScript with a UI/UX focus',
                'voice': 'practical, conversational, clear, and useful'
            },
            'niches': [
                'Semantic HTML and Accessibility',
                'Tailwind CSS Design Systems',
                'Angular Application Architecture',
                'React Component Architecture',
                'TypeScript for Frontend Systems',
                'UI/UX Design and Product Thinking',
                'Frontend Performance Optimization',
                'Reliable User Interfaces'
            ],
            'posting': {
                'start_time': '09:00',
                'increment_hours': 24,
                'timezone': 'America/New_York'
            }
        }
        
        with open(config_path, 'w') as f:
            yaml.dump(default_config, f, default_flow_style=False, indent=2)
        print(f"✅ Created config file: {config_path}")
    
    # Default calendar.yaml
    calendar_path = Path('agent/calendar.yaml')
    if not calendar_path.exists():
        default_calendar = {
            'weekly_schedule': {
                '0': {  # Monday
                    'primary_topic': 'Semantic HTML and Accessibility',
                    'subtopics': ['Accessible landmarks', 'Keyboard-friendly interactions', 'Useful form errors'],
                    'post_type': 'lesson',
                    'series_length': 4
                },
                '1': {  # Tuesday
                    'primary_topic': 'Tailwind CSS Design Systems',
                    'subtopics': ['Responsive layout decisions', 'Reusable utility patterns', 'Design token consistency'],
                    'post_type': 'lesson',
                    'series_length': 4
                },
                '2': {  # Wednesday
                    'primary_topic': 'Angular and React Component Architecture',
                    'subtopics': ['Component boundaries', 'State ownership', 'Reusable UI contracts'],
                    'post_type': 'lesson',
                    'series_length': 4
                },
                '3': {  # Thursday
                    'primary_topic': 'TypeScript for Frontend Systems',
                    'subtopics': ['Typed API boundaries', 'Discriminated UI state', 'Safer component inputs'],
                    'post_type': 'lesson',
                    'series_length': 4
                },
                '4': {  # Friday
                    'primary_topic': 'UI/UX Design and Product Thinking',
                    'subtopics': ['Useful empty states', 'Recoverable error flows', 'Designing for user intent'],
                    'post_type': 'story',
                    'series_length': 4
                }
            },
            'post_templates': {
                'lesson': {
                    'title_template': '{topic}',
                    'body_template': 'A practical lesson from building {topic}.\n\nWhat I learned and how I apply it now.\n\n{hashtags}'
                },
                'story': {
                    'title_template': '{topic}',
                    'body_template': 'A frontend problem around {topic} taught me something useful.\n\nHere is the detail I now watch for.\n\n{hashtags}'
                }
            }
        }
        
        with open(calendar_path, 'w') as f:
            yaml.dump(default_calendar, f, default_flow_style=False, indent=2)
        print(f"✅ Created calendar file: {calendar_path}")
    
    # Default repo_queue.json
    queue_path = Path('agent/repo_queue.json')
    if not queue_path.exists():
        default_queue = {
            'pending_repos': []
        }
        
        with open(queue_path, 'w') as f:
            json.dump(default_queue, f, indent=2)
        print(f"✅ Created repo queue file: {queue_path}")
    
    # Default used_repos.json
    used_path = Path('agent/used_repos.json')
    if not used_path.exists():
        with open(used_path, 'w') as f:
            json.dump([], f, indent=2)
        print(f"✅ Created used repos file: {used_path}")

def create_env_template():
    """Create .env template file"""
    env_template_path = Path('.env.template')
    if not env_template_path.exists():
        template_content = """# Frontend LinkedIn Content Agent Environment Variables

# OpenRouter API (Required)
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=openai/gpt-4o-mini

# GitHub API (Optional, for repo posts)
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token_here

# LinkedIn Credentials (Required for posting)
LINKEDIN_EMAIL=your_linkedin_email@example.com
LINKEDIN_PASSWORD=your_linkedin_password

# Email Reporting (Optional)
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_password
EMAIL_RECEIVER=recipient@example.com

# Configuration (Optional)
ENABLE_POST=true
HEADLESS=false
LOG_LEVEL_CONSOLE=INFO
LOG_LEVEL_FILE=DEBUG
MIN_SEO_SCORE=70
MAX_LOW_SEO_ATTEMPTS=2
MAX_REGENERATION_ATTEMPTS=3
"""
        
        with open(env_template_path, 'w') as f:
            f.write(template_content)
        print(f"✅ Created environment template: {env_template_path}")

def main():
    """Run setup process"""
    print("🚀 Setting up AI LinkedIn Agent")
    print("=" * 40)
    
    try:
        create_directories()
        create_config_files()
        create_env_template()
        
        print("=" * 40)
        print("✅ Setup completed successfully!")
        print("\nNext steps:")
        print("1. Copy .env.template to .env and fill in your credentials")
        print("2. Customize agent/config.yaml with your preferences")
        print("3. Add repositories to agent/repo_queue.json if desired")
        print("4. Run: python health_check.py to validate setup")
        print("5. Test with: python run.py --dry-run --force")
        
    except Exception as e:
        print(f"❌ Setup failed: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())