from requests import get
import google.cloud.logging
import logging

client = google.cloud.logging.Client()
client.setup_logging()


def main(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()

    ip = get('https://api.ipify.org').content.decode('utf8')
    logging.info('My public IP address is: {}'.format(ip))
    if request.args and 'message' in request.args:
        return request.args.get('message') + ' from ' + ip
    elif request_json and 'message' in request_json:
        return request_json['message'] + ' from ' + ip
    else:
        return f'Hello World! {ip}'
