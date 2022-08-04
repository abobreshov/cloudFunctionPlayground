import socket


def main(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message') + ' from ' + local_ip
    elif request_json and 'message' in request_json:
        return request_json['message'] + ' from ' + local_ip
    else:
        return f'Hello {hostname}! {local_ip}'
