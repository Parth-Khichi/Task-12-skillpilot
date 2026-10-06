# Contact Form — Flask + Flask-WTF \+ SQLite

 A simple contact form built with **Flask**, **Flask-WTF**, and **SQLite3**. Form submissions are validated before being stored in the SQLite database.

 ## Features

 - Flask web application
- Flask-WTF form handling
- CSRF protection
- Server-side validation
- Email validation
- SQLite database storage
- Success messages after submission
- Validation error messages
- Responsive CSS design

 ## Project Structure

```
contact-form/
│
├── app.py
├── contacts.db
├── requirements.txt
│
├── templates/
    └── contact.html

```

 ## Requirements

 - Python 3.9+
- Flask
- Flask-WTF
- email-validator

 ## Installation

 Clone or download the project, then create a virtual environment:

```
python -m venv venv
```

 Activate it:

 ### Windows

```
venv\Scripts\activate
```

 ### macOS/Linux

```
source venv/bin/activate
```

 Install dependencies:

```
pip install -r requirements.txt
```

 ## `requirements.txt`

```
Flask
Flask-WTF
email-validator
```

 ## Run the Application

```
python app.py
```

 The application will start at:

```
http://127.0.0.1:5000/contact
```

 Open that address in your browser.

 ## Database

 The application automatically creates a SQLite database named:

```
contacts.db
```

 The `contacts` table contains:

 | Column | Type | Description |
| --- | --- | --- |
| `id` | INTEGER | Primary key |
| `name` | TEXT | User's name |
| `email` | TEXT | User's email |
| `message` | TEXT | Contact message |

## Validation

 The form validates:

 - **Name:** Required, 2–100 characters
- **Email:** Required and must be a valid email address
- **Message:** Required, 10–1000 characters

 Data is inserted into SQLite **only after successful validation**.

 ## Submission Flow

```
User opens /contact
        ↓
Form displayed
        ↓
User submits form
        ↓
Flask-WTF validates input
        ↓
   Validation OK?
      /      \
    Yes       No
     ↓         ↓
SQLite DB   Show errors
     ↓
Success message
     ↓
Redirect to /contact
```

 ## Security

 The application uses:

 - Flask-WTF CSRF protection
- Parameterized SQLite queries
- Server-side input validation

 For production, replace the development `SECRET_KEY` with a secure secret stored in an environment variable.

 ## Future Improvements

 - Add a page to view submitted contacts
- Add delete/edit functionality
- Add email notifications
- Use Flask-SQLAlchemy
- Add automated tests
- Deploy using a production WSGI server

 ## License

 This project is intended for learning and development purposes.