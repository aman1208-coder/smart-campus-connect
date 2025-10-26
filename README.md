🌟 Overview
Smart Campus Connect is a web-based application designed to streamline campus communication and management. The system efficiently handles student records, announcements, events, and polls using custom implementations of fundamental data structures.
Key Highlights
<img width="1591" height="849" alt="Screenshot 2025-10-26 144700" src="https://github.com/user-attachments/assets/8bd38180-a66a-479f-92c3-9b3cd9472636" />
<img width="1902" height="1031" alt="Screenshot 2025-10-26 144822" src="https://github.com/user-attachments/assets/dccb56f4-60cd-45fc-9c03-5a9eac5b3581" />

✅ Custom implementation of data structures (no libraries)
✅ RESTful API architecture
✅ Role-based access control (Admin, Faculty, Student)
✅ Real-time data management
✅ Responsive user interface


🔧 Data Structures Used
1. Linked List - User Management & Polls

Purpose: Store user accounts and poll data
Operations: Insert (O(1)), Search (O(n)), Authenticate
Implementation: Singly linked list with head pointer

2. Binary Search Tree (BST) - Student Records

Purpose: Organize student data by ID for efficient searching
Operations: Insert (O(log n)), Search (O(log n)), Delete (O(log n)), Inorder Traversal
Implementation: Recursive BST with three-case deletion

3. Queue (FIFO) - Announcements

Purpose: Manage announcements in First-In-First-Out order
Operations: Enqueue (O(1)), Dequeue (O(1))
Implementation: Linked list-based queue with front and rear pointers

4. Stack (LIFO) - Events

Purpose: Manage events in Last-In-First-Out order
Operations: Push (O(1)), Pop (O(1))
Implementation: Linked list-based stack with top pointer

✨ Features
For All Users

🔐 Secure login and registration system
📢 View campus announcements
📅 Browse upcoming events
📊 Participate in campus polls
👥 View student directory

For Admins & Faculty

➕ Add/Remove student records
📝 Post announcements to campus
🎉 Schedule new events
📋 Create polls
📊 Manage all system data

For Students

🆔 Automatic student ID generation upon registration
📖 Access to all campus information
🗳️ Vote in campus polls
📧 View personal academic information

💻 Technology Stack
Backend

Python 3.7+
Flask - Web framework
Flask-CORS - Cross-origin resource sharing

Frontend

HTML5 - Structure
CSS3 - Styling (Gradient UI, Responsive Design)
JavaScript (ES6+) - Dynamic functionality, Fetch API

Data Structures


Custom implementations (no external libraries)
Pure Python & JavaScript

📦 Installation
Prerequisites

Python 3.7 or higher
pip (Python package manager)
Modern web browser (Chrome, Firefox, Edge, Safari)
Login not working?

Ensure backend is running on http://localhost:8080
Check browser console for errors (F12)
Verify CORS is enabled

Data not persisting?

This is an in-memory system
Data resets when server restarts
For persistence, integrate a database

🚀 Future Enhancements

 Database integration (SQLite/MySQL)
 File upload support
 Email notifications
 Advanced search and filtering
 Analytics dashboard
 Mobile application
 Graph data structures for course prerequisites
 Hash tables for faster lookups

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

👨‍💻 Authors
Team Link Loopers

Implemented custom data structures
Designed RESTful API architecture
Created responsive UI/UX

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

Inspired by real-world campus management needs
Built to demonstrate practical data structure applications
Thanks to the open-source community

📞 Contact
For questions or feedback:

Create an issue on GitHub
Email: [itsmj1208@gmail.com]
