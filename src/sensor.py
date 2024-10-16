from random import randrange

class Sensor:
    def __init__(self, identificador, ip_address, gps_location):
        """
        Inicializa um objeto Sensor com um identificador, endereço IP e localização GPS.
        
        :param identificador: Identificador único do sensor.
        :param ip_address: Endereço IP do sensor.
        :param gps_location: Localização GPS do sensor (latitude, longitude).
        """
        self.identificador = identificador
        self.ip_address = ip_address
        self.gps_location = gps_location

    def open_water(self, tempo):
        """
        Simula a abertura do sistema de irrigação com base no tempo fornecido.
        
        :param tempo: Tempo (em segundos) durante o qual a água deve ser aberta.
        :return: Mensagem informando que a água foi aberta por um tempo específico.
        """
        return f"Água aberta por {tempo} segundos no sensor {self.identificador}."

    def get_hum(self):
        """
        Simula a obtenção da humidade do solo a partir do sensor.
        
        :return: Um valor fictício da humidade do solo (percentual).
        """
        # Aqui você pode implementar a lógica para obter a humidade real de um sensor
        # Neste exemplo, retornaremos um valor fictício.
        # Exemplo de um valor fixo de humidade
        humidade = randrange(20,100) 
        return f"Humidade do solo no sensor {self.identificador}: {humidade}%"