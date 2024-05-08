import bcrypt

class Authentication:
    def __init__(self):
        # Your database or user storage logic can be initialized here
        self.users = {}

    def register(self, username, password):
        try:
            # Hash the password before storing it
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # Simulate storing user data in a dictionary
            self.users[username] = hashed_password
            return {'success': True, 'message': 'User registered successfully'}
        except Exception as e:
            print('Error registering user:', e)
            return {'success': False, 'message': 'Failed to register user'}

    def login(self, username, password):
        try:
            # Retrieve the hashed password for the given username
            hashed_password = self.users.get(username)
            if not hashed_password:
                return {'success': False, 'message': 'User not found'}
            # Check if the provided password matches the hashed password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return {'success': True, 'message': 'Login successful'}
            else:
                return {'success': False, 'message': 'Incorrect password'}
        except Exception as e:
            print('Error logging in:', e)
            return {'success': False, 'message': 'Failed to login'}

# Example usage:
auth = Authentication()

# Register a new user
print(auth.register('john_doe', 'password123'))

# Login with registered user
print(auth.login('john_doe', 'password123'))
