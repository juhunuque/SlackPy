import os
from gSheet.sheet_utils import SheetUtils
from keys import Keys


def process_keys(request, sheet_id, slack_client):
    sheet = SheetUtils(sheet_id)
    key = request.form.get('text')
    channel_id = request.form.get('channel_id')
    username = request.form.get('user_name')
    if str(key).lower() == str(Keys.yoVoy):
            sheet.update_row(username, 'Si', 4)
            send_chat(channel_id, username + ' va ir a mejenguear!', slack_client)
    elif str(key).lower() == str(Keys.help):
        send_chat(channel_id, '$yoVoy: Lo apunta en la mejenga \n'
                              '$yaNoVoy: Lo quita de la mejenga', slack_client)

    elif str(key).lower() == str(Keys.yaNoVoy):
        sheet.update_row(username, 'No', 4)
        send_chat(channel_id, username + ' se quito de la mejenga!', slack_client)
    elif str(key).lower() == str(Keys.cleanAll):
        send_chat(channel_id, 'Ready to start!', slack_client)
    else:
        print key


def send_chat(channel_id, message, slack_client):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='mejengasbot',
        icon_emoji=':robot_face:'
    )


def resolve_config_property(config, config_section_name, property_name):
    if property_name is None:
        return None

    env_var = '{0}_{1}'.format(config_section_name, property_name).upper()

    if os.getenv(env_var) is not None:
        return os.getenv(env_var)

    config_section = config.get(config_section_name)
    if config_section is not None and config_section.get(property_name) is not None:
        return config_section.get(property_name)

    return None