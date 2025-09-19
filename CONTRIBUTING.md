# 🤝 Contributing to AI Poem Generator

First off, thank you for considering contributing to the AI Poem Generator! It's people like you that make this project a great learning resource and portfolio piece.

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

## 🌟 Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. Please be respectful and constructive in all interactions.

### Our Standards
- ✅ **Be respectful** to all contributors regardless of experience level
- ✅ **Provide constructive feedback** and be open to receiving it
- ✅ **Focus on the project** and avoid personal attacks
- ✅ **Help others learn** by explaining your suggestions and decisions

## 🚀 Getting Started

### Prerequisites
Before contributing, make sure you have:
- Python 3.8+ installed
- Git configured with your GitHub account
- Basic understanding of Flask and web development
- Familiarity with AI APIs (OpenAI/Ollama) is helpful but not required

### Quick Setup
```bash
# 1. Fork and clone the repository
git clone https://github.com/yourusername/ollama-app.git
cd ollama-app

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment
cp .env.example .env
# Edit .env with your configuration

# 5. Test the application
python server.py
```

## 💡 How Can I Contribute?

### 🐛 Reporting Bugs
If you find a bug, please create an issue with:
- **Clear title** describing the problem
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, browser)
- **Screenshots** if applicable

### ✨ Suggesting Enhancements
We welcome feature suggestions! Please include:
- **Clear description** of the enhancement
- **Use case** - why would this be useful?
- **Implementation ideas** if you have them
- **Examples** from other projects if relevant

### 📝 Documentation Improvements
Help make our docs better by:
- Fixing typos or unclear explanations
- Adding examples or use cases
- Improving code comments
- Creating tutorials or guides

### 🔧 Code Contributions
Areas where contributions are especially welcome:

#### 🎨 Frontend Enhancements
- Improved UI/UX design
- Mobile responsiveness improvements
- Accessibility features
- Interactive elements

#### ⚡ Backend Features
- Additional AI model support
- Performance optimizations
- Error handling improvements
- API endpoint additions

#### 🧪 Testing
- Unit test coverage
- Integration tests
- Performance benchmarks
- User acceptance tests

#### 🚀 DevOps & Deployment
- Docker configuration
- Cloud deployment guides
- CI/CD improvements
- Monitoring solutions

## 🛠️ Development Setup

### Local Development
```bash
# Start development server with auto-reload
export FLASK_ENV=development
python server.py

# The app will be available at http://localhost:3000
```

### Environment Variables
```bash
# Required for development
OPENAI_API_KEY=your_key_here          # Get from OpenAI
LLM_ENDPOINT=https://api.openai.com/v1
MODEL=gpt-3.5-turbo

# Optional for development
PORT=3000
FLASK_ENV=development
FLASK_DEBUG=True
```

### Testing Your Changes
```bash
# Basic functionality test
python -c "from server import app; print('✅ Import successful')"

# Manual testing checklist:
# - Application starts without errors
# - Main page loads correctly
# - Form accepts input
# - AI generation works (or shows appropriate error)
# - Response is displayed properly
```

## 🔄 Pull Request Process

### Before You Submit
1. **Create a feature branch** from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** with clear, focused commits
   ```bash
   git add .
   git commit -m "feat: add poem export functionality"
   ```

3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Follow the style guidelines** below

### Pull Request Guidelines
- **Use a clear title** that describes what the PR does
- **Fill out the PR template** (if available)
- **Link related issues** using `Fixes #123` or `Relates to #123`
- **Keep PRs focused** - one feature or fix per PR
- **Include tests** for new functionality
- **Update docs** for user-facing changes

### PR Review Process
1. **Automated checks** must pass (CI/CD pipeline)
2. **Code review** by project maintainers
3. **Testing** in a staging environment
4. **Approval and merge** by maintainers

## 📏 Style Guidelines

### Python Code Style
We follow PEP 8 with some preferences:

```python
# ✅ Good
def generate_poem(prompt: str) -> str:
    """Generate a poem using AI based on the given prompt."""
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    # Implementation here
    return poem

# ❌ Avoid
def generatePoem(prompt):
    if prompt=="":
        return None
```

### Key Conventions
- **Line length**: 88 characters (Black formatter standard)
- **Imports**: Standard library, third-party, local imports
- **Docstrings**: Use for all public functions
- **Type hints**: Preferred for new code
- **Error handling**: Explicit and informative

### Frontend Guidelines
- **Responsive design**: Mobile-first approach
- **Accessibility**: Use semantic HTML and ARIA labels
- **Performance**: Optimize images and minimize CSS/JS
- **Consistency**: Follow existing design patterns

### Documentation Style
- **Clear headings** with emoji for visual appeal
- **Code examples** with syntax highlighting
- **Step-by-step instructions** for complex processes
- **Screenshots** for UI-related changes

### Commit Message Format
```bash
# Format: <type>(<scope>): <description>
# Types: feat, fix, docs, style, refactor, test, chore

feat(ui): add dark mode toggle
fix(api): handle empty responses from AI service
docs(readme): update installation instructions
test(server): add unit tests for poem generation
```

## 🗂️ Project Structure

Understanding the codebase:

```
ollama-app/
├── server.py              # 🚀 Main Flask application
├── requirements.txt       # 📦 Python dependencies  
├── .env.example          # ⚙️ Environment template
├── .github/workflows/    # 🔄 CI/CD pipelines
├── docs/                 # 📚 Documentation
└── tests/               # 🧪 Test files (future)
```

### Key Files to Know
- **`server.py`** - Main application logic, routes, and AI integration
- **`requirements.txt`** - Python package dependencies
- **`.env.example`** - Configuration template for environment variables
- **`README.md`** - Main project documentation
- **`COMPLETE_PROJECT_GUIDE.md`** - Comprehensive development guide

## 🧪 Testing Guidelines

### Manual Testing Checklist
Before submitting a PR, test these scenarios:

#### Basic Functionality
- [ ] Application starts without errors
- [ ] Main page loads and displays correctly
- [ ] Input form accepts text
- [ ] Submit button triggers generation
- [ ] Results display properly formatted
- [ ] Error messages show for invalid input

#### AI Integration
- [ ] OpenAI API integration works
- [ ] Ollama integration works (if configured)
- [ ] Error handling for API failures
- [ ] Appropriate responses for different prompts

#### Cross-Platform
- [ ] Works on different browsers (Chrome, Firefox, Safari)
- [ ] Mobile responsive design
- [ ] Different screen sizes
- [ ] Touch interactions work properly

### Future Testing Framework
We're planning to add:
- Unit tests with pytest
- Integration tests for AI services
- Frontend tests with Selenium
- Performance benchmarking

## 🚀 Deployment Testing

If your changes affect deployment:

### Local Testing
```bash
# Test with production-like settings
export FLASK_ENV=production
export FLASK_DEBUG=False
python server.py
```

### Docker Testing (Future)
```bash
# When Docker support is added
docker build -t ollama-app .
docker run -p 3000:3000 ollama-app
```

## 📞 Getting Help

### Documentation
- **README.md** - Quick start and basic usage
- **COMPLETE_PROJECT_GUIDE.md** - Comprehensive development guide
- **DEPLOYMENT_GUIDE.md** - Deployment instructions

### Community Support
- **GitHub Issues** - For bugs and feature requests
- **GitHub Discussions** - For questions and community chat
- **Code Review** - Learn from PR feedback

### Maintainer Contact
- **GitHub**: [@romancete85](https://github.com/romancete85)
- **Response Time**: Usually within 48 hours
- **Best Practices**: Use GitHub issues for project-related questions

## 🎯 Recognition

Contributors will be recognized:
- **README.md** - Listed in contributors section
- **GitHub** - Automatic contribution graph
- **Releases** - Mentioned in release notes
- **Learning** - Gain experience with modern web development

## 📜 License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

## 🙏 Thank You

Every contribution, no matter how small, helps make this project better for everyone. Whether you're:
- 🐛 Fixing a typo
- ✨ Adding a new feature  
- 📚 Improving documentation
- 🧪 Writing tests
- 💡 Sharing ideas

Your efforts are appreciated and help create a valuable learning resource for the community!

---

**Happy Contributing!** 🚀

*Last updated: 2025-09-19*