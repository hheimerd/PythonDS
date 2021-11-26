import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']


def on_error():
  raise ValueError()

def main():
    if len(sys.argv) != 2: on_error()

    clients_set = set(clients)
    participants_set = set(participants)
    recipients_set = set(recipients)

    commands = ["call_center", "potential_clients", "loyalty_program"]
    command = sys.argv[1]

    if (command not in commands): on_error()

    print ({
        "call_center": (clients_set | participants_set) - recipients_set,
        "potential_clients": participants_set - clients_set, 
        "loyalty_program": clients_set - participants_set
    }[command])



if __name__ == '__main__':
    main()
