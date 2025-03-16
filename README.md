# Todo List App

A modern, bilingual todo list application built with Flask and modern web technologies. The application supports both English and Arabic languages, with full RTL support and a clean, responsive interface.

## Features

- 📝 Create, read, update, and delete todos
- 🎨 Color-code your todos for better organization
- 📅 Add due dates to your tasks
- 🌐 Bilingual support (English/Arabic)
- ⚡ Real-time language switching
- 🔄 RTL/LTR layout support
- 💅 Modern typography with Google Fonts
- 🎯 Task categorization with color coding
- 📱 Responsive design

## Technologies Used

- Backend:
  - Flask 3.1.0
  - Flask-CORS 5.0.0
  - Python 3.x

- Frontend:
  - HTML5
  - CSS3
  - JavaScript (Vanilla)
  - Google Fonts (Roboto, Poppins, Noto Sans Arabic)
  - Font Awesome Icons

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   cd todo-list-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:59727
   ```

## Usage

1. **Adding a Todo**:
   - Enter your task in the input field
   - Select a due date
   - Choose a color for categorization
   - Click "Add Todo" or "إضافة مهمة"

2. **Managing Todos**:
   - View all todos in the list
   - Delete todos using the delete button
   - Tasks are color-coded based on your selection

3. **Language Switching**:
   - Click "English" or "عربي" in the header
   - Interface automatically adjusts for RTL/LTR
   - All text elements are translated

## API Endpoints

- `GET /api/todos` - Retrieve all todos
- `POST /api/todos` - Create a new todo
- `DELETE /api/todos/<index>` - Delete a specific todo
- `PUT /api/todos/<index>` - Update a specific todo

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
