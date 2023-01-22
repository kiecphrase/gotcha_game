from gotcha_game import gotcha_pull as g

def handle_response(m) -> str:
    p_message = m.lower()

    if p_message == '$roll':
        return g()

    elif p_message == '!help':
        return '`type "$roll" to play!`'

    else:
        return