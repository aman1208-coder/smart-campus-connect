"""
Smart Campus Connect - Python Flask Backend Server
Team: Link Loopers
Uses Data Structures: Linked List, BST, Queue, Stack
"""

try:
    from flask import Flask, jsonify, request
    from flask_cors import CORS
except ImportError as e:
    print("=" * 50)
    print("ERROR: Missing required packages!")
    print("=" * 50)
    print("\nPlease install the required packages:")
    print("  pip install flask flask-cors")
    print("\nOr if using pip3:")
    print("  pip3 install flask flask-cors")
    print("\n" + str(e))
    print("=" * 50)
    import sys
    sys.exit(1)

from datetime import datetime
from typing import Optional, List

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend connection

# ==================== DATA STRUCTURES ====================

# 1. LINKED LIST - User Management
class UserNode:
    def __init__(self, user_id: int, name: str, email: str, password: str, role: str, student_id: int = 0):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.student_id = student_id
        self.next: Optional[UserNode] = None

class UserList:
    def __init__(self):
        self.head: Optional[UserNode] = None
        self.count = 0
    
    def add(self, name: str, email: str, password: str, role: str, student_id: int = 0):
        new_user = UserNode(self.count + 1, name, email, password, role, student_id)
        new_user.next = self.head
        self.head = new_user
        self.count += 1
        return new_user
    
    def authenticate(self, email: str, password: str) -> Optional[UserNode]:
        current = self.head
        while current:
            if current.email == email and current.password == password:
                return current
            current = current.next
        return None
    
    def find_by_email(self, email: str) -> Optional[UserNode]:
        current = self.head
        while current:
            if current.email == email:
                return current
            current = current.next
        return None
    
    def to_list(self) -> List[dict]:
        result = []
        current = self.head
        while current:
            result.append({
                'id': current.id,
                'name': current.name,
                'email': current.email,
                'role': current.role,
                'studentId': current.student_id
            })
            current = current.next
        return result


# 2. BINARY SEARCH TREE - Student Records
class TreeNode:
    def __init__(self, student_id: int, name: str, email: str, department: str, cgpa: float):
        self.id = student_id
        self.name = name
        self.email = email
        self.department = department
        self.cgpa = cgpa
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class BST:
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def insert(self, student_id: int, name: str, email: str, department: str, cgpa: float):
        self.root = self._insert_node(self.root, student_id, name, email, department, cgpa)
    
    def _insert_node(self, node: Optional[TreeNode], student_id: int, name: str, 
                     email: str, department: str, cgpa: float) -> TreeNode:
        if node is None:
            return TreeNode(student_id, name, email, department, cgpa)
        
        if student_id < node.id:
            node.left = self._insert_node(node.left, student_id, name, email, department, cgpa)
        elif student_id > node.id:
            node.right = self._insert_node(node.right, student_id, name, email, department, cgpa)
        
        return node
    
    def search(self, student_id: int) -> Optional[TreeNode]:
        return self._search_node(self.root, student_id)
    
    def _search_node(self, node: Optional[TreeNode], student_id: int) -> Optional[TreeNode]:
        if node is None or node.id == student_id:
            return node
        
        if student_id < node.id:
            return self._search_node(node.left, student_id)
        return self._search_node(node.right, student_id)
    
    def delete(self, student_id: int):
        self.root = self._delete_node(self.root, student_id)
    
    def _delete_node(self, node: Optional[TreeNode], student_id: int) -> Optional[TreeNode]:
        if node is None:
            return None
        
        if student_id < node.id:
            node.left = self._delete_node(node.left, student_id)
        elif student_id > node.id:
            node.right = self._delete_node(node.right, student_id)
        else:
            # Node found - handle 3 cases
            if node.left is None and node.right is None:
                return None
            
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Two children
            min_right = self._find_min(node.right)
            node.id = min_right.id
            node.name = min_right.name
            node.email = min_right.email
            node.department = min_right.department
            node.cgpa = min_right.cgpa
            node.right = self._delete_node(node.right, min_right.id)
        
        return node
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
    
    def inorder(self) -> List[dict]:
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node: Optional[TreeNode], result: List[dict]):
        if node:
            self._inorder_traversal(node.left, result)
            result.append({
                'id': node.id,
                'name': node.name,
                'email': node.email,
                'department': node.department,
                'cgpa': node.cgpa
            })
            self._inorder_traversal(node.right, result)


# 3. QUEUE - Announcements (FIFO)
class QueueNode:
    def __init__(self, ann_id: int, message: str, posted_by: str):
        self.id = ann_id
        self.message = message
        self.posted_by = posted_by
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.next: Optional[QueueNode] = None

class Queue:
    def __init__(self):
        self.front: Optional[QueueNode] = None
        self.rear: Optional[QueueNode] = None
        self.count = 0
    
    def enqueue(self, message: str, posted_by: str):
        new_node = QueueNode(self.count + 1, message, posted_by)
        self.count += 1
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self) -> Optional[dict]:
        if self.front is None:
            return None
        
        removed = self.front
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        return {
            'id': removed.id,
            'message': removed.message,
            'postedBy': removed.posted_by,
            'timestamp': removed.timestamp
        }
    
    def to_list(self) -> List[dict]:
        result = []
        current = self.front
        while current:
            result.append({
                'id': current.id,
                'message': current.message,
                'postedBy': current.posted_by,
                'timestamp': current.timestamp
            })
            current = current.next
        return result


# 4. STACK - Events (LIFO)
class StackNode:
    def __init__(self, event_id: int, event: str, date: str, time: str):
        self.id = event_id
        self.event = event
        self.date = date
        self.time = time
        self.next: Optional[StackNode] = None

class Stack:
    def __init__(self):
        self.top: Optional[StackNode] = None
        self.count = 0
    
    def push(self, event: str, date: str, time: str):
        new_node = StackNode(self.count + 1, event, date, time)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
    
    def pop(self) -> Optional[dict]:
        if self.top is None:
            return None
        
        removed = self.top
        self.top = self.top.next
        self.count -= 1
        
        return {
            'id': removed.id,
            'event': removed.event,
            'date': removed.date,
            'time': removed.time
        }
    
    def to_list(self) -> List[dict]:
        result = []
        current = self.top
        while current:
            result.append({
                'id': current.id,
                'event': current.event,
                'date': current.date,
                'time': current.time
            })
            current = current.next
        return result


# 5. POLLS - Linked List
class Poll:
    def __init__(self, poll_id: int, question: str, options: List[str]):
        self.id = poll_id
        self.question = question
        self.options = options
        self.votes = [0] * len(options)
        self.total_votes = 0
        self.next: Optional[Poll] = None

class PollList:
    def __init__(self):
        self.head: Optional[Poll] = None
        self.count = 0
    
    def add(self, question: str, options: List[str]):
        new_poll = Poll(self.count + 1, question, options)
        new_poll.next = self.head
        self.head = new_poll
        self.count += 1
        return new_poll
    
    def vote(self, poll_id: int, option_index: int) -> bool:
        current = self.head
        while current:
            if current.id == poll_id:
                if 0 <= option_index < len(current.options):
                    current.votes[option_index] += 1
                    current.total_votes += 1
                    return True
                return False
            current = current.next
        return False
    
    def to_list(self) -> List[dict]:
        result = []
        current = self.head
        while current:
            result.append({
                'id': current.id,
                'question': current.question,
                'options': current.options,
                'votes': current.votes,
                'totalVotes': current.total_votes
            })
            current = current.next
        return result


# ==================== GLOBAL INSTANCES ====================

users = UserList()
student_tree = BST()
announcements = Queue()
events = Stack()
polls = PollList()
next_student_id = 101


# ==================== INITIALIZE DATA ====================

def initialize_data():
    """Initialize empty data structures"""
    users.add("Admin User", "admin@campus.com", "admin123", "admin", 0)
    print("✓ Data structures initialized")
    print("✓ System ready with empty database")


# ==================== API ROUTES ====================

@app.route('/')
def index():
    return jsonify({
        'message': 'Smart Campus Connect API',
        'team': 'Link Loopers',
        'status': 'running'
    })


@app.route('/api/announcements', methods=['GET'])
def get_announcements():
    return jsonify(announcements.to_list())

@app.route('/api/announcements', methods=['POST'])
def add_announcement():
    data = request.json
    announcements.enqueue(data.get('message'), data.get('postedBy'))
    return jsonify({'status': 'success', 'message': 'Announcement added'})

@app.route('/api/announcements', methods=['DELETE'])
def remove_announcement():
    removed = announcements.dequeue()
    if removed:
        return jsonify({'status': 'success', 'removed': removed})
    return jsonify({'status': 'error', 'message': 'No announcements to remove'}), 404


@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(events.to_list())

@app.route('/api/events', methods=['POST'])
def add_event():
    data = request.json
    events.push(data.get('event'), data.get('date'), data.get('time'))
    return jsonify({'status': 'success', 'message': 'Event added'})

@app.route('/api/events', methods=['DELETE'])
def remove_event():
    removed = events.pop()
    if removed:
        return jsonify({'status': 'success', 'removed': removed})
    return jsonify({'status': 'error', 'message': 'No events to remove'}), 404


@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(student_tree.inorder())

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = student_tree.search(student_id)
    if student:
        return jsonify({
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'department': student.department,
            'cgpa': student.cgpa
        })
    return jsonify({'status': 'error', 'message': 'Student not found'}), 404

@app.route('/api/students', methods=['POST'])
def add_student():
    data = request.json
    student_tree.insert(
        data.get('id'),
        data.get('name'),
        data.get('email'),
        data.get('department'),
        data.get('cgpa')
    )
    return jsonify({'status': 'success', 'message': 'Student added'})

@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = student_tree.search(student_id)
    if student:
        student_tree.delete(student_id)
        return jsonify({'status': 'success', 'message': 'Student deleted'})
    return jsonify({'status': 'error', 'message': 'Student not found'}), 404


@app.route('/api/polls', methods=['GET'])
def get_polls():
    return jsonify(polls.to_list())

@app.route('/api/polls', methods=['POST'])
def create_poll():
    data = request.json
    polls.add(data.get('question'), data.get('options'))
    return jsonify({'status': 'success', 'message': 'Poll created'})

@app.route('/api/polls/<int:poll_id>/vote', methods=['POST'])
def vote_poll(poll_id):
    data = request.json
    option_index = data.get('optionIndex')
    if polls.vote(poll_id, option_index):
        return jsonify({'status': 'success', 'message': 'Vote recorded'})
    return jsonify({'status': 'error', 'message': 'Invalid poll or option'}), 400


@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    user = users.authenticate(data.get('email'), data.get('password'))
    if user:
        return jsonify({
            'status': 'success',
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role,
                'studentId': user.student_id
            }
        })
    return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401

@app.route('/api/auth/register', methods=['POST'])
def register():
    global next_student_id
    data = request.json
    
    if users.find_by_email(data.get('email')):
        return jsonify({'status': 'error', 'message': 'Email already exists'}), 400
    
    student_id = 0
    role = data.get('role')
    
    if role == 'student':
        student_id = next_student_id
        next_student_id += 1
        student_tree.insert(
            student_id,
            data.get('name'),
            data.get('email'),
            'Not Assigned',
            0.0
        )
    
    user = users.add(
        data.get('name'),
        data.get('email'),
        data.get('password'),
        role,
        student_id
    )
    
    return jsonify({
        'status': 'success',
        'message': 'Registration successful',
        'studentId': student_id if role == 'student' else None
    })


# ==================== RUN SERVER ====================

if __name__ == '__main__':
    print("=" * 50)
    print("  Smart Campus Connect - Python Flask Backend")
    print("  Team: Link Loopers")
    print("=" * 50)
    print()
    
    initialize_data()
    
    print()
    print("✓ Server starting on http://localhost:8080")
    print("✓ Press CTRL+C to stop the server")
    print()
    
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("\nMake sure port 8080 is not already in use.")