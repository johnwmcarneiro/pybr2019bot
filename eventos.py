import dateutil.parser
import requests


GOOGLE_CALENDAR_URL = "https://www.googleapis.com/calendar/v3/calendars/ft5mdp26mhosq2heu6g87mb7ns%40group.calendar.google.com/events?key=AIzaSyAIn8DyZFtthupLozgwIX3NUURFMWEIPb4&timeMin=2019-10-22T00%3A00%3A00.000Z&timeMax=2019-10-25T00%3A00%3A00.000Z&singleEvents=true&maxResults=9999&timeZone=America%2FSao_Paulo"


def todos_eventos():
    conteudo = requests.get(GOOGLE_CALENDAR_URL)
    return conteudo.json()["items"]


def tutoriais_23():
    eventos = todos_eventos()
    tutoriais_23 = []
    for evento in eventos:
        start = dateutil.parser.parse(evento['start']['dateTime'])
        evento['start']['dateTime'] = start

        if start.day == 23:
            tutoriais_23.append(evento)

    return sorted(tutoriais_23, key=lambda evento: evento['start']['dateTime'])
