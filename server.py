from flask import Flask, request
import json

app = Flask(__name__)


class ticket_info(object):
    def __init__(self, user, title):
        self.data = {'user': user,
                     'title': title}

    def to_json(self):
        return json.dumps(self.data)


TICKETS = []


@app.route('/', methods=['POST', 'GET'])
def handle_post():
    global TICKETS

    if request.method == "POST":
        data = request.get_json()
        TICKETS.append(ticket_info(data['kanbanize_payload']['triggerAuthor'],
                                   data['kanbanize_payload']['card']['title']))

    elif request.method == "GET" and len(TICKETS) > 0:
        ticket = TICKETS.pop(0)
        json_data = ticket.to_json()
        del(ticket)
        return json_data

    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
