import re

header = '''<!-- Navbar -->
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
</nav>'''

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

files = ['index.html', 'employees.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace navbar
    content = re.sub(r'<!-- Nav.*? -->.*?</nav>', header, content, flags=re.DOTALL)
    # Replace footer
    content = re.sub(r'<!-- Footer -->.*</html>', footer, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Done index and employees.")

