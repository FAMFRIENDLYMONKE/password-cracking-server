from flask import Flask, request, render_template_string

app = Flask(__name__)

# Demo credentials (do not use in production)
USERNAME = 'student'
PASSWORD = 'password123'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        if user == USERNAME and pwd == PASSWORD:
            return "Login successful!"
        else:
            return "Invalid credentials", 401
    return render_template_string("""
    <form method="post">
        <input type="text" name="username" placeholder="username"/><br>
        <input type="password" name="password" placeholder="password"/><br>
        <input type="submit" value="Login"/>
    </form>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
