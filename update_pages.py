import re

header = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arslan Corporation</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🏗️%3C/text%3E%3C/svg%3E">
</head>
<body>

<!-- Navbar -->
<nav class="navbar" id="navbar">
    <div class="nav-container">
        <a href="index.html" class="nav-logo">
            <h2>ARSLAN CORPORATION</h2>
            <span>Architects • Engineers • Developers</span>
        </a>
        <ul class="nav-menu" id="navMenu">
            <li><a href="index.html#home" class="nav-link">Home</a></li>
            <li><a href="index.html#about" class="nav-link">About</a></li>
            <li><a href="index.html#expertise" class="nav-link">Expertise</a></li>
            <li><a href="index.html#projects" class="nav-link">Projects</a></li>
            <li><a href="employees.html" class="nav-link">Team</a></li>
            <li><a href="subsidiaries.html" class="nav-link">Subsidiaries</a></li>
            <li><a href="experience.html" class="nav-link">Experience</a></li>
            <li><a href="index.html#contact" class="nav-link">Contact</a></li>
        </ul>
        <div class="hamburger" id="hamburger">
            <span class="bar"></span><span class="bar"></span><span class="bar"></span>
        </div>
    </div>
</nav>

'''

footer = '''<!-- Footer -->
<footer class="footer">
    <div class="container">
        <div class="footer-grid">
            <div class="footer-brand">
                <h3>ARSLAN CORPORATION</h3>
                <p>Building tomorrow's infrastructure today. A leading construction company in Islamabad since 2004.</p>
                <div class="social-links">
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                    <a href="https://wa.me/923338568856"><i class="fab fa-whatsapp"></i></a>
                </div>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="index.html#about">About Us</a></li>
                    <li><a href="index.html#projects">Projects</a></li>
                    <li><a href="employees.html">Our Team</a></li>
                    <li><a href="subsidiaries.html">Subsidiaries</a></li>
                    <li><a href="experience.html">Experience</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Services</h4>
                <ul>
                    <li><a href="index.html#expertise">Bridge Construction</a></li>
                    <li><a href="index.html#expertise">Buildings</a></li>
                    <li><a href="index.html#expertise">Roads</a></li>
                    <li><a href="index.html#expertise">Parks & Playgrounds</a></li>
                    <li><a href="index.html#expertise">Wedding Marquees</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Contact</h4>
                <p><i class="fas fa-map-marker-alt"></i> 5 St 1, H-13, Islamabad</p>
                <p><i class="fas fa-phone"></i> <a href="tel:+923338568856">+92 333 8568856</a></p>
                <p><i class="fas fa-envelope"></i> <a href="mailto:info@arslancorporation.com">info@arslancorporation.com</a></p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Arslan Corporation. All rights reserved.</p>
            <p>Architects • Engineers • Developers</p>
        </div>
    </div>
</footer>

<script src="script.js"></script>
</body>
</html>'''

with open('temp_subs.txt', 'r', encoding='utf-16') as f:
    subs_content = f.read()

page_hero_subs = '''<!-- Page Hero -->
<section class="page-hero">
    <h1>Our <span>Subsidiaries</span></h1>
    <p>Expanding our expertise through specialized companies</p>
    <div class="breadcrumb">
        <a href="index.html">Home</a><span>/</span><span>Subsidiaries</span>
    </div>
</section>
'''

subs_content = re.sub(r'style="padding-top:\s*120px;"', 'class="section section-dark"', subs_content)

with open('subsidiaries.html', 'w', encoding='utf-8') as f:
    f.write(header.replace('<title>Arslan Corporation</title>', '<title>Our Subsidiaries — Arslan Corporation</title>') + page_hero_subs + subs_content + footer)

with open('temp_exp.txt', 'r', encoding='utf-16') as f:
    exp_content = f.read()

page_hero_exp = '''<!-- Page Hero -->
<section class="page-hero">
    <h1>Working <span>Experience</span></h1>
    <p>Our extensive experience working with leading organizations</p>
    <div class="breadcrumb">
        <a href="index.html">Home</a><span>/</span><span>Experience</span>
    </div>
</section>
'''

exp_content = re.sub(r'style="padding-top:\s*120px;"', 'class="section section-dark"', exp_content)

with open('experience.html', 'w', encoding='utf-8') as f:
    f.write(header.replace('<title>Arslan Corporation</title>', '<title>Experience — Arslan Corporation</title>') + page_hero_exp + exp_content + footer)

print("Done subs and exp.")
