from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Portfolio data - customize this for your client
PORTFOLIO_DATA = {
    "name": "Thushara Madushanka",
    "title": "Business Promotional Manager | MDRT Member 2025",
    "tagline": "MDRT Member 2025 | Emerald Club Member | 17th from AIA Alternate Agency | Strategic Financial Planning & Insurance Solutions",
    "email": "thushara.wishwanath@aia.com",
    "phone": "+94 77 123 4567",
    "address": "AIA Alternate Agency, Colombo, Sri Lanka",
    "years_experience": 8,
    "projects_completed": 500,
    "social": {
        "facebook": "#",
        "twitter": "#",
        "linkedin": "#",
        "instagram": "#",
        "github": "#"
    },
    "about": {
        "description": "I am proud to share that thanks to your unwavering trust and support, I have been recognized as a Member of the 2025 Million Dollar Round Table (MDRT) - a prestigious global recognition in the financial services industry. I am honored to be the 17th member from AIA Alternate Agency to achieve this milestone. This achievement belongs to you as much as it does to me. Your decision to trust me with your financial protection and future planning is what makes my work meaningful. I look forward to continuing our partnership and providing you with the best possible service in the years to come.",
        "services": ["MDRT Member 2025", "Emerald Club Member", "Business Promotional Manager"]
    },
    "skills": [
        {"name": "Financial Planning", "percentage": 95},
        {"name": "Insurance Advisory", "percentage": 90},
        {"name": "Client Relations", "percentage": 95},
        {"name": "Risk Assessment", "percentage": 85},
        {"name": "Business Development", "percentage": 90}
    ],
    "tools": ["AIA Systems", "Financial Analysis", "CRM", "MS Office", "Planning Tools", "Presentation"],
    "services": [
        {
            "icon": "fas fa-chart-line",
            "title": "Financial Planning",
            "description": "Comprehensive financial planning services to help you achieve your short-term and long-term financial goals."
        },
        {
            "icon": "fas fa-shield-alt",
            "title": "Life Insurance",
            "description": "Protect your loved ones with tailored life insurance solutions that provide security and peace of mind."
        },
        {
            "icon": "fas fa-heartbeat",
            "title": "Health Insurance",
            "description": "Comprehensive health coverage plans to ensure you and your family receive the best medical care."
        },
        {
            "icon": "fas fa-piggy-bank",
            "title": "Investment Planning",
            "description": "Strategic investment advisory services to help grow your wealth and secure your financial future."
        },
        {
            "icon": "fas fa-building",
            "title": "Business Insurance",
            "description": "Protect your business with comprehensive coverage solutions tailored to your industry needs."
        },
        {
            "icon": "fas fa-handshake",
            "title": "Consulting",
            "description": "Expert advice and guidance on insurance and financial matters to make informed decisions."
        }
    ],
    "projects": [
        {
            "id": 1,
            "title": "Family Protection Plan",
            "category": "insurance",
            "image": "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=600&h=400&fit=crop",
            "tools": ["Life Insurance", "AIA"],
            "link": "#"
        },
        {
            "id": 2,
            "title": "Corporate Insurance Package",
            "category": "business",
            "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&h=400&fit=crop",
            "tools": ["Business", "Group Plans"],
            "link": "#"
        },
        {
            "id": 3,
            "title": "Retirement Planning",
            "category": "investment",
            "image": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=600&h=400&fit=crop",
            "tools": ["Pension", "Savings"],
            "link": "#"
        },
        {
            "id": 4,
            "title": "Health Coverage Solutions",
            "category": "insurance",
            "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600&h=400&fit=crop",
            "tools": ["Health", "Medical"],
            "link": "#"
        },
        {
            "id": 5,
            "title": "Education Fund Planning",
            "category": "investment",
            "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600&h=400&fit=crop",
            "tools": ["Education", "Savings"],
            "link": "#"
        },
        {
            "id": 6,
            "title": "Wealth Management",
            "category": "investment",
            "image": "https://images.unsplash.com/photo-1565514020179-026b92b2d70b?w=600&h=400&fit=crop",
            "tools": ["Investment", "Growth"],
            "link": "#"
        }
    ],
    "testimonials": [
        {
            "name": "Kumara Perera",
            "role": "Business Owner",
            "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop",
            "text": "Thushara helped me understand the importance of proper insurance coverage for my business. His professional approach and clear explanations made the entire process smooth and hassle-free."
        },
        {
            "name": "Nimali Fernando",
            "role": "Teacher",
            "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop",
            "text": "I was looking for a comprehensive family protection plan, and Thushara provided exactly what we needed. His dedication to finding the right solution for our family was exceptional."
        },
        {
            "name": "Rajitha Silva",
            "role": "IT Professional",
            "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop",
            "text": "The retirement planning advice I received was invaluable. Thushara took the time to understand my goals and created a plan that gives me confidence about my future."
        }
    ],
    "pricing": [
        {
            "name": "Basic Plan",
            "price": 5000,
            "period": "month",
            "features": ["Life Coverage", "Accidental Coverage", "24/7 Support", "Annual Health Checkup", "Easy Claims Process"],
            "popular": False
        },
        {
            "name": "Family Plan",
            "price": 12000,
            "period": "month",
            "features": ["Family Life Coverage", "Health Insurance", "Critical Illness Cover", "Education Benefits", "Investment Component", "Premium Waiver"],
            "popular": True
        },
        {
            "name": "Premium Plan",
            "price": 25000,
            "period": "month",
            "features": ["Comprehensive Coverage", "Global Health Coverage", "Wealth Building", "Tax Benefits", "VIP Support", "Flexible Payments"],
            "popular": False
        }
    ],
    "blog": [
        {
            "id": 1,
            "title": "Why Life Insurance is Essential for Every Family",
            "date": "Jan 15, 2026",
            "author": "Thushara Madushanka",
            "image": "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=400&h=250&fit=crop",
            "excerpt": "Understanding the importance of life insurance in protecting your family's financial future."
        },
        {
            "id": 2,
            "title": "Planning for Your Child's Education",
            "date": "Jan 10, 2026",
            "author": "Thushara Madushanka",
            "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=400&h=250&fit=crop",
            "excerpt": "Smart strategies to save and invest for your children's educational expenses."
        },
        {
            "id": 3,
            "title": "Retirement Planning: Start Early, Retire Comfortably",
            "date": "Jan 05, 2026",
            "author": "Thushara Madushanka",
            "image": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=400&h=250&fit=crop",
            "excerpt": "Tips and strategies for building a secure retirement fund for a comfortable future."
        }
    ]
}


@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)


@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Here you would typically send an email or save to database
    # For now, we'll just return a success response
    return jsonify({
        'success': True,
        'message': 'Thank you for your message! I will get back to you soon.'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
