import requests
import time

class TwoCaptchaSolver:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://2captcha.com"

    def solve_captcha(self, image_path):
        # Paso 1: Subir el CAPTCHA a TwoCaptcha
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            data = {
                'key': self.api_key,
                'method': 'post',
                'json': 1
            }
            response = requests.post(f"{self.base_url}/in.php", files=files, data=data)
            result = response.json()

            if result.get('status') == 1:
                captcha_id = result.get('request')
                print(f"CAPTCHA subido exitosamente. ID: {captcha_id}")
            else:
                raise Exception(f"Error al subir CAPTCHA: {result.get('request')}")

        # Paso 2: Consultar el resultado del CAPTCHA resuelto
        captcha_text = self._get_captcha_result(captcha_id)
        return captcha_text

    def _get_captcha_result(self, captcha_id):
        while True:
            time.sleep(5)  # Esperar unos segundos antes de intentar obtener el resultado

            params = {
                'key': self.api_key,
                'action': 'get',
                'id': captcha_id,
                'json': 1
            }
            response = requests.get(f"{self.base_url}/res.php", params=params)
            result = response.json()

            if result.get('status') == 1:
                # El CAPTCHA ha sido resuelto
                print(f"CAPTCHA resuelto: {result.get('request')}")
                return result.get('request')
            elif result.get('request') == 'CAPCHA_NOT_READY':
                print("CAPTCHA aún no está listo, esperando...")
            else:
                raise Exception(f"Error al resolver CAPTCHA: {result.get('request')}")
