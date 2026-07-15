from flask import Flask, jsonify, render_template_string
import json, os

app = Flask(__name__)

html_template = '''
<html>
    <body style="background:#000; color:white; display:flex; justify-content:center; align-items:center; height:100vh; margin:0; font-family:sans-serif;">
        <div style="text-align:center;">
            <div id="game-box" style="width:300px; height:150px; border:4px solid #444; display:flex; align-items:center; justify-content:center; font-size:40px; font-weight:bold; background:#111; margin-bottom:20px;">?</div>
            <h2 id="status-text" style="color:#888;">Tunggu jawaban...</h2>
        </div>
        <script>
            setInterval(() => {
                fetch('/get_data').then(r => r.json()).then(data => {
                    if (data.status === 'correct') {
                        document.getElementById('game-box').innerText = data.word.toUpperCase();
                        document.getElementById('game-box').style.background = '#27ae60';
                        document.getElementById('status-text').innerText = "PEMENANG: " + data.user;
                        document.getElementById('status-text').style.color = '#27ae60';
                    }
                });
            }, 1000);
        </script>
    </body>
</html>
'''

@app.route('/')
def index(): return render_template_string(html_template)

@app.route('/get_data')
def get_data():
    if os.path.exists('game_state.json'):
        with open('game_state.json', 'r') as f: return f.read()
    return jsonify({"status": "waiting"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
