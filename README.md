# Dezy's Budget Tracker

A Python-based personal finance application that helps users track their expenses and manage their budget effectively.

## Features

- Add daily expenses with dates, amounts, and categories
- View expense history
- Input validation and error handling
- Data persistence through JSON storage
- User-friendly command-line interface

## Prerequisites

- Python 3.6 or higher
- Git (for cloning the repository)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DezysBudgetTracker.git
   cd DezysBudgetTracker
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the on-screen menu to:
   - Add new expenses
   - View existing expenses
   - Exit the application

## Project Structure

```
├── expense.py       # Expense class and validation functions
├── main.py        # Main application logic
├── operations.py  # Additional operations for managing expenses
├── README.md        # Project documentation
```

## Error Handling

The application includes comprehensive error handling for:
- Invalid date formats
- Invalid monetary amounts
- Empty categories
- File I/O operations
- Unexpected errors

## To-Do List

- [ ] Add monthly budget setting
- [ ] Add Storage system for expenses
- [ ] Add budget managment settings
- [ ] Implement expense categories management
- [ ] Add data visualization (graphs/charts)
- [ ] Create expense reports
- [ ] Add multi-currency support
- [ ] Implement user authentication
- [ ] Create a web interface
- [ ] Add expense search functionality
- [ ] Enable data export to CSV/Excel
- [ ] Add recurring expenses feature

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to my girlfriend for highlighting my need for a budget tracker
- Inspired by the need for a simple, effective budget tracking solution for myself


## Support

If you find this project helpful, please give it a ⭐️!
