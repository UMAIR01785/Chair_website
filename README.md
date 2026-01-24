# 🛋️ Sofa Website - E-commerce Platform

A modern, full-featured e-commerce website built with Django for selling furniture and home decor items. This project features a clean, responsive design with a comprehensive product catalog, shopping cart, blog system, and more.

![Django](https://img.shields.io/badge/Django-6.0.1-green.svg)
![Python](https://img.shields.io/badge/Python-3.14.2-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### 🏠 Home Page
- Hero section with featured products
- Featured product showcase (limit 3 products)
- Recent blog posts section
- About section preview
- Fully responsive design

### 🛍️ E-Commerce Features
- **Product Catalog**: Browse all available furniture products
- **Product Details**: Detailed product pages with:
  - Product images
  - Pricing information
  - Stock availability
  - Add to cart functionality
- **Shopping Cart**:
  - Add/remove items
  - Update quantities
  - Real-time subtotal calculations
  - Session-based cart management
- **Order Management**: Place and track orders

### 📝 Blog System
- **Blog Listing**: Grid layout showing all blog posts
- **Blog Detail Pages**: 
  - Full blog content with rich text support
  - Featured post badges
  - Author information and publish dates
  - Social media sharing options
  - Responsive image handling
- **Featured Blogs**: Mark blogs as featured

### 👥 About Section
- Team management showcase
- Display team members with:
  - Photos
  - Names and positions
  - Bio information

### 🎨 Design Features
- Modern, clean UI with green (#3b5d50) and yellow (#f9bf29) color scheme
- Fully responsive design (mobile, tablet, desktop)
- Bootstrap 5 integration
- Font Awesome icons
- Custom CSS with smooth transitions and hover effects
- Consistent styling across all pages

## 🛠️ Technology Stack

### Backend
- **Django 6.0.1** - Web framework
- **Python 3.14.2** - Programming language
- **PostgreSQL** - Production database
- **psycopg2-binary 2.9.11** - PostgreSQL adapter
- **Pillow 12.1.0** - Image processing
- **python-decouple 3.8** - Environment variable management

### Frontend
- **Bootstrap 5** - CSS framework
- **HTML5/CSS3** - Markup and styling
- **Font Awesome 6** - Icons
- **Tiny Slider** - Carousel functionality
- **JavaScript** - Interactive elements

## 📁 Project Structure

```
Sofa website/
├── about/              # About and team management app
├── account/            # User account management
├── blog/               # Blog functionality
├── cart/               # Shopping cart system
├── home/               # Homepage views
├── order/              # Order processing
├── store/              # Product catalog and store
├── sofawebsite/        # Main project settings
├── static/             # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/          # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── about/
│   ├── blog/
│   ├── cart/
│   ├── include/
│   ├── order/
│   └── shop/
├── media/              # User uploaded files
├── env/                # Virtual environment
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.14.2 or higher
- pip (Python package manager)
- Git

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd "Sofa website"
```

2. **Create virtual environment**
```bash
python -m venv env
```

3. **Activate virtual environment**
```bash
# Windows
env\Scripts\activate

# Linux/Mac
source env/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Set up environment variables**
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
db_name=your-database-name
db_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
```

6. **Set up PostgreSQL database**
Make sure PostgreSQL is installed and create a database:
```sql
CREATE DATABASE your_database_name;
CREATE USER your_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user;
```

7. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create superuser**
```bash
python manage.py createsuperuser
```

8. **Collect static files** (if needed)
```bash
python manage.py collectstatic
```

9. **Run development server**
```bash
python manage.py runserver
```

10. **Access the application**
- Website: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 📊 Database Models

### Product Model
- Product name, price, image
- Stock management
- Availability status
- Featured product flag
- Auto-generated slugs
- Timestamps

### Blog Model
- Title, content (description)
- Author (User FK)
- Featured image
- Featured post flag
- Auto-generated slugs
- Publication date

### Cart Models
- Cart: Session-based cart tracking
- CartItem: Product quantities and subtotals

### Team Model
- Name, position, bio
- Profile images

## 🎯 Key Functionalities

### Product Management
- Add products via Django admin
- Set featured products (displayed on homepage)
- Manage stock levels
- Track product availability

### Shopping Cart
- Session-based cart (no login required)
- Add/remove products
- Update quantities
- Automatic subtotal calculation
- Cart persistence across sessions

### Blog System
- Create and publish blog posts
- Rich text content support
- Featured post designation
- SEO-friendly URLs with slugs
- Responsive image handling

### Admin Panel
- Full CRUD operations for all models
- Product management
- Blog post management
- Order management
- Team member management

## 🎨 Customization

### Color Scheme
The website uses a consistent color palette:
- Primary: `#3b5d50` (Green)
- Accent: `#f9bf29` (Yellow)
- Text: `#6a6a6a`
- Dark: `#2f2f2f`
- Background: `#eff2f1`

### Modifying Styles
Edit `/static/css/style.css` to customize:
- Colors and themes
- Typography
- Layout spacing
- Component styles

## 📱 Responsive Design

The website is fully responsive with breakpoints for:
- Mobile: < 768px
- Tablet: 768px - 991px
- Desktop: 992px+

## 🔒 Security Features

- CSRF protection
- SQL injection prevention (Django ORM)
- XSS protection
- Environment-based configuration
- Secret key management via python-decouple

## 🚀 Deployment Considerations

Before deploying to production:
1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Ensure PostgreSQL is properly configured with strong credentials
4. Set up proper static file serving
5. Configure media file storage
6. Use environment variables for all sensitive data
7. Enable HTTPS
8. Set up proper logging
9. Configure database backups

## 📝 Future Enhancements

- User authentication and profiles
- Payment gateway integration
- Product reviews and ratings
- Wishlist functionality
- Advanced search and filtering
- Email notifications
- Order tracking system
- Multi-image product galleries
- Related products suggestions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Built with ❤️ using Django

## 🙏 Acknowledgments

- Bootstrap team for the CSS framework
- Font Awesome for icons
- Django community for excellent documentation
- Untree.co for design inspiration

---

**Note**: This is a development version. Make sure to configure proper security settings before deploying to production.
