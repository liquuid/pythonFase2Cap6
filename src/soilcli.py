import click
from random import randrange, randint
from models import Sensor, SessionLocal

# Função auxiliar para criar uma nova sessão
def get_session():
    return SessionLocal()


def generate_ipv4():
    # Generate four random numbers between 0 and 255
    return ".".join(str(randint(0, 255)) for _ in range(4))


# CLI principal
@click.group()
def cli():
    """A Simple CLI for Sensor Management"""
    pass

# Create (Criar um novo sensor)
@cli.command()
@click.option('--identificador', prompt='Identificador', help='Identificador do sensor')
@click.option('--ip', prompt='IP', help='Endereço IP do sensor')
@click.option('--latitude', prompt='Latitude', type=float, help='Latitude do sensor')
@click.option('--longitude', prompt='Longitude', type=float, help='Longitude do sensor')
@click.option('--humidade_max', prompt='Humidade Máxima', type=float, help='Humidade Máxima permitida no sensor')
@click.option('--humidade_min', prompt='Humidade Mínima', type=float, help='Humidade Mínima permitida no sensor')
def create(identificador, ip, humidade_max, humidade_min, latitude, longitude):
    """Cria um novo sensor"""
    session = get_session()
    novo_sensor = Sensor(identificador=identificador, ip=ip, humidade_max=humidade_max,humidade_min=humidade_min, latitude=latitude, longitude=longitude)
    session.add(novo_sensor)
    session.commit()
    session.close()
    click.echo(f"Sensor {identificador} criado com sucesso!")

@cli.command()
@click.option('--quantidade', prompt='Quantidade', type=int, help='Quantidade de sensores')
def populate(quantidade=10):
    """Cria varios sensores com valores aleatórios"""
    session = get_session()
    max_try = 5
    while quantidade > 0:
        print(max_try)
        try:
            novo_sensor = Sensor(identificador=randrange(10000,100000), ip=generate_ipv4(), humidade_max=randrange(0,100),humidade_min=randrange(0,100), latitude=randrange(0,90), longitude=randrange(0,180))
            session.add(novo_sensor)
            session.commit()
            print(novo_sensor)
            quantidade -= 1
            max_try = 5
        except Exception as error:
            session.close()
        if max_try > 1:
            max_try -= 1
        else:
            break
        
    session.close()


# Read (Listar todos os sensores)
@cli.command()
def read():
    """Lista todos os sensores cadastrados"""
    session = get_session()
    sensores = session.query(Sensor).all()
    session.close()
    if sensores:
        for sensor in sensores:
            click.echo(f"ID: {sensor.identificador}, IP: {sensor.ip}, Hmin: {sensor.humidade_min}, Hmax: {sensor.humidade_max}, Hultimo_valor: {sensor.humidade_ultimo_valor}, Localização: ({sensor.latitude}, {sensor.longitude})")
    else:
        click.echo("Nenhum sensor encontrado.")

# Update (Atualizar um sensor existente)
@cli.command()
@click.option('--identificador', prompt='Identificador', help='Identificador do sensor a ser atualizado')
@click.option('--ip', prompt='Novo IP', help='Novo endereço IP do sensor')
@click.option('--latitude', prompt='Nova Latitude', type=float, help='Nova latitude do sensor')
@click.option('--longitude', prompt='Nova Longitude', type=float, help='Nova longitude do sensor')
@click.option('--humidade_max', prompt='Humidade Máxima', type=float, help='Humidade Máxima permitida no sensor')
@click.option('--humidade_min', prompt='Humidade Mínima', type=float, help='Humidade Mínima permitida no sensor')
def update(identificador, ip, humidade_max, humidade_min, latitude, longitude):
    """Atualiza as informações de um sensor existente"""
    session = get_session()
    sensor = session.query(Sensor).filter_by(identificador=identificador).first()
    if sensor:
        sensor.ip = ip
        sensor.latitude = latitude
        sensor.longitude = longitude
        sensor.humidade_min = humidade_min
        sensor.humidade_max = humidade_max
        session.commit()
        click.echo(f"Sensor {identificador} atualizado com sucesso!")
    else:
        click.echo(f"Sensor com identificador {identificador} não encontrado.")
    session.close()

# Delete (Deletar um sensor existente)
@cli.command()
@click.option('--identificador', prompt='Identificador', help='Identificador do sensor a ser deletado')
def delete(identificador):
    """Deleta um sensor existente"""
    session = get_session()
    sensor = session.query(Sensor).filter_by(identificador=identificador).first()
    if sensor:
        session.delete(sensor)
        session.commit()
        click.echo(f"Sensor {identificador} deletado com sucesso!")
    else:
        click.echo(f"Sensor com identificador {identificador} não encontrado.")
    session.close()

@cli.command()
def get_data():
    """ Carrega os dados de todos os sensores """
    session = get_session()
    sensores = session.query(Sensor).all()

    # itera por uma lista de sensores
    for sensor in sensores: 
        print(sensor.get_hum(session))
    session.close()

@cli.command()
def irrigar():
    """ Envia o comando para irrigar """
    session = get_session()
    sensores = session.query(Sensor).all()

    # itera por uma lista de sensores
    for sensor in sensores:
        sensor.get_hum(session)
        if sensor.humidade_min >= sensor.humidade_ultimo_valor:
            print(sensor.open_water(600))
        elif sensor.humidade_ultimo_valor >= sensor.humidade_max:
            print("Solo encharcado em (", sensor.latitude, "," ,sensor.longitude, ")")
        else:
            print("Solo dentro dos parâmetros em (", sensor.latitude, "," ,sensor.longitude, ")")

    session.close()


# Iniciar a CLI
if __name__ == '__main__':
    cli()