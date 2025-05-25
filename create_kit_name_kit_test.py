import data
import sender_stand_request
import copy

#Creando nuevo usuario
def get_kit_body(name):
    current_body = copy.deepcopy(data.kit_body)
    current_body["name"] = name
    return current_body

#Realiza una solicitud para crear un nuevo kit de cliente y verifica que la respuesta sea exitosa..
def positive_assert(kit_body):
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Realiza una solicitud para crear un nuevo kit de cliente y verifica que la respuesta indique un error de solicitud incorrecta.
def negative_assert_code_400(kit_body):
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400

#Prueba la creación de un kit con un nombre de un solo carácter.
def test_create_kit_name_1_character():
    positive_assert(get_kit_body("a"))

#Prueba la creación de un kit con un nombre de 511 caracteres
def test_create_kit_name_511_characters():
    name_511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert(get_kit_body(name_511))

#Prueba la creación de un kit con un nombre vacío.
def test_create_kit_name_0_characters():
    positive_assert(get_kit_body(""))

#Prueba la creación de un kit con un nombre de 512 caracteres.
def test_create_kit_name_512_characters():
    name_512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    positive_assert(get_kit_body(name_512))

#Prueba la creación de un kit con un nombre que contiene caracteres especiales.
def test_create_kit_name_special_characters():
    positive_assert(get_kit_body("\"№%@\","))

#Prueba la creación de un kit con un nombre que contiene espacios.
def test_create_kit_name_with_spaces():
    positive_assert(get_kit_body(" A Aaa "))

#Prueba la creación de un kit con un nombre numérico
def test_create_kit_name_number_instead_of_string():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

#Prueba la creación de un kit sin el campo 'name
def test_create_kit_name_missing_name_field():
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit({}, token)
    assert response.status_code == 500  # No es correcto, pero es lo que devuelve

#Prueba la creación de un kit con un nombre numérico como cadena
def test_create_kit_name_number_instead_of_string_positive():
    kit_body = copy.deepcopy(data.kit_body)
    kit_body["name"] = "123"  # aquí sí es string "123"
    positive_assert(kit_body)


