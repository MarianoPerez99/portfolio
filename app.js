// Dynamic skill addition
document.addEventListener('DOMContentLoaded', () => {
    const skillsContainer = document.getElementById('skills-container');
    const additionalSkills = [
        'MS SQL Server', 
        'Netezza',
        'Data Warehouse',
        'Data Visualization',
        'Business Intelligence',
        'Pandas',
        'Numpy',
        'Agile Methodologies'
    ];

    const colorClasses = [
        'bg-blue-100 text-blue-800',
        'bg-green-100 text-green-800',
        'bg-purple-100 text-purple-800',
        'bg-red-100 text-red-800',
        'bg-yellow-100 text-yellow-800',
        'bg-indigo-100 text-indigo-800',
        'bg-pink-100 text-pink-800',
        'bg-gray-100 text-gray-800'
    ];

    additionalSkills.forEach((skill, index) => {
        const skillElement = document.createElement('span');
        const colorClass = colorClasses[index % colorClasses.length];
        skillElement.className = `${colorClass} px-3 py-1 rounded-full text-sm`;
        skillElement.textContent = skill;
        skillsContainer.appendChild(skillElement);
    });
});

// Smooth scroll and interaction effects
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
