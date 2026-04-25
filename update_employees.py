import re

with open('employees.html', 'r', encoding='utf-8') as f:
    content = f.read()

svg_avatar = '''<svg viewBox="0 0 24 24" fill="#333" xmlns="http://www.w3.org/2000/svg">
<path d="M12 12C14.7614 12 17 9.76142 17 7C17 4.23858 14.7614 2 12 2C9.23858 2 7 4.23858 7 7C7 9.76142 9.23858 12 12 12Z"/>
<path d="M12 14C8.13401 14 5 17.134 5 21H19C19 17.134 15.866 14 12 14Z"/>
</svg>'''

new_employees_list = f'''<div class="employees-list">

    <div class="employee-card-horizontal">
        <div class="employee-avatar-wrapper">
            {svg_avatar}
        </div>
        <div class="employee-info">
            <h3>Rana Arslan Munir</h3>
            <span class="role">Project Engineer</span>
            <p>Experienced project engineer with expertise in construction project management, technical planning, and execution of complex infrastructure projects.</p>
            <div class="employee-socials">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fas fa-envelope"></i></a>
                <a href="https://wa.me/923338568856"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
    </div>

    <div class="employee-card-horizontal">
        <div class="employee-avatar-wrapper">
            {svg_avatar}
        </div>
        <div class="employee-info">
            <h3>Abdullah Ahmed</h3>
            <span class="role">Marketing Officer</span>
            <p>Strategic marketing professional responsible for business development, client relations, and promoting Arslan Corporation's services across Pakistan.</p>
            <div class="employee-socials">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fas fa-envelope"></i></a>
                <a href="https://wa.me/923338568856"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
    </div>

    <div class="employee-card-horizontal">
        <div class="employee-avatar-wrapper">
            {svg_avatar}
        </div>
        <div class="employee-info">
            <h3>Noman</h3>
            <span class="role">Quantity Surveyor / Project Estimator</span>
            <p>Expert in cost estimation, quantity surveying, and project budgeting. Ensures accurate cost analysis and budget management for all construction projects.</p>
            <div class="employee-socials">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fas fa-envelope"></i></a>
                <a href="https://wa.me/923338568856"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
    </div>

    <div class="employee-card-horizontal">
        <div class="employee-avatar-wrapper">
            {svg_avatar}
        </div>
        <div class="employee-info">
            <h3>Irfan</h3>
            <span class="role">Electrical Engineer</span>
            <p>Specialized electrical engineer responsible for electrical systems design, installation, and maintenance across all construction projects.</p>
            <div class="employee-socials">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fas fa-envelope"></i></a>
                <a href="https://wa.me/923338568856"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
    </div>

    <div class="employee-card-horizontal">
        <div class="employee-avatar-wrapper">
            {svg_avatar}
        </div>
        <div class="employee-info">
            <h3>Abdul Malik</h3>
            <span class="role">Mechanical Engineer</span>
            <p>Expert mechanical engineer specializing in HVAC systems, mechanical installations, and equipment maintenance for construction projects.</p>
            <div class="employee-socials">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fas fa-envelope"></i></a>
                <a href="https://wa.me/923338568856"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
    </div>

    <div class="employee-card-horizontal">
        <div class="employee-avatar-wrapper">
            {svg_avatar}
        </div>
        <div class="employee-info">
            <h3>Abdur Rehman</h3>
            <span class="role">Architect</span>
            <p>Creative architect specializing in modern building designs and sustainable architecture. Leads design teams for residential and commercial projects.</p>
            <div class="employee-socials">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fas fa-envelope"></i></a>
                <a href="https://wa.me/923338568856"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
    </div>

</div>'''

content = re.sub(r'<div class="employees-grid">.*?</section>', new_employees_list + '</section>', content, flags=re.DOTALL)

with open('employees.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
