from rolepermissions.roles import AbstractUserRole

class Gestores(AbstractUserRole):
    available_permissions = {
        'create_patrimonios': True,
        'read_patrimonios': True,
        'update_patrimonios': True,
        'delete_patrimonios': True,
        
        'create_ambientes': True,
        'read_ambientes': True,
        'update_ambientes': True,
        'delete_ambientes': True,

        'create_ordemServico': True,
        'read_ordemServico': True,
        'update_ordemServico': True,
        'delete_ordemServico': False,
    }

class Manutentores(AbstractUserRole):
    available_permissions = {
        'create_patrimonios': False,
        'read_patrimonios': True,
        'update_patrimonios': False,
        'delete_patrimonios': False,
        
        'create_ambientes': False,
        'read_ambientes': True,
        'update_ambientes': False,
        'delete_ambientes': False,

        'create_ordemServico': True,
        'read_ordemServico': True,
        'update_ordemServico': True,
        'delete_ordemServico': True,
    }

class Responsaveis(AbstractUserRole):
    available_permissions = {
        'create_patrimonios': False,
        'read_patrimonios': True,
        'update_patrimonios': False,
        'delete_patrimonios': False,
        
        'create_ambientes': False,
        'read_ambientes': True,
        'update_ambientes': False,
        'delete_ambientes': False,

        'create_ordemServico': True,
        'read_ordemServico': True,
        'update_ordemServico': True,
        'delete_ordemServico': False,
    }