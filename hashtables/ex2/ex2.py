#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    flights = {}
    route = []

    for ticket in tickets:
        flights[ticket.source] = ticket.destination

    current_flight = flights['NONE']

    while current_flight is not 'NONE':
        route.append(current_flight)
        current_flight = flights[current_flight]

    route.append(current_flight)

    return route
