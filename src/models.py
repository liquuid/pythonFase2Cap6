from sqlalchemy import Column, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from random import randrange


Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensor'

    identificador = Column(String(50), primary_key=True, nullable=False)
    ip = Column(String(45), nullable=False)
    latitude = Column(Float, nullable=False) 
    longitude = Column(Float, nullable=False)
    humidade_max = Column(Float, nullable=False)
    humidade_min = Column(Float, nullable=False)
    humidade_ultimo_valor = Column(Float, nullable=True)

    def open_water(self, tempo):
        """
        Simula a abertura do sistema de irrigação com base no tempo fornecido.
        
        :param tempo: Tempo (em segundos) durante o qual a água deve ser aberta.
        :return: Mensagem informando que a água foi aberta por um tempo específico.
        """
        return f"Água aberta por {tempo} segundos no sensor {self.identificador}."

    def get_hum(self,session):
        """
        Simula a obtenção da humidade do solo a partir do sensor.
        
        :return: Um valor fictício da humidade do solo (percentual).
        """
        # Aqui você pode implementar a lógica para obter a humidade real de um sensor
        # Neste exemplo, retornaremos um valor fictício.
        # Exemplo de um valor fixo de humidade

        humidade = randrange(20,100)
        self.humidade_ultimo_valor = humidade
        #import pdb; pdb.set_trace()
        #print(self.humidade_ultimo_valor, humidade)
        session.commit()
        return f"Humidade do solo no sensor {self.identificador}: {humidade}%"    

    def __repr__(self):
        return f"<Sensor(identificador={self.identificador}, ip={self.ip}, latitude={self.latitude}, longitude={self.longitude})>"

# Exemplo de criação de engine para diferentes bancos de dados
# Para SQLite (ou outros bancos SQLAlchemy suporta diretamente)
engine = create_engine('sqlite:///sensors.db')

# Para Oracle (caso esteja configurando para Oracle)
# Exemplo: 'oracle+cx_oracle://user:password@host:port/?service_name=your_service'
# engine = create_engine('oracle+cx_oracle://user:password@host:port/?service_name=your_service')

# Criação das tabelas no banco
try:
    Base.metadata.create_all(engine)
except:
    pass

# Exemplo de uso: criando uma sessão para inserção de dados
#Session = sessionmaker(bind=engine)
#session = Session()

# Criando um novo sensor
#novo_sensor = Sensor(identificador='Sensor1', ip='192.168.1.10', latitude=52.516274, longitude=13.377704)

# Adicionando e confirmando a transação
#session.add(novo_sensor)
#session.commit()

# Fechando a sessão
#session.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
