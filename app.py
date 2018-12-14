import os
from bottle import route, run, request, abort, static_file
from fsm import TocMachine


#VERIFY_TOKEN = "verify"
#PORT = 5000
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']

machine = TocMachine(
    states=[
        'user',
        'simon',
        'food',
            'bubble',
            'chicken',
            'loser',
            'dragon',
            'ice',
        'ipass',
            'smallpa',
            'P',
            'elfair',
        '3boss',
            'air',
            'magi',
            'sakura',
            'rice',
                'child',
                'sister',
                'whiterice',
        'mrt',
            'sora',
            'emilia',
            'jay',
            'nana'
    ],
    transitions=[
        {
            'trigger': 'wakeup',
            'source': 'user',
            'dest': 'simon',
        },
        {
            'trigger': 'advance',
            'source': [
                'user',
                'simon',
                'food',
                    'bubble',
                    'chicken',
                    'loser',
                    'dragon',
                    'ice',
                'ipass',
                    'smallpa',
                    'P',
                    'elfair',
                '3boss',
                    'air',
                    'magi',
                    'sakura',
                    'rice',
                        'child',
                        'sister',
                        'whiterice',
                'mrt',
                    'sora',
                    'emilia',
                    'jay',
                    'nana'
            ],
            'dest': 'simon',
            'conditions': 'is_going_to_simon'
        },
        {
            'trigger': 'advance',
            'source': 'simon',
            'dest': 'food',
            'conditions': 'is_going_to_food'
        },
            {
            'trigger': 'advance',
            'source': 'food',
            'dest': 'bubble',
            'conditions': 'is_going_to_bubble'
            },
            {
            'trigger': 'advance',
            'source': 'food',
            'dest': 'chicken',
            'conditions': 'is_going_to_chicken'
            },
            {
            'trigger': 'advance',
            'source': 'food',
            'dest': 'loser',
            'conditions': 'is_going_to_loser'
            },
            {
            'trigger': 'advance',
            'source': 'food',
            'dest': 'dragon',
            'conditions': 'is_going_to_dragon'
            },
            {
            'trigger': 'advance',
            'source': 'food',
            'dest': 'ice',
            'conditions': 'is_going_to_ice'
            },
        {
            'trigger': 'advance',
            'source': 'simon',
            'dest': 'ipass',
            'conditions': 'is_going_to_ipass'
        },
            {
            'trigger': 'advance',
            'source': 'ipass',
            'dest': 'smallpa',
            'conditions': 'is_going_to_smallpa'
            },
            {
            'trigger': 'advance',
            'source': 'ipass',
            'dest': 'P',
            'conditions': 'is_going_to_P'
            },
            {
            'trigger': 'advance',
            'source': 'ipass',
            'dest': 'elfair',
            'conditions': 'is_going_to_elfair'
            },

        {
            'trigger': 'advance',
            'source': 'simon',
            'dest': '3boss',
            'conditions': 'is_going_to_3boss'
        },
            {
            'trigger': 'advance',
            'source': '3boss',
            'dest': 'air',
            'conditions': 'is_going_to_air'
            },
            {
            'trigger': 'advance',
            'source': '3boss',
            'dest': 'magi',
            'conditions': 'is_going_to_magi'
            },
            {
            'trigger': 'advance',
            'source': '3boss',
            'dest': 'sakura',
            'conditions': 'is_going_to_sakura'
            },
            {
            'trigger': 'advance',
            'source': '3boss',
            'dest': 'rice',
            'conditions': 'is_going_to_rice'
            },
                {
                'trigger': 'advance',
                'source': 'rice',
                'dest': 'child',
                'conditions': 'is_going_to_child'
                },
                {
                'trigger': 'advance',
                'source': 'rice',
                'dest': 'sister',
                'conditions': 'is_going_to_sister'
                },
                {
                'trigger': 'advance',
                'source': 'rice',
                'dest': 'whiterice',
                'conditions': 'is_going_to_whiterice'
                },
        {
            'trigger': 'advance',
            'source': 'simon',
            'dest': 'mrt',
            'conditions': 'is_going_to_mrt'
        },
            {
            'trigger': 'advance',
            'source': 'mrt',
            'dest': 'sora',
            'conditions': 'is_going_to_sora'
            },
            {
            'trigger': 'advance',
            'source': 'mrt',
            'dest': 'emilia',
            'conditions': 'is_going_to_emilia'
            },
            {
            'trigger': 'advance',
            'source': 'mrt',
            'dest': 'jay',
            'conditions': 'is_going_to_jay'
            },
            {
            'trigger': 'advance',
            'source': 'mrt',
            'dest': 'nana',
            'conditions': 'is_going_to_nana'
            }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if machine.state == 'user':
            machine.wakeup(event)
        else:    
            machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')

if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
