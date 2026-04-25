import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make hero dark
content = content.replace('<div class="hero-video">', '<div class="hero-bg">')
if '<div class="hero-overlay"></div>' not in content:
    content = content.replace('</video>\n        </div>', '</video>\n        </div>\n        <div class="hero-overlay"></div>')

# Update buttons
content = content.replace('btn btn-secondary', 'btn btn-outline')

# Make sections dark
content = content.replace('<section class="stats">', '<section class="section section-dark stats">')
content = content.replace('<section id="about" class="about">', '<section id="about" class="section section-darker about">')
content = content.replace('<section class="solar-subsidiary">', '<section class="section section-dark solar-subsidiary">')
content = content.replace('<section id="projects" class="projects">', '<section id="projects" class="section section-darker projects">')
content = content.replace('<section id="services" class="services">', '<section id="services" class="section section-dark services">')
content = content.replace('<section id="contact" class="contact">', '<section id="contact" class="section section-darker contact">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
