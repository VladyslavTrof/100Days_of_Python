from flask import Flask, render_template, request, redirect, url_for, flash
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    # Character pools
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Build the character pool based on user choices
    char_pool = ''
    if use_uppercase:
        char_pool += uppercase_letters
    if use_lowercase:
        char_pool += lowercase_letters
    if use_digits:
        char_pool += digits
    if use_special:
        char_pool += special_characters

    # Ensure at least one character type is selected
    if not char_pool:
        raise ValueError("At least one character type must be selected")

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form['length'])
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_digits = 'digits' in request.form
        use_special = 'special' in request.form

        try:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            flash(f"Generated password: {password}", 'success')
        except ValueError as e:
            flash(str(e), 'danger')

        return redirect(url_for('index'))

    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Password Generator</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
      </head>
      <body>
        <div class="container">
          <h1 class="mt-5">Password Generator</h1>
          <form method="post">
            <div class="form-group">
              <label for="length">Password Length</label>
              <input type="number" class="form-control" id="length" name="length" required>
            </div>
            <div class="form-check">
              <input type="checkbox" class="form-check-input" id="uppercase" name="uppercase">
              <label class="form-check-label" for="uppercase">Include Uppercase Letters</label>
            </div>
            <div class="form-check">
              <input type="checkbox" class="form-check-input" id="lowercase" name="lowercase">
              <label class="form-check-label" for="lowercase">Include Lowercase Letters</label>
            </div>
            <div class="form-check">
              <input type="checkbox" class="form-check-input" id="digits" name="digits">
              <label class="form-check-label" for="digits">Include Digits</label>
            </div>
            <div class="form-check">
              <input type="checkbox" class="form-check-input" id="special" name="special">
              <label class="form-check-label" for="special">Include Special Characters</label>
            </div>
            <button type="submit" class="btn btn-primary mt-3">Generate Password</button>
          </form>
          {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
              <div class="mt-3">
                {% for category, message in messages %}
                  <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
              </div>
            {% endif %}
          {% endwith %}
        </div>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
