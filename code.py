from flask import Flask, request, render_template_string

app = Flask(__name__)

faq_responses = {
    # Greetings
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "hey": "Hey! How’s your day going?",
    "good morning": "Good morning! Hope you have a great day.",
    "good afternoon": "Good afternoon! How’s it going?",
    "good evening": "Good evening! What’s up?",
    
    # Small Talk
    "how are you": "I'm just a bot, but I'm doing great! Thanks for asking.",
    "i am fine": "Glad to hear that! 😊",
    "what’s up": "Not much, just here to help you.",
    
    # Bot Info
    "what is your name": "I am your friendly chatbot.",
    "who are you": "I’m a simple chatbot here to chat and help.",
    "what can you do": "I can answer greetings, chat a little, and share some fun stuff.",
    
    # Fun
    "tell me a joke": "Why did the computer show up at work late? It caught a virus!",
    "motivate me": "You’re stronger than you think. Keep going! 💪",
    "fact": "Did you know? Honey never spoils — it can last thousands of years!",
    
    # Farewell
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later! Stay safe.",
    "see you": "Catch you later! 👋",
    
    # Gratitude
    "thanks": "You're welcome! 😊",
    "thank you": "Anytime! Happy to help."
}


html_template = """
<!doctype html>
<html>
<head>
    <title>Simple Chatbot</title>
    <style>
        body {
            background-color: aliceblue;
            font-family: Times New Roman;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background: white;
            padding: 20px 30px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        form {
            margin-top: 10px;
        }
        input[type="text"] {
            width: 300px;
            padding: 12px;
            font-size: 1.1rem;
            border-radius: 25px;
            border: 1px solid #ccc;
            outline: none;
            transition: 0.3s;
        }
        input[type="text"]:focus {
            border-color: #4CAF50;
            box-shadow: 0 0 5px #4CAF50;
        }
        button {
            padding: 12px 18px;
            font-size: 1.1rem;
            border-radius: 25px;
            border: none;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #45a049;
        }
        .chat {
            margin-top: 20px;
            text-align: left;
        }
        .you, .bot {
            display: inline-block;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 8px 0;
            max-width: 80%;
            font-size: 1.1rem;
        }
        .you {
            text-align: right;
            background-color: #d0e7ff;
            color: #004085;
            align-self: flex-end;
            float: right;
            clear: both;
        }
        .bot {
            text-align: left;
            background-color: #d4edda;
            color: #155724;
            align-self: flex-start;
            float: left;
            clear: both;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Simple Chatbot</h1>
        <form method="POST">
            <input type="text" name="user_input" placeholder="Ask me something...">
            <button type="submit">Send</button>
        </form>
        <div class="chat">
            {% if user_input %}
                <p class="you">You: {{ user_input }}</p>
                <p class="bot">Bot: {{ bot_response }}</p>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chatbot():
    user_input = None
    bot_response = None
    if request.method == "POST":
        user_input = request.form["user_input"].strip()
        bot_response = faq_responses.get(user_input.lower(), "Sorry, I didn't understand that.")
    return render_template_string(html_template, user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
