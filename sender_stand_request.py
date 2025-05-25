import requests
import configuration
import data

def post_new_user():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body
    )

def get_new_user_token():
    response = post_new_user()
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
        json=kit_body,
        headers={"Authorization": f"Bearer {auth_token}"}
    )


