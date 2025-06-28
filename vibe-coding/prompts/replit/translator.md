# Spanish ↔ English Translator - Replit

**Platform:** Replit  
**Difficulty:** Beginner (Low-code)  
**Duration:** 20-25 minutes

## 🎯 Project Goal
Build a language translation tool that converts between Spanish and English using AI APIs.

## 📋 Instructions

### Step 1: Access Replit
1. Go to [replit.com](https://replit.com)
2. Create a free account or sign in
3. Create a new Python project

### Step 2: Use This Prompt
Copy and paste the following prompt into Replit's AI assistant:

```
Create a Spanish-English translator using Python with the following requirements:

**Core Features:**
- Translate text from Spanish to English
- Translate text from English to Spanish
- Simple web interface using Flask
- Support for both individual words and sentences
- Error handling for invalid inputs

**Technical Requirements:**
- Use the Google Translate API or a free alternative
- Create a Flask web application
- Include HTML templates for the interface
- Add CSS styling for a clean look
- Handle API rate limits and errors

**User Interface:**
- Input text area for source text
- Language selection dropdown (Spanish ↔ English)
- Translate button
- Output area showing translated text
- Clear button to reset the form

**Code Structure:**
- main.py (Flask app)
- templates/index.html (web interface)
- static/style.css (styling)
- requirements.txt (dependencies)

Please include comments in Spanish and English to help beginners understand the code.
```

### Step 3: Setup Dependencies
Add these to your `requirements.txt`:
```
Flask==2.3.3
googletrans==4.0.0rc1
requests==2.31.0
```

### Step 4: Customize the Interface
1. Modify the HTML template for better styling
2. Add your own branding or colors
3. Include additional language options if desired
4. Add input validation

## 🎨 Enhancement Ideas

- **Voice Input:** Add speech-to-text functionality
- **History:** Save recent translations
- **Offline Mode:** Use local translation libraries
- **Multiple Languages:** Expand beyond Spanish/English
- **File Upload:** Translate text files

## 📱 Expected Output
A web application that:
- Translates text between Spanish and English
- Has a clean, user-friendly interface
- Handles errors gracefully
- Can be deployed and shared

## 🔗 Next Steps
After completing this project, you'll have:
- Experience with web development basics
- Understanding of API integration
- Foundation for more complex AI projects
- Portfolio piece demonstrating practical skills

## 🐛 Troubleshooting

**Common Issues:**
- API rate limits: Add delays between requests
- Character encoding: Ensure UTF-8 support
- CORS errors: Configure Flask properly
- Translation accuracy: Consider using multiple APIs

---

**💡 Pro Tip:** This project introduces you to web development concepts that will be essential for the AI Agents workshop! 