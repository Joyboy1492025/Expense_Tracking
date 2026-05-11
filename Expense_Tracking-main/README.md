# Spent - Self-Hostable Personal Finance Tracker

A modern, self-hostable expense tracking application built with Flask and SQLAlchemy. Track your spending across multiple currencies with category filtering, visual analytics, and a beautiful dark/light mode interface.

## Features

- 💰 **Expense Tracking**: Record expenses with title, amount, category, and currency
- 🌍 **Multi-Currency Support**: Track expenses in USD, EUR, GBP, JPY, INR, AUD, CAD, CHF, CNY, SEK, NZD, SGD, HKD, MXN, BRL, and ZAR
- 🏷️ **Category Filtering**: Organize expenses by Food, Bills, Work, Personal, Travel, and Other
- 📊 **Visual Analytics**: See spending totals and filter by category
- 🌙 **Dark Mode**: Toggle between light and dark themes
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🎨 **Category Icons**: Visual emoji indicators for each expense category
- 🚀 **Self-Hostable**: Run on your own server with minimal setup

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup

1. **Clone or download the project files**

2. **Navigate to the Expense_Tracking directory**
   ```bash
   cd Expense_Tracking
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and visit `http://localhost:5000`

## Usage

### Adding Expenses
- Click the blue "+" button at the bottom right
- Enter expense description
- Input the amount
- Select a category (Food, Bills, Work, Personal, Travel, Other)
- Choose your currency
- Click "Add Entry"

### Managing Expenses
- **View All**: See all expenses with totals
- **Filter by Category**: Use the dropdown to filter expenses by category
- **Currency Selection**: Change display currency in the top navigation
- **Delete**: Hover over any expense and click the X to remove it

### Features
- **Total Display**: Shows total spending with currency symbol
- **Category Icons**: Visual indicators (🍔 for Food, 💼 for Work, ⚡ for Bills, etc.)
- **Date Tracking**: Each expense shows the date it was added
- **Dark Mode**: Toggle with the moon/sun icon in the header

## Project Structure

```
Expense_Tracking/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── instance/           # SQLite database storage
└── templates/
    └── index.html      # Main UI template
```

## Dependencies

- Flask==3.1.3
- Flask-SQLAlchemy==3.1.1
- SQLAlchemy==2.0.49

## Database

The application uses SQLite (`expenses.db`) which is automatically created when you first run the app. The database includes:
- Expense title/description
- Amount (float)
- Category
- Currency (3-letter code)
- Date added (timestamp)

The app automatically handles database migrations to add the currency column if upgrading from an older version.

## Supported Currencies

The application supports 16 currencies with their proper symbols:
- USD ($), EUR (€), GBP (£), JPY (¥), INR (₹)
- AUD (A$), CAD (C$), CHF (CHF), CNY (¥), SEK (kr)
- NZD (NZ$), SGD (S$), HKD (HK$), MXN ($), BRL (R$), ZAR (R)

## Customization

### Adding Categories
Add new expense categories by updating the category select options in `templates/index.html` and the filtering logic in the JavaScript.

### Currency Support
Add more currencies by updating the `CURRENCIES` dictionary in `app.py` and the currency select options in the template.

### Styling
The UI uses Tailwind CSS and can be customized by modifying the `<style>` section in `templates/index.html`.

### Database
For production use, consider switching to PostgreSQL or MySQL by updating the `SQLALCHEMY_DATABASE_URI` in `app.py`.

## Security Notes

- This is a basic implementation for personal use
- For production deployment, consider:
  - Using environment variables for configuration
  - Adding user authentication
  - Implementing data backup strategies
  - Setting up proper database backups
  - Adding expense editing functionality

## License

MIT License - feel free to use and modify for your own projects.

## Contributing

Feel free to submit issues and enhancement requests!</content>
