def setup_database(sqlite_file=':memory:'):
    from settings import database
    from models.contribution import Contribution
    from models.contract import Contract
    from models.evaluation import Evaluation
    from models.user import User

    if database.database != sqlite_file:
        database.init(sqlite_file)
    database.connect()
    database.create_tables([User, Contribution, Contract, Evaluation], safe=True)


def init_database(sqlite_file):
    from settings import database
    if database.database != sqlite_file:
        database.init(sqlite_file)
    return database


def reset_database():
    """delete all data from the database"""
    from .models.contribution import Contribution
    from models.contract import Contract
    from .models.evaluation import Evaluation
    from .models.user import User

    db_tables = [Contract, Contribution, Evaluation, User]
    for table in db_tables:
        table.delete().execute()


def get_contract(name=None, contract_id=1):
    """return the contract identified by name

    returns a Contract instance

    TODO: for now, this functino returns a DMagContract()
    """
    from contracts.dmag import DMagContract

    try:
        contract = DMagContract().get(id=contract_id)
    except:
        contract = DMagContract()
        contract.save()
    return contract
